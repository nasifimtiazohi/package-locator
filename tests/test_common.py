import json
import requests
from package_locator.common import *


def test_search_for_github_repo():
    def search_pypi(package):
        url = "https://pypi.org/pypi/{}/json".format(package)
        page = requests.get(url)
        data = json.loads(page.content)
        urls = search_for_github_repo(data)
        return urls

    package = "gradio"
    urls = search_pypi(package)
    assert len(urls) == 1
    assert "https://github.com/gradio-app/gradio-UI" in urls

    package = "rsa"
    urls = search_pypi(package)
    assert len(urls) == 1
    assert "https://github.com/sybrenstuvel/python-rsa" in urls
