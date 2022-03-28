# Git and GitHub Professional Course

**[platzi](https://platzi.com/cursos/git-github/) | Freddy Vega**

<br>

Stop versioning your projects using your own version control system. Better use Git, the quintessential version control system used by the technology industry. Learn how to work with git, basic concepts, clone a repository, and manage your projects by hosting them in your local repository and on GitHub.

## Learning Objectives

- Take a Version Control in your Projects with Git
- Work in Teams Collaboratively
- Using Custom Domains with GitHub Pages
- Install Git on your operating system

## Syllabus

### Basic commands in Git

- Creating and working with repositories: `git init`, `git add`, `git push`, `git status`
- Set user and email in Git: `git config --global user [or email] 'username [or email]'`
- Check main configurations in Git`git config --list` or `git config --list --show-origin`
- Check history and file versions: `git log 'file' --stat` or `git show 'file'`
- Stage area: the basic work cycle in Git: `git resert [commit] --hard` and `git resert [commit] --soft`
- Working with `branch`, `merge`, and `checkout`
- `git reset` vs. `git rm`

### Basic workflow in GitHub

- Conflict resolution with `merge`, `git pull origin main --allow-unrelated-histories`

- Commands to work with tags:
  - Create a new tag and assign it to a commit: `git tag [tag-name] [commit-id]`
  - Delete a tag in the locally: `git tag -d [tag-name]`
  - List tags locally: `git tag` or `git show-ref --tags`
  - Push tags: `git push origin --tags`
  - Delete tags from remote repository: `git tag -d [tag-name]` && `git push origin :refs/tags/tag-name`

- How to add a git-only alias:
  - Single project: `git config alias.superlog "log --all --graph --decorate --oneline"`
  - Global: `git config --global alias.superlog "log --all --graph --decorate --oneline"` 
  - With format: `git config alias.superlog "log --graph --abbrev-commit --decorate --date=relative --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(bold yellow)%d%C(reset)' --all"`
  - To run: `git superlog`

- Working with private and public keys:
  - Generating SSH keys: `ssh-keygen -t rsa -b 4096 -C "youremail@example.com"`
  - Turn on the SSH server: `eval $(ssh-agent - s)`
  - Adding the SSH to the server: `ssh-add [origin-path-private-key]`
  - Conect GitHub with SSH: `git remote set-url origin [ssh-url-repository]`

- Working wit branches:
  - Create a branch locally: `git branch [branch-name]` or `gir checkout -b [branch-name`
  - Change branch: `git checkout [branch-name]`
  - Push local branches: `git push origin [branch-name]`
  - See current branches and their history: `git show-branch [--all]` or `git branch`


- Configure multiple collaborators in Git

### Professional Workflows

- Pull requests
- Fork: contribute to a project
- Deployment to a server

## Multiples Worflows

- `git rebase`
- `git stash`
- `git clean`
- `git cherry-pick`
- `git reset` and `git reflog`
