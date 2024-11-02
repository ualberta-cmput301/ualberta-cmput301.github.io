Title: Lab 4 Participation Exercise
date: 2024-01-06
tags: labs, policy, grading
authors: Samuel Iwuchukwu,Hazel Victoria Campbell
status: published
summary: Lab 4 Participation Exercise

[TOC]

# Lab 4 Slides

- [Lab 4 Slides]({attach}slides/Github_Slides.pdf)
- [Lab 4 Slides (Old Version)]({attach}slides/Lab4.pdf)

## Extra Information

### Command Line Authentication to GitHub

- In the slides, authentication with GitHub is done using a token you generate with our account.
- GitHub has a command line tool which makes this process easier, and will generate and manage the token for you.
- GitHub has documentation about how to do this [here](https://docs.github.com/en/get-started/getting-started-with-git/caching-your-github-credentials-in-git).
  - The summary of these steps is to first install the GitHub CLI, which will depend on what operating system you are using. The instructions for installation is [here](https://github.com/cli/cli#installation).
  - Then, with the CLI tool installed, run the command `gh auth login`. The terminal will guide you through what you need to do. Please make sure to select that you want a **GitHub.com** account and want to use **SSH** as your protocol.
  - The documentation for the authentication command is located [here](https://cli.github.com/manual/gh_auth_login)

## Sensitive Information and Git

### What is Sensitive Information

- Git is a version control system which tracks all files, past and current, that you commit to it.
- This means that even if you remove a file or part of a file from your repository, it is still tracked and accessible in the history of your repository.
- As such, if you commit sensitive data, it is very difficult, if not impossible, to remove it.
  - Sensitive data includes anything such as ID numbers (like your student ID number), API keys, passwords, etc.
-  GitHub as some excellent documentation about best practices for avoiding this, located [here](https://docs.github.com/en/code-security/getting-started/best-practices-for-preventing-data-leaks-in-your-organization).
- There is also information about removing sensitive information from your repository, but this should only be used in an emergency as it can have severe consequences if not done properly.

# Lab 4 Participation Exercise

This task is for teams. 

1. As a team:

    + Create an Organization in GitHub and then create a repository (repo name: Team name) under this organization. 
    + Add your members as collaborators so the whole team will be able to commit to their branches.
    + Create a new Android Studio project (1 project per team) with the same name as the repo name (Team name).
    + Your android project folder is your local repository and write all the commands within this repo/directory.
    + Use 'git init', 'git add', 'git commit', and 'git push' to push your code to the remote
    + Use 'git remote add origin' to add the URL of your remote repo to this local repo.
    + The repository should include .gitignore to not include Android Studio settings files (.idea) and the project build folder.
    + Create an abstract class Shape (java file) with x and y  integer fields (as a team).
    + Commit the change and push it to GitHub.

2. As a member, on your local machine:

    + (Do not fork) Clone the repository and create a branch with your name (do not use CCID).
    + Create a model class (ex. circle, rectangle, star, etc) (new java file) that extends Shape in your own branch.
    + Commit the change and push the branch to GitHub.
    + Create a pull request to main in Github.
    + Ask another member to merge it.
    + Edit the Shape class by adding a color string field. (String color = "blue";) (local your-own branch)
    + Commit the change. (Don't push it)
3. As a team:

    + Edit the Shape class in the main branch **on GitHub** by adding a **color** string field. (String color = "$PUT_YOUR_CHOICE_OF_COLOR";)
    + Commit the change in GitHub.
4. As a member, on your local machine:

    + Pull the main branch from GitHub. You should have a conflict. (**Origin/main -> local your-own**)
    + Resolve the conflict.
    + Commit the change.
    + Push the branch to GitHub.


Please submit:

1. Your CCID (not your student id number!)

2. Link to your branch in the repository at eClass

**Due Date**

Friday after the Thursday lab at 4PM