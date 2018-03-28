import unittest
import os

from src.git_repos import GitRepo


class TestDirectory(unittest.TestCase):
    def setUp(self):
        self.git_repo = GitRepo()

    def test_returns_current_directory(self):
        self.assertEqual(self.git_repo.get_cwd(), os.getcwd())

    def test_list_all_dirs_in_cwd(self):
        self.assertEqual(self.git_repo.list_all(), ['test_repo', 'test_main.py'])

    def test_if_dir_is_git_repo(self):
        self.assertTrue(self.git_repo.is_git_repo('test_repo'))
