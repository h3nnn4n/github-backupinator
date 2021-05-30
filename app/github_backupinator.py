from . import github_api
from . import downloader


def main():
    repositories = github_api.list_repositories("h3nnn4n")

    for repository in repositories:
        downloader.download_repository(repository)
