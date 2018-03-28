import os
import git
import argparse
import logging

from log import logger_setup
from git_repos import GitRepo, GitCommand

parser = argparse.ArgumentParser(description='Process the git command the user wants to run.')
parser.add_argument('git_command', help='git command to run e.g. Push/Pull')
args = parser.parse_args()


def main():
    logger.info(" --- multigit --- ")
    git_repo = GitRepo()
    command = GitCommand()
    repos = git_repo.list_all_git_repos()
    for repo in repos:
        if args.git_command == "pull":
            command.pull(repo)
        elif args.git_command == "push":
            command.push(repo)


if __name__ == "__main__":
    logger = logger_setup()
    main()
