from package_locator.locator import *


def test_npm():
    assert get_npm_location("lodash") == ("https://github.com/lodash/lodash", "")
    assert get_npm_location("react") == ("https://github.com/facebook/react", "packages/react")


def test_rubygems():
    assert get_rubygems_location("bundler") == ("https://github.com/rubygems/rubygems/", "bundler")
    assert get_rubygems_location("a4nt") == ("https://github.com/ma2gedev/a4nt", "")


def test_pypi():
    assert get_pypi_location("django") == ("https://github.com/django/django", "")
    assert get_pypi_location("rsa") == ("https://github.com/sybrenstuvel/python-rsa", "")
