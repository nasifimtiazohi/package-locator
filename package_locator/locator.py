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
    return repo_url, subdir


def get_rubygems_location(package):
    url = "https://rubygems.org/api/v1/gems/{}.json".format(package)
    data = json.loads(requests.get(url).content)
    repo_url = data.get("source_code_uri", "")
    if repo_url:
        # validate get subdirectory
        subdir = get_rubygems_subdir(package, repo_url)
        if subdir:
            return repo_url, subdir

    urls = search_for_github_repo(data)
    for url in urls:
        print("adsdasd", url)
        subdir = get_rubygems_subdir(package, url)
        return url, subdir


def get_repository_url_and_subdir(ecosystem, package):
    if ecosystem == NPM:
        return get_npm_location(package)
