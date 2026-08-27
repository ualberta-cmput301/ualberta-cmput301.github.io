Title: Lab 4 Participation Exercise
date: 2026-06-30
tags: labs, policy, grading
authors: Raj Prasad, Michelle Deng
status: published
summary: Lab 4 Participation Exercise

[TOC]

# Lab 4 Slides

[Lab 4 Slides]({attach}slides/2026-Lab-4_Github.pdf)

## Extra Information

### Command Line Authentication to GitHub

If you use Git from the command line, GitHub may ask you to authenticate when you run commands such as `git clone`, `git pull`, or `git push`.

GitHub does not accept account passwords for Git operations. Instead, you should use one of the following methods:

- GitHub Desktop
- Android Studio GitHub sign-in
- Git Credential Manager
- Personal Access Token
- SSH key

The slides show how to use a Personal Access Token. GitHub also provides documentation on authentication here:

- [Creating a Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- [Caching your GitHub credentials](https://docs.github.com/en/get-started/getting-started-with-git/caching-your-github-credentials-in-git)

You may also use the GitHub CLI if you prefer:

- [GitHub CLI installation](https://github.com/cli/cli#installation)
- [GitHub CLI authentication command](https://cli.github.com/manual/gh_auth_login)

After installing GitHub CLI, you can run:

```bash
gh auth login
```

Follow the prompts in the terminal. Choose the options that match the way your team is using GitHub.

## Sensitive Information and Git

### What is Sensitive Information

Git tracks the history of files that are committed to a repository. This means that even if you delete a file or remove part of a file later, the old version may still exist in the repository history.

Do not commit sensitive information. 

Sensitive information includes:

- student ID numbers
- passwords
- API keys
- access tokens
- private credentials
- personal information that should not be public

If sensitive information is committed, it can be difficult to fully remove. GitHub provides documentation on preventing data leaks here:

[Best practices for preventing data leaks](https://docs.github.com/en/code-security/getting-started/best-practices-for-preventing-data-leaks-in-your-organization)

GitHub also provides documentation on removing sensitive information from a repository, but this should only be used in an emergency because it can affect the repository history.

# Lab 4 Participation Exercise

This task is for teams. 

1. As a team:

    - Create a GitHub Organization.
    - Create a repository under this organization
        - Use your team name as a repository name
    - Create a `README.md` file for that repository 
    - Add your members as **collaborators** so the whole team will be able to commit to their own branches.
    - Add a `.gitignore` file appropriate for an Android Studio project.
        - Do not include Android Studio settings files such as `.idea/`.
        - Do not include project build folders.
    - Create a new Android Studio project (1 project per team) with the same name as the repo name (Team name).
    - Your android project folder is your local repository and write all the commands within this repo/directory.
    - Connect your local project to the GitHub repository using `git remote add origin`.
    - Use 'git init', 'git add', 'git commit', and 'git push' to push your code to the remote
    - Create a Kotlin abstract class Shape with x and y  integer fields (as a team).
    - Commit the change and push it to GitHub.

2. As a member, on your local machine:

    - Clone the repository 
        - Do **not** fork the repository 
    - Create a branch with your name 
        - Do **not** use your CCID as the branch name
    - Create a Kotlin class (ex. circle, rectangle, star, etc) that extends Shape in your own branch.
    - Commit the change and push your branch to GitHub.
    - Create a pull request from your branch to main in Github.
    - Ask another member to review it and merge your pull request.
    - After your pull request is merged: 
        - Stay on your local branch
        - Edit the Shape class by adding a color string field. (val color: String = "blue") (local your-own branch)
        - Commit the change. (Do **not** push this commit just yet)
3. As a team:

    - Edit the Shape class in the main branch **on GitHub** by adding a **color** string field. (val color: String = "$PUT_YOUR_CHOICE_OF_COLOR")
    - Commit the change in GitHub.

4. As a member, on your local machine:

    - Pull the latest main branch from GitHub into your own branch. 
        - You should have a merge conflict. (**Origin/main -> local your-branch**)
    - Resolve the conflict in the Shape class
    - Commit the resolved file change.
    - Push your branch to GitHub.


Please submit:

1. Your CCID (not your student id number!)

2. Link to your branch in the repository at Canvas

**Due Date**

Friday after the Thursday lab at 5 PM