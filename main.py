import os
import git

import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--git_command', help='git command to run e.g. Push/Pull')

args = parser.parse_args()


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

    def pull_repo(self, dir):
        try:
            repo = git.Repo(dir).remotes.origin
            repo.pull()
            return True
        except Exception:
            return False

    def push_repo(self, dir):
        try:
            repo = git.Repo(dir).remotes.origin
            repo.push()
            return True
        except Exception:
            return False

    def push_req(self):
        global repo_pull
        repo_pull = git_repo.push_repo(r)
        if repo_pull is True:
            print("{r} has successfully pushed the repo".format(r=r))
        else:
            print("{r} has failed to push the repo".format(r=r))

    def pull_req(self):
        global repo_pull
        repo_pull = git_repo.pull_repo(r)
        if repo_pull is True:
            print("{r} has successfully pulled the repo".format(r=r))
        else:
            print("{r} has failed to pull the repo".format(r=r))


if __name__ == "__main__":
    repos = []
    git_repo = GitRepo()
    for d in git_repo.list_all():
        if git_repo.is_git_repo(dir=d) is True:
            repos.append(d)
    for r in repos:
        if args.git_command == "pull":
            git_repo.pull_req()
        elif args.git_command == "push":
            git_repo.push_req()
