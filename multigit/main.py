import os
import argparse

from log import logger_setup
from git_repos import GitRepo, GitCommand

parser = argparse.ArgumentParser(description='Process the git command the user wants to run.')
parser.add_argument('git_command', help='git command to run e.g. Push/Pull')
args = parser.parse_args()


def main():
    logger.info(" --- multigit --- ")
    
    git_repo = GitRepo()
    command = GitCommand(command=args.git_command)
    
    repos = git_repo.list_all_git_repos()
    logger.info("git repositories in current directory {}".format(repos))
    
    for repo in repos:
        logger.debug("Running git command on {} repository".format(repo['repo']))
        command.execute(repo)


if __name__ == "__main__":
    logger = logger_setup()
    main()
