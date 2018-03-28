import os
import git
import argparse
import logging

from log import logger_setup


class GitRepo:
    def get_cwd(self):
        dir_path = os.getcwd()
        return dir_path

    def list_all(self):
        dir = self.get_cwd()
        return os.listdir(dir)

    def is_git_repo(self, dir):
        try:
            _ = git.Repo(dir).git_dir
            return True
        except git.exc.InvalidGitRepositoryError:
            return False

    def get_remote(self, dir):
        try:
            return git.Repo(dir).remotes.origin
        except Exception:
            return False

    def pull_repo(self, dir):
        try:
            repo = self.get_remote(dir)
            repo.pull()
            return True
        except Exception:
            return False

    def push_repo(self, dir):
        try:
            repo = self.get_remote(dir)
            repo.push()
            return True
        except Exception:
            return False

    def push_req(self, repo):
        repo_pull = self.push_repo(repo)
        if repo_pull is True:
            logger.info("{r} has successfully pushed the repo".format(r=repo))
        else:
            logger.info("{r} has failed to push the repo".format(r=repo))

    def pull_req(self, repo):
        repo_pull = self.pull_repo(repo)
        if repo_pull is True:
            logger.info("{r} has successfully pulled the repo".format(r=repo))
        else:
            logger.info("{r} has failed to pull the repo".format(r=repo))

    def run_command_on_repos(self, git_repo, repos):
        for repo in repos:
            if args.git_command == "pull":
                git_repo.pull_req(repo)
            elif args.git_command == "push":
                git_repo.push_req(repo)

    def list_all_git_repos(self, git_repo, repos):
        for d in git_repo.list_all():
            if git_repo.is_git_repo(dir=d) is True:
                repos.append(d)


def main():
    logger.info(" --- multigit --- ")
    repos = []
    git_repo = GitRepo()
    git_repo.list_all_git_repos(git_repo, repos)
    git_repo.run_command_on_repos(git_repo, repos)


def parser_func():
    global args
    parser = argparse.ArgumentParser(description='Process the git command the user wants to run.')
    parser.add_argument('git_command', help='git command to run e.g. Push/Pull')
    args = parser.parse_args()


if __name__ == "__main__":
    logger = logger_setup()
    parser_func()
    main()
