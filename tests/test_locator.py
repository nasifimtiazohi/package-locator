from requests.api import get
from package_locator.locator import *
from giturlparse import parse


def test_npm():
    assert get_npm_location("lodash") == ("https://github.com/lodash/lodash", "")
    assert get_npm_location("react") == ("https://github.com/facebook/react", "packages/react")


def test_rubygems():
    assert get_rubygems_location("bundler") == ("https://github.com/rubygems/rubygems", "bundler")
    assert get_rubygems_location("a4nt") == ("https://github.com/ma2gedev/a4nt", "")


def test_pypi():
    assert get_pypi_location("django") == ("https://github.com/django/django", "")
    assert get_pypi_location("rsa") == ("https://github.com/sybrenstuvel/python-rsa", "")


def test_composer():
    assert get_composer_location("psr/log") == ("https://github.com/php-fig/log", "")


def test_cargo():
    assert get_cargo_location("depdive") == ("https://github.com/diem/whackadep", "depdive")


def test_get_base_repo_url():
    assert get_base_repo_url("https://github.com/php-fig/log.git/tree/3.0.0") == "https://github.com/php-fig/log"
