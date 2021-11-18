import tempfile
import os
import json
from git import Repo
from pathlib import Path
from os.path import join, relpath

from package_locator.common import NotPackageRepository


def locate_file_in_repo(repo_path, target_file):
    candidates = []
    for root, dirs, files in os.walk(repo_path):
        for file in files:
            if file.endswith(target_file):
                candidates.append(relpath(join(root, file), repo_path))
    return candidates


def locate_dir_in_repo(repo_path, target_dir):
    """return the top-level dir"""
    for root, dirs, files in os.walk(repo_path):
        for dir in dirs:
            if dir.endswith(target_dir):
                return relpath(join(root, dir), repo_path)


def get_package_name_from_npm_json(filepath):
    with open(filepath, "r") as f:
        data = json.load(f)
        return data.get("name", None)


def validate_npm_package_directory(package, repo_url, subdir):
    manifest_filename = "package.json"
    temp_dir = tempfile.TemporaryDirectory()
    repo = Repo.clone_from(repo_url, temp_dir.name)
    repo_path = Path(repo.git_dir).parent

    target_manifest = "{}/{}".format(subdir, manifest_filename) if subdir else manifest_filename
    assert target_manifest in locate_file_in_repo(repo_path, manifest_filename)
    return get_package_name_from_npm_json(join(repo_path, target_manifest)) == package


def get_rubygems_subdir(package, repo_url):
    manifest_filename = "{}.gemspec".format(package)
    temp_dir = tempfile.TemporaryDirectory()
    repo = Repo.clone_from(repo_url, temp_dir.name)
    repo_path = Path(repo.git_dir).parent

    target_manifest = locate_file_in_repo(repo_path, manifest_filename)
    print(target_manifest)
    if not target_manifest:
        raise NotPackageRepository
    assert len(target_manifest) == 1
    subdir = target_manifest[0].removesuffix("{}".format(manifest_filename)).removesuffix("/")
    return subdir


def get_pypi_subdir(package, repo_url):
    """
    There is no manifest file for pypi
    We work on the heuristic that python packages have a common pattern
    of putting library specific code into a directory named on the package
    """
    temp_dir = tempfile.TemporaryDirectory()
    repo = Repo.clone_from(repo_url, temp_dir.name)
    repo_path = Path(repo.git_dir).parent
    dir = locate_dir_in_repo(repo_path, package)
    if not dir:
        raise NotPackageRepository
    return dir.removesuffix(package)
