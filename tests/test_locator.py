from package_locator.locator import *
from package_locator.common import *


def test_npm():
    assert get_repository_url_and_subdir(NPM, "lodash") == ("https://github.com/lodash/lodash", "./")
    assert get_repository_url_and_subdir(NPM, "react") == ("https://github.com/facebook/react", "./packages/react")
    assert get_repository_url_and_subdir(NPM, "babel-core") == (
        "https://github.com/babel/babel",
        "./packages/babel-core",
    )
    assert get_repository_url_and_subdir(NPM, "@babel/plugin-syntax-typescript") == (
        "https://github.com/babel/babel",
        "./packages/babel-plugin-syntax-typescript",
    )


def test_rubygems():
    assert get_repository_url_and_subdir(RUBYGEMS, "bundler") == ("https://github.com/rubygems/rubygems", "./bundler")
    assert get_repository_url_and_subdir(RUBYGEMS, "a4nt") == ("https://github.com/ma2gedev/a4nt", "./")
    assert get_repository_url_and_subdir(RUBYGEMS, "safety_net_attestation") == (
        "https://github.com/bdewater/safety_net_attestation",
        "./",
    )
    assert get_repository_url_and_subdir(RUBYGEMS, "builder") == ("https://github.com/jimweirich/builder", "./")


def test_pypi():
    assert get_repository_url_and_subdir(PYPI, "django") == ("https://github.com/django/django", "./")
    assert get_repository_url_and_subdir(PYPI, "rsa") == ("https://github.com/sybrenstuvel/python-rsa", "./")
    assert get_repository_url_and_subdir(PYPI, "hypothesis") == (
        "https://github.com/HypothesisWorks/hypothesis",
        "./hypothesis-python/src",
    )
    assert get_repository_url_and_subdir(PYPI, "six") == ("https://github.com/benjaminp/six", "./")
    assert get_repository_url_and_subdir(PYPI, "azure-storage-blob") == (
        "https://github.com/Azure/azure-sdk-for-python",
        "./sdk/storage/azure-storage-blob",
    )
    assert get_repository_url_and_subdir(PYPI, "pbr") == ("https://opendev.org/openstack/pbr", "./")
    assert get_repository_url_and_subdir(PYPI, "yappi") == ("https://github.com/sumerc/yappi", "./")
    assert get_repository_url_and_subdir(PYPI, "aiobotocore") == ("https://github.com/aio-libs/aiobotocore", "./")
    assert get_repository_url_and_subdir(PYPI, "slacker") == ("https://github.com/os/slacker", "./")
    assert get_repository_url_and_subdir(PYPI, "editdistance") == ("https://www.github.com/roy-ht/editdistance", "./")
    assert get_repository_url_and_subdir(PYPI, "pycountry") == ("https://github.com/flyingcircusio/pycountry", "./")
    assert get_repository_url_and_subdir(PYPI, "py4j") == ("https://github.com/bartdag/py4j", "./py4j-python/src")
    assert get_repository_url_and_subdir(PYPI, "ply") == ("https://github.com/dabeaz/ply", "./")
    assert get_repository_url_and_subdir(PYPI, "aiobotocore") == ("https://github.com/aio-libs/aiobotocore", "./")


def test_composer():
    assert get_repository_url_and_subdir(COMPOSER, "psr/log") == ("https://github.com/php-fig/log", "./")


def test_cargo():
    assert get_repository_url_and_subdir(CARGO, "depdive") == ("https://github.com/diem/whackadep", "./depdive")


def test_get_base_repo_url():
    assert get_base_repo_url("https://github.com/php-fig/log.git/tree/3.0.0") == "https://github.com/php-fig/log"


def test_null_subdir():
    print(get_repository_url_and_subdir(CARGO, "rustc-ap-rustc_ast_passes"))
