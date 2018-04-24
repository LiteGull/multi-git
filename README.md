# multigit

### Introduction

multigit is a tool which allows the user to interact with Git repositories in multiple directories and run commands
such as changing the branch all repositories are on as well as make pull requests from each repositories current branch.

### Usage

The simplest way to comsume this tool is to clone the repository locally:
```git@github.com:LiteGull/multigit.git```
Then set an alias in your ~/.bashrc (or where ever you create your alias) which points executes the src/main.py:
```alias multigit="python3 ~/path-to-dir/multigit/src/main.py"```
This will then execute the code in the current working directory and depending on which command you pass through push/pull, it will execute that command for each git repository in the current working directory.
