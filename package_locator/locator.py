from git import repo
from package_locator.common import *
from package_locator.directory import *
import requests
import json


def get_npm_location(package):
    url = "https://registry.npmjs.org/{}".format(package)
    data = json.loads(requests.get(url).content)

    # TODO: do all npm packages have repo_url data?
    repo_url = parse(data["repository"]["url"]).url2https
    subdir = data["repository"].get("directory", "")
    validate_npm_package_directory(package, repo_url, subdir)
    return repo_url.removesuffix(".git"), subdir


def get_rubygems_location(package):
    url = "https://rubygems.org/api/v1/gems/{}.json".format(package)
    data = json.loads(requests.get(url).content)
    repo_url = data.get("source_code_uri", None)
    if repo_url:
        try:
            subdir = get_rubygems_subdir(package, repo_url)
            if subdir:
                return repo_url.removesuffix(".git"), subdir
        except NotPackageRepository:
            return None

    urls = search_for_github_repo(data)
    for url in urls:
        try:
            subdir = get_rubygems_subdir(package, url)
            return url.removesuffix(".git"), subdir
        except NotPackageRepository:
            continue


def get_pypi_location(package):
    url = "https://pypi.org/pypi/{}/json".format(package)
    data = json.loads(requests.get(url).content)
    repo_url = data["info"].get("project_urls", {}).get("Source Code", None)
    if repo_url:
        try:
            subdir = get_pypi_subdir(package, repo_url)
            if subdir:
                return repo_url.removesuffix(".git"), subdir
        except NotPackageRepository:
            return None

    urls = search_for_github_repo(data)
    for url in urls:
        try:
            subdir = get_pypi_subdir(package, url)
            return url.removesuffix(".git"), subdir
        except NotPackageRepository:
            continue


def get_composer_location(package):
    url = "https://repo.packagist.org/p2/{}.json".format(package)
    data = json.loads(requests.get(url).content)
    data = data["packages"][package][0]
    repo_url = data.get("source", {}).get("url", None)
    if repo_url:
        try:
            subdir = get_composer_subdir(package, repo_url)
            if subdir:
                return repo_url.removesuffix(".git"), subdir
        except NotPackageRepository:
            return None

    urls = search_for_github_repo(data)
    for url in urls:
        try:
            subdir = get_composer_subdir(package, url)
            return url.removesuffix(".git"), subdir
        except NotPackageRepository:
            continue


def get_repository_url_and_subdir(ecosystem, package):
    if ecosystem == NPM:
        return get_npm_location(package)
    elif ecosystem == PYPI:
        return get_pypi_location(package)
    elif ecosystem == RUBYGEMS:
        return get_rubygems_location(package)
    elif ecosystem == COMPOSER:
        return get_composer_location(package)
