import subprocess
import os


def download_repository(repository):
    print(f"fetching {repository.get('full_name')}")

    if not os.path.exists("bkp"):
        os.mkdir("bkp")

    os.chdir("bkp")

    if not os.path.exists(repository.get("name")):
        subprocess.run(["git", "clone", repository.get("clone_url")])

    os.chdir(repository.get("name"))
    subprocess.run(["git", "fetch", "--all"])
    os.chdir("../..")

    print("done")
