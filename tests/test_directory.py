from package_locator import locator
from package_locator.common import NPM
import tempfile
from package_locator.directory import *
from os.path import join

repo_url = "https://github.com/facebook/react"
temp_dir_a = tempfile.TemporaryDirectory()
react_repo = Repo.clone_from(repo_url, temp_dir_a.name)

repo_url = "https://github.com/lodash/lodash"
temp_dir_b = tempfile.TemporaryDirectory()
lodash_repo = Repo.clone_from(repo_url, temp_dir_b.name)


def test_locate_file_in_repo():
    file = "package.json"
    path = Path(react_repo.git_dir).parent
    files = locate_file_in_repo(path, file)

    assert "packages/react/{}".format(file) in files
    assert len(files) == 82


def test_get_package_name_from_npm_json():
    file = "packages/react/package.json"
    package = "react"
    path = Path(react_repo.git_dir).parent
    assert get_package_name_from_npm_json(join(path, file)) == package


def test_validate_npm_package_directory():
    package = "react-dom"
    subdir = "packages/react-dom"
    repo_url = "https://github.com/facebook/react"
    assert validate_npm_package_directory(package, repo_url, subdir)

    package = "lodash"
    subdir = ""
    repo_url = "https://github.com/lodash/lodash"
    assert validate_npm_package_directory(package, repo_url, subdir)


def test_get_rubygems_subdir():
    package = "ahoy"
    repo_url = "https://github.com/matsadler/ahoy"
    assert get_rubygems_subdir(package, repo_url) == ""

    package = "bundler"
    repo_url = "https://github.com/rubygems/rubygems"
    assert get_rubygems_subdir(package, repo_url) == "bundler"
