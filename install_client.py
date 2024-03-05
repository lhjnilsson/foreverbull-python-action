import json
import subprocess
from urllib import request


def find_latest_release_wheel():
    url = "https://api.github.com/repos/lhjnilsson/foreverbull/releases/latest"
    with request.urlopen(url) as response:
        data = json.loads(response.read())
    for asset in data["assets"]:
        if asset["name"].endswith(".whl"):
            return asset["browser_download_url"]
    raise Exception("No wheel found in release")


def install_package(package: str):
    subprocess.run(["pip", "install", package])


if __name__ == "__main__":
    install_package(find_latest_release_wheel())
