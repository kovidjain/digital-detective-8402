# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective

Use the command line to inspect folders, practise safe file management, understand flags and pipes, and explain what package managers do.

## 2. Work completed

- Practised navigation and directory listings.
- Created, copied, renamed, and displayed practice files inside `terminal-practice/`.
- Compared normal, detailed, hidden-file, and human-readable listings.
- Recorded a pipe example and explained the roles of both commands.
- Checked the package-manager situation without installing or removing software.

## 3. Commands / tools used

- `pwd` — displayed the current directory.
- `ls`, `ls -l`, and `ls -lah` — listed files with increasing detail.
- `cd` — changed the current directory.
- `mkdir` and `touch` — created the practice folder and an empty file.
- `cp` and `mv` — copied and renamed the practice file.
- `printf`, `cat`, and `wc -c` — wrote, displayed, and checked text files.
- `head` and `awk` — limited and formatted a listing.
- `brew --version` and `brew list` — checked Homebrew without changing installed packages.

## 4. My understanding

The current-directory command shows where a command will operate when I use a relative path. A normal listing shows visible entries, while `-l` adds file details, `-a` includes hidden entries, and `-h` makes sizes easier to read. A pipe sends the output from one command to the input of another, so small commands can be combined.

`>` replaces a file's contents and `>>` adds text at the end. `cp` makes another copy while leaving the original in place, whereas `mv` moves or renames a path. A package manager helps find, install, update, and remove software while keeping track of dependencies.

## 5. Difficulties faced

It was important to avoid publishing local paths, account names, or package names in the evidence.

## 6. How I resolved them

I kept the practice files generic and recorded only privacy-safe observations. I did not install or remove any packages.

## 7. Evidence / files

- [Terminal notes](terminal-notes.md)
- [CLI practice evidence](evidence/cli-session.md)
- [Practice files](../terminal-practice/)

## 8. Commit details

Commit message: `Complete Terminal and file management mission`

The completed Mission 2 files were committed and pushed to GitHub. No personal account, device, or network details are included.

## Mission title

Become comfortable with the Terminal.

## Task / objective

I needed to practise using a command-line interface for navigation, file management, command options, pipelines, and package management. The aim was to understand what each command does instead of copying commands without checking their effect.

## Work completed

- Documented basic navigation and file-management commands.
- Explained how flags change a command's behaviour.
- Used pipes to pass one command's output into another command.
- Compared package managers with the operating system and application software they install.
- Kept command examples generic and free from personal paths, usernames, or network details.

## Commands / tools used

- `pwd` — displayed the current directory.
- `ls` — listed directory contents.
- `cd` — changed directory.
- `mkdir` and `touch` — created folders and files.
- `cp`, `mv`, and `rm` — copied, moved, renamed, and removed files.
- `cat`, `head`, and `grep` — inspected and filtered text.
- `|` — connected commands in a pipeline.
- A package manager — installed and updated software through package metadata.

## My understanding

The Terminal is a text-based way to communicate with the operating system. Commands are small instructions, arguments provide the target, and flags adjust how a command works. A pipe makes commands more useful together because the output of one command becomes the input of the next command.

## Difficulties faced

It was easy to confuse a command with its argument or flag, especially when several options appeared on one line. File-removal commands also need care because a mistake can affect more than the intended file.

## How I resolved them

I wrote down each command's purpose and separated the command, target, and options in the examples. I used harmless example names and checked the target directory before describing file changes.

## Evidence / files

- [`terminal-notes.md`](terminal-notes.md) — command examples, flags, pipelines, and package-manager notes.

## Commit details

Commit message: `Document terminal fundamentals mission`

Only Mission 2 files are included in this mission commit.
