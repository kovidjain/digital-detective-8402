# Mission 2 — CLI practice evidence

The following is a privacy-safe record of the practice. Local paths, account names, owner fields, and package names are not included.

## File operations

| Operation | Observation |
| --- | --- |
| `pwd` | Printed the repository's current local path. |
| `ls` and `ls -l` | Showed the repository entries and detailed metadata. |
| `cd ..` followed by `cd -` | Moved to the parent and returned to the repository. |
| `mkdir`, `touch`, `cp`, and `mv` | Created an empty file, copied it, and renamed the copy. |
| `printf` with `>` and `>>` | Created a two-line text file by replacing then appending. |
| `cat` and `wc -c` | Displayed the text and checked its byte count. |

## Flags and pipe

`ls` did not show the hidden demonstration file. `ls -lah` showed it and included detailed, human-readable information. The command `ls -lah | head -n 5` sent the detailed listing to `head`, which displayed only the first five lines.

## Package manager

Homebrew was checked without installing or removing packages. Only the version and general package-manager observations were retained; package names and machine-specific details were left out.
