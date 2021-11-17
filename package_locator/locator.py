from package_locator.common import *
from package_locator.directory import *
import requests
import json
import collections
from giturlparse import parse


def get_npm_location(package):
    url = "https://registry.npmjs.org/{}".format(package)
    data = json.loads(requests.get(url).content)
    repo_url = parse(data["repository"]["url"]).url2https
    subdir = data["repository"].get("directory", "")
    validate_npm_package_directory(package, repo_url, subdir)
    return repo_url, subdir


def get_repository_url_and_subdir(ecosystem, package):
    if ecosystem == NPM:
        return get_npm_location(package)
