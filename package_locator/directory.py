import tempfile
import os
import json
from git import Repo
from pathlib import Path
from os.path import join, relpath


def locate_file_in_repo(repo_path, target_file):
    candidates = []
    for root, dirs, files in os.walk(repo_path):
        for file in files:
            if file.endswith(target_file):
                candidates.append(relpath(join(root, file), repo_path))
    return candidates


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
        return None
    assert len(target_manifest) == 1
    subdir = target_manifest[0].removesuffix("{}".format(manifest_filename)).removesuffix("/")
    return subdir
