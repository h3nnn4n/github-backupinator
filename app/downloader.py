import subprocess
import os


def _go_to_bkp_dir():
    if not os.path.exists("bkp"):
        os.mkdir("bkp")

    os.chdir("bkp")


def _go_to_repo_dir(repo_name):
    os.chdir(repo_name)


def _restore_dir():
    os.chdir("../..")


def _get_all_branches():
    result = subprocess.run(["git", "branch", "-r"], capture_output=True)
    output = result.stdout.decode()
    branches = [x.strip() for x in output.split("\n")]

    for branch in branches:
        if not branch or "->" in branch:
            continue

        _, _, branch = branch.partition("origin/")

        subprocess.run(["git", "checkout", branch], stdout=subprocess.DEVNULL)
        subprocess.run(["git", "pull", "origin", branch], stdout=subprocess.DEVNULL)


def _clone(repository):
    if not os.path.exists(repository.get("name")):
        subprocess.run(["git", "clone", repository.get("clone_url")], stdout=subprocess.DEVNULL)


def download_repository(repository):
    print(f"fetching {repository.get('full_name')}")

    _go_to_bkp_dir()
    _clone(repository)
    _go_to_repo_dir(repository.get("name"))
    _get_all_branches()
    _restore_dir()

    print("done")
