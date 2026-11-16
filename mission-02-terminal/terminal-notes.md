# Mission 2 — Terminal notes

## 1. Navigation and file management

| Command | Example | What it does |
| --- | --- | --- |
| `pwd` | `pwd` | Prints the path of the current working directory. |
| `ls` | `ls` | Lists files and folders in the current directory. |
| `cd` | `cd notes` | Moves into the `notes` directory. |
| `mkdir` | `mkdir practice` | Creates a new directory. |
| `touch` | `touch draft.txt` | Creates an empty file or updates a file timestamp. |
| `cp` | `cp draft.txt copy.txt` | Copies a file to a new name or location. |
| `mv` | `mv draft.txt final.txt` | Moves or renames a file. |
| `rm` | `rm final.txt` | Removes a selected file. |

The current working directory matters because many commands use relative paths. An absolute path starts from the root of the file system, while a relative path starts from the current directory. I would check the target before using a command that changes or removes files.

## 2. Flags and arguments

A command is the main instruction, an argument identifies what the command should act on, and a flag changes the command's behaviour. For example, `ls -l notes` uses `ls` as the command, `-l` as a flag for a detailed listing, and `notes` as the target.

Flags can make output easier to inspect without changing the underlying files. Common examples include:

- `ls -a` includes hidden entries.
- `ls -l` shows detailed file information.
- `head -n 5 file.txt` displays the first five lines.
- `grep -i "term" file.txt` searches without treating uppercase and lowercase as different.

The exact flags depend on the command and operating system, so I would use a command's help page or manual before relying on an unfamiliar option.

## 3. Pipes

A pipe uses the `|` symbol to send the standard output of one command to the standard input of another command. For example:

```text
ls -l | grep ".md"
```

The first command creates a detailed directory listing. The second command keeps only lines containing `.md`. This is useful because each command does one focused job, while the pipeline combines their results.

Another example is:

```text
cat notes.txt | head -n 10
```

This sends the contents of `notes.txt` to `head`, which displays only the first ten lines.

## 4. Package managers

A package manager is a tool that obtains software packages from configured sources, installs their files, and can manage updates or removal. It also tracks dependencies so that required supporting packages can be installed.

Package managers are different from ordinary application programs because their main purpose is to manage other software. They are also different from the operating system: the operating system provides the environment and core services, while the package manager is one tool used within that environment.

Typical package-manager operations include:

| Operation | Purpose |
| --- | --- |
| Search | Finds an available package by name or description. |
| Install | Downloads and installs a package and its dependencies. |
| Update | Refreshes package information or upgrades installed packages. |
| Remove | Uninstalls a package while using the package database to track it. |

Commands can differ between platforms, so I would check the package manager documentation instead of assuming that one platform's syntax works everywhere.
