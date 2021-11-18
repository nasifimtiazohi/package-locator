from package_locator.locator import *


def test_npm():
    assert get_npm_location("lodash") == ("https://github.com/lodash/lodash.git", "")
    assert get_npm_location("react") == ("https://github.com/facebook/react.git", "packages/react")


def test_rubygems():
    assert get_rubygems_location("bundler") == ("https://github.com/rubygems/rubygems/", "bundler")
    assert get_rubygems_location("a4nt") == ("https://github.com/ma2gedev/a4nt.git", "")
