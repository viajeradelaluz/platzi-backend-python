# Git and GitHub Practice

![](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white)![](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)

<br>

Stop versioning your projects using your own version control system. Better use Git, the quintessential version control system used by the technology industry. Learn how to work with git, basic concepts, clone a repository, and manage your projects by hosting them in your local repository and on GitHub.

### Basic commands in Git

- Creating and working with repositories: `git init`, `git add`, `git push`, `git status`
- Set user and email in Git: `git config --global user [or email] 'username [or email]'`
- Check main configurations in Git`git config --list` or `git config --list --show-origin`
- Check history and file versions: `git log 'file' --stat` or `git show 'file'`
- Stage area: the basic work cycle in Git: `git resert [commit] --hard` and `git resert [commit] --soft`
- - Removing from Stage area: `git rm --cached`
- Working with `branch`, `merge`, and `checkout`
- `git reset` vs. `git rm`

### Basic workflow in GitHub

- Conflict resolution with `merge`, `git pull origin [branch] --allow-unrelated-histories`
- Overwrite saving local changes on stash: `git stash --include-untracked` then `git pull origin [branch]`
- Overwrite discarding local changes: `git clean -fd` then `git pull origin [branch]`

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
  - Turn on the SSH server: `eval $(ssh-agent -s)`
  - Adding the SSH to the server: `ssh-add [origin-path-private-key]`
  - Test your connection: `ssh -T git@github.com`
  - Connect GitHub with SSH: `git remote set-url [origin] [ssh-url-repository]`

- Working wit branches:
  
  - Create a branch locally: `git branch [branch-name]` or `gir checkout -b [branch-name`
  - Change branch: `git checkout [branch-name]`
  - Push local branches: `git push origin [branch-name]`
  - See current branches and their history: `git show-branch [--all]` or `git branch`
  - See remote branches: `git branch -r` or `git branch -a`

### Professional Workflows

- Pull requests
- Fork - Contributing to a project:
  - Showing the current remotes: `git remote -v` or `git remote show [remote]`
  - Adding remotes: `git remote add [name] [url]`
  - Generate an additional remote: `git remote upstream [repo-url]`
  - Get the changes: `git pull upstream [branch]`
  - Add to our forked repository: `git push origin [branch]`
- Deployment to a server

### Multiples Workflows

- Rewrite commits using `git rebase`
- Create a stash with local modifications and revert back to the head commit: `git stash`
- Display a list of all stashes in your repository: `git stash list`
- Apply a commit’s changes onto a different branch with `git cherry-pick [id-commit]`
- Edit a Git commit message by adding a message in quotation marks after the command: `git commit --amend`
- `git clean`
- `git reset` and `git reflog`

### Searches

- Search key-words in files with `git grep [color]`
  
  - Show number line: `git grep -n [color]`
  - Count number of appearances: `git grep -c [color]`

- Search key-words in commits with `git log -S [color]`

- Show number of commits by member: `git shortlog -sn`
  
  - Include commits deleted: `git shortlog -sn --all`
  - Show without `merge` commits: `git shortlog -sn --all --no-merge`

- Show revisions and authors: `git blame [file]`
  
  - Show line by line: `git blame [file] -L[initial-line,final-line]`

<br>

## More resources

- `git [command] --help`
- [Git-scm](https://git-scm.com/)
- [Git commands: A reference guide (by GitKraken)](https://www.gitkraken.com/learn/git/commands)
