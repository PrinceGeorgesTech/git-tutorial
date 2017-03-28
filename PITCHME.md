---
# Git & Github
---
## What we are going to learn.
### Part 1
- Git
  - What is it and what is it used for?
  - How to install and configure git
  - How to clone a git repository (repo)
  - How to stage and unstage changes
  - How to commit and rollback changes
  - Branching
---
## What we are going to learn.
### Part 2
---
- Github
  - What is it and what is it used for?
  - Create and configure a Github account
  - How to push code to github 
  - How to create and merge pull requests
---
## What is Git?
Git is tool used to manage changes to digital files. It allows users to track the files changes as well as where the changes came from.
---
## What is it used for?
Git was originally invented in 2005 to help software engineers working on the Linux OS to collaborate in a distributed fashion. Today it's used by many software projects to help developers merge code changes without overwritting each others work.
---
## Installing and configure git
### Windows 
https://desktop.github.com/
### MacOS
https://desktop.github.com/
### Linux
```bash
sudo apt-get update
sudo apt-get install git
```
---
## How to clone a git repository (repo)
Cloning a repository (repo) - downloading project code and code history on to your machine
```bash
git clone https://github.com/...
```
---
## Inspecting code and code history
```bash
git status # current status of the code
git log # a history of changes make to this code
git show HEAD~1 # the last version of the code
git show HEAD~2 # 2 versions before, etc.
```
---
## Saving code - staging and then commiting
Coding is very precise, so git forces users to be very clear about saving code.
Git has two steps to save code. 
- Staging phase - changes about to be saved
- Commiting phase - changes are more permanently saved
---
## Staging
Please, open a file and make changes to it. 
```bash
git status # Notice the files that have been changed
git add (the name of the file that was changed)
git status # Notice the files that are ready to be saved
```
---
## Unstaging
Let's say we change our mind
```bash
git reset HEAD (the name of the file that was changed)
git checkout (the name of the file that was changed)
git status # Notice how the changes are gone
```
---
# Staging and Unstaging 
Preparing files to be saved permanently 
---
## Committing
Please, open a file and make changes to it. 
```bash
git status # Notice the files that have been changed
git add (the name of the file that was changed)
git status # Notice the files that are ready to be saved
git commit -m "Some message"
git status # Notice how the changes don't show anymore
git show HEAD~1 # Notice how your changes are showing
```
---
## Reverting 
Git gives you the ability to (go back in time)
```bash
git reset HEAD~1 # Notice how your changes are now not commited
get checkout . # Notice how your files are now back to their original state
```
---
# Staging and Unstaging 
Preparing files to be saved permanently 
---
## Branching 
Git gives you the ability to keep multiple tracks of work
---
## Branching
```bash
git checkout -b your-name
git checkout master
git checkout your-name
```
---
## Github - Part 2
---
## What is Github?
Github is a web application that serves as a web repo and UI for git repositories. 
Other similar web applications also exist - gitlab, bitbucket, etc. 
---
## Site demo 
1. Visit site
2. Show code
3. Let students see where to add code
---
## How to push to github
```bash
git push origin HEAD
```
## Visit github and go over merging
