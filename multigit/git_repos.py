import logging
import os
import git

logger = logging.getLogger('log')


class GitRepo:

    def __init__(self):
        self.current_directory = os.getcwd()

    def list_all_git_repos(self):
        repos = []
        for repo in self._listdir():
            if self._is_git_repo(repo=repo) is True:
                repos.append({'repo': repo, 'remote': self._get_remote(repo)})
        return repos

    def _listdir(self):
        return os.listdir(self.current_directory)

    def _is_git_repo(self, repo):
        try:
            _ = git.Repo(repo).git_dir
            return True
        except git.exc.InvalidGitRepositoryError:
            return False

    def _get_remote(self, dir):
        try:
            return git.Repo(dir).remotes.origin
        except Exception:
            return False


class GitCommand:

    def __init__(self, command):
        self.command = command

    def execute(self, repo):
        try:
            # repo['remote'].self.command()
            logger.info(f"{repo['repo']} has successfully {self.command} the repo on remote {repo['remote']}")
        except Exception:
            logger.info(f"{repo['repo']} has failed to {self.command} the repo on remote {repo['remote']}")
