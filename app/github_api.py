import requests
import links_from_header
import os
from dotenv import load_dotenv


load_dotenv()


def get_auth():
    """
    Reads the setting file and sets the github api credentials. If not found,
    None is returned and the system runs unauthenticated.
    """
    auth = (os.environ["GITHUB_API_USER"], os.environ.get("GITHUB_API_KEY"))

    if all(auth):
        return auth

    return None


def _get_user_repositories_page(user_name, page_link=None):
    """
    Lists a developer's repositories. Receives an username/login. E.g.
    'h3nnn4n'. This is paginated. The first query returns a 'next' link, which
    should be passed back to this function via the `page_link` parameter.
    """
    auth = get_auth()

    result = requests.get(
        page_link or f"https://api.github.com/users/{user_name}/repos",
        auth=auth,
    )

    if "link" in result.headers.keys():
        links = links_from_header.extract(result.headers["link"])
    else:
        links = {}

    return result.json(), links


def list_repositories(user_name):
    next_page_link = None

    while True:
        data, links = _get_user_repositories_page(user_name, page_link=next_page_link)

        for repository in data:
            yield repository

        next_page_link = links.get("next")

        if next_page_link is None:
            break
