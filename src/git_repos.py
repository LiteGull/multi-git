import logging
import os
import git

logger = logging.getLogger('log')


class GitRepo:

    def get_cwd(self):
        dir_path = os.getcwd()
        return dir_path

    def listdir(self):
        dir = self.get_cwd()
        return os.listdir(dir)

    def is_git_repo(self, repo):
        try:
            _ = git.Repo(repo).git_dir
            return True
        except git.exc.InvalidGitRepositoryError:
            return False

    def get_remote(self, dir):
        try:
            return git.Repo(dir).remotes.origin
        except Exception:
            return False

    def list_all_git_repos(self):
        repos = []
        for repo in self.listdir():
            if self.is_git_repo(repo=repo) is True:
                repos.append({'repo': repo, 'remote': self.get_remote(repo)})
        return repos


class GitCommand:

    def pull(self, repo):
        try:
            repo['remote'].pull()
            logger.info("{repo} has successfully pulled the repo on remote {remote}".format(repo=repo['repo'],remote=repo['remote']))
        except Exception:
            logger.info("{repo} has failed to pull the repo on remote {remote}".format(repo=repo['repo'], remote=repo['remote']))

    def push(self, repo):
        try:
            repo['remote'].push()
            logger.info("{repo} has successfully pushed the repo on remote {remote}".format(repo=repo['repo'],remote=repo['remote']))
        except Exception:
            logger.info("{repo} has failed to push the repo on remote {remote}".format(repo=repo['repo'], remote=repo['remote']))
