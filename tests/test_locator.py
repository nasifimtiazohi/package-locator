import pytest
from package_locator.locator import *


def test_npm():
    assert get_npm_location("lodash") == ("https://github.com/lodash/lodash.git", "")
    assert get_npm_location("react") == ("https://github.com/facebook/react.git", "packages/react")
