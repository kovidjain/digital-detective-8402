# Mission 3 — Operating-system notes

## 1. What an operating system does

An operating system is system software that controls and coordinates a computer's hardware and provides common services for applications. Its responsibilities include:

| Responsibility | What it provides |
| --- | --- |
| Process management | Starts, schedules, pauses, and ends running programs. |
| Memory management | Gives processes working memory and keeps their memory areas organised. |
| File management | Creates, reads, changes, and organises files and folders. |
| Device management | Helps applications use input, output, storage, and other hardware devices. |
| User interface | Provides graphical or command-line ways to interact with the computer. |
| Security and permissions | Controls which users and processes may access resources. |

This makes the operating system a shared manager. An application does not need to control hardware directly for every operation; it requests services from the operating system.

## 2. Processes

A process is a running instance of a program. The program is the stored set of instructions, while the process is the active work created when those instructions run. A process has its own working state, including memory and information about what it is doing.

When I open a writing application, the operating system loads the program, creates a process, gives it memory, and schedules its instructions on the processor. If I open another application, the operating system gives both processes time to run and keeps their memory areas separate. When I close the application, the operating system can release those resources.

## 3. Files, folders, paths, and storage

| Concept | Meaning |
| --- | --- |
| File | A named collection of data, such as a document, image, or program. |
| Folder or directory | A container used to organise files and other folders. |
| Path | The address that identifies a file or folder's location. |
| Storage | Persistent hardware or media that keeps data after a process ends or power is removed. |
| Working memory | Temporary memory used by active processes while they run. |

An absolute path starts from the root of the file system and identifies one location directly. A relative path starts from the current working directory. Paths let applications and users refer to data without relying only on a display name.

## 4. Permissions

Permissions are access rules applied to resources such as files, folders, devices, and processes. They help prevent accidental changes and stop one user or program from freely reading or changing everything on a computer.

Common permission ideas include:

- **Read** — view or retrieve the contents.
- **Write** — change the contents or metadata.
- **Execute** — run a program or enter a directory, depending on the system.

The operating system checks the requesting user or process against the resource's rules. If the request is allowed, the operation continues; otherwise, the operating system reports an access error. This check is useful for both security and safe sharing.

## 5. Example flow: opening and saving a document

1. I select a writing application, and the operating system starts its process.
2. The application asks the operating system to open a document using its path.
3. The operating system checks the path and permissions, then reads the file from storage.
4. The application displays the document and keeps working data in memory.
5. When I choose Save, the application asks the operating system to write the updated data.
6. The operating system checks permission again and transfers the data to storage.

This example shows how an application, process, path, storage device, and permission check work together.
