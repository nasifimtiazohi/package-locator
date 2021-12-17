from zipfile import PyZipFile
from git import repo
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

repo_url = "https://github.com/django/django"
temp_dir_c = tempfile.TemporaryDirectory()
django_repo = Repo.clone_from(repo_url, temp_dir_c.name)

repo_url = "https://github.com/php-fig/log"
temp_dir_d = tempfile.TemporaryDirectory()
psrlog_repo = Repo.clone_from(repo_url, temp_dir_d.name)

repo_url = "https://github.com/diem/whackadep"
temp_dir_e = tempfile.TemporaryDirectory()
depdive_repo = Repo.clone_from(repo_url, temp_dir_e.name)


def test_locate_file_in_dir():
    file = "package.json"
    path = Path(react_repo.git_dir).parent
    files = locate_file_in_dir(path, file)

    assert "packages/react/{}".format(file) in files
    assert len(files) == 82


def test_get_package_name_from_npm_json():
    file = "packages/react/package.json"
    package = "react"
    path = Path(react_repo.git_dir).parent
    assert get_package_name_from_npm_json(join(path, file)) == package


def test_get_rubygems_subdir():
    package = "ahoy"
    repo_url = "https://github.com/matsadler/ahoy"
    assert locate_subdir(RUBYGEMS, package, repo_url) == "./"

    package = "bundler"
    repo_url = "https://github.com/rubygems/rubygems"
    assert locate_subdir(RUBYGEMS, package, repo_url) == "./bundler"


def test_get_composer_subdir():
    package = "psr/log"
    repo_url = "https://github.com/php-fig/log"
    assert locate_subdir(COMPOSER, package, repo_url) == "./"


def test_locate_dir_in_repo():
    package = "django"
    path = Path(django_repo.git_dir).parent
    assert "django" in locate_dir_in_repo(path, package)


def test_get_pypi_subdir():
    package = "django"
    repo_url = "https://github.com/django/django"
    assert locate_subdir(PYPI, package, repo_url) == "./"


def test_get_cargo_subdir():
    package = "depdive"
    repo_url = "https://github.com/diem/whackadep"
    assert locate_subdir(CARGO, package, repo_url) == "./depdive"


def test_pypi_init_file():
    path = Path(django_repo.git_dir).parent
    assert get_pypi_init_file(path) == "django/__init__.py"


def test_commit_subdir():
    package = "foreign-types"
    repo_url = "https://github.com/sfackler/foreign-types"
    assert locate_subdir(CARGO, package, repo_url, "5ae74bfe45f38b0849f8131585c638e741bf0234") == "./"
