Title: Lab 4 Participation Exercise Past Notes
date: 2024-01-06
tags: labs, policy, grading
authors: Samuel Iwuchukwu,Hazel Victoria Campbell
status: published
summary: Lab 4 Participation Exercise

[TOC]

# PAST Lab Git Notes (Romansky)

Preliminaries: Git has two modes it runs in. You can run it as a client which
is what most uses will be. Or, you can run it as a server service. Github
runs git as a service. As a client, you can connect your computer to the
service. The computer offering git as a service is after referred to as a
remote, or remote computer.
You should setup a Github account for this course.
Your Github account should be professional. Please be safe for work!
Your git repositories in this class should all use a FOSS license!
You can read about .gitignore files if you want git to ignore files matching
regular expressions like backup files that end in a ~.

```bash
cmd: git config --global user.name "yourUserName"
cmd: git config --global user.email "your@email.com"
cmd: git config --global core.editor nano
cmd: git config --list
```
description: these commands setup your workstation git configurations which
will be associated with each of the file changes you make through git. So, you
should set them before you do anything.

cmd: git clone <repository address>
description: allows a developer to make a copy of a git repository from a remote
location to the developers local work station.
example: git clone https://github.com/bpython/bpython.git
result: makes a copy of the bpython repo on your computer!

cmd: git branch <branch-name>
description: create a new code branch. The new branch will contain a copy
of the current branches code.
example: git branch bug444
result: creates a branch named bug444

cmd: git branch -a
description: shows all current branches associated with the current working
repo. This will list branches that exist on the local work station and the
remote repositories associated with the repo.

cmd: git push -u origin <branch>
description: this will push a local branch to a given remote git service.
You have to run this command when you make a new local branch that you would
also like to track on the remote server.

cmd: git add <file>
cmd: git rm <file>
description: add or remove a file from gits file tracking system

cmd: git status
description: print the current changes that git can track or is not tracking

cmd: git checkout <branch_name>
cmd: git checkout --branch <branch_name>
description: git checkout lets you change which branch you are working in. The
latter usage changes your current branch and creates a new branch with the
given name.

cmd: git merge <branch_name>
description: git merge will take a given branch name and merge it into your
current working branch. This is useful if you would like to grab features from
another branch of code.

cmd: git pull
cmd: git push
description: fetch the latest commits from origin, or push your latest changes
to origin

Other commands, git remote, git rebase, and git fetch


Last modified: Tuesday, 3 September 2019, 11:58 PM