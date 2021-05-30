import sys

from app.github_backupinator import main as app_main


def main():
    args = sys.argv

    if len(args) < 2:
        return print("please pass a github user name")

    username = args[1]
    app_main(username)


if __name__ == '__main__':
    main()
