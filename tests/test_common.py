import json
import requests
from package_locator.common import *


def test_search_for_github_repo():
    package = "gradio"
    url = "https://pypi.org/pypi/{}/json".format(package)
    page = requests.get(url)
    data = json.loads(page.content)
    urls = search_for_github_repo(data)
    assert len(urls) == 1
    assert "https://github.com/gradio-app/gradio-UI.git" in urls
