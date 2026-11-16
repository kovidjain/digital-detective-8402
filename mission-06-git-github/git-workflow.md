# Mission 6 — Git and GitHub workflow

## 1. Git's local workflow

Git tracks files in a repository and records selected changes as commits. The main parts of a simple workflow are:

| Area | Role |
| --- | --- |
| Working tree | The files currently being edited. |
| Staging area | The exact changes selected for the next commit. |
| Local repository | The commit history stored on the current computer. |
| Remote repository | A shared copy hosted elsewhere, such as on GitHub. |

A typical sequence is:

```text
git status
git add path/to/file
git commit -m "Describe the change"
git push
```

`git status` helps me check what changed before I stage anything. `git add` selects changes, and `git commit` records those staged changes with a message. `git push` transfers local commits to a remote branch.

## 2. Commits

A commit is a saved snapshot of staged changes. A useful commit message says what changed, such as `Document terminal fundamentals mission`. Commits form a history, so earlier states can be inspected and compared instead of relying only on the latest files.

Small, focused commits are easier to review and troubleshoot. They also make it clearer which change introduced a problem or completed a particular piece of work.

## 3. Branches

A branch is a movable name pointing to a line of commits. It allows work to happen without immediately changing another branch, such as `main`.

For example:

```text
main:    A --- B
               \
feature:        C --- D
```

The feature branch can be tested and reviewed before its commits are merged into `main`. Branches do not copy every file into a separate universe; they provide names for different points in the commit graph while the working tree shows the selected branch.

## 4. Pull requests

A pull request is a GitHub proposal to merge changes from one branch into another. It normally includes:

- a title and description of the proposed change;
- a comparison showing changed files;
- automated checks such as tests or linting;
- review comments and approval decisions;
- a merge action after the required checks and reviews pass.

The pull request is a collaboration and review layer around Git branches. Git can create and transfer the commits, while GitHub provides the discussion, checks, permissions, and merge interface.

## 5. Collaboration workflow

1. I create or select a branch for one focused change.
2. I edit files and use `git status` to inspect the working tree.
3. I stage only the intended files.
4. I create a clear commit and run the relevant checks.
5. I push the branch to the remote repository.
6. I open a pull request and explain the change.
7. Reviewers inspect the diff and leave comments.
8. I address requested changes with additional commits.
9. After checks and review are complete, the pull request is merged.

This workflow keeps the shared branch stable while still making the history and decisions visible.
