from . import github_api
from . import downloader


def main(username):
    repositories = github_api.list_repositories(username)

    for repository in repositories:
        downloader.download_repository(repository)
