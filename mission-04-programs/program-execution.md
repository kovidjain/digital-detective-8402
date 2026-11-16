# Mission 4 — Program execution

## 1. From source code to a running program

Source code is written in a programming language that people can read and edit. A program is the set of instructions saved in one or more source files or translated files. It becomes a process when the operating system starts executing it.

A general flow looks like this:

1. I write source code using the rules of a programming language.
2. A language tool checks the code and translates it, directly or indirectly, into instructions the computer can execute.
3. The operating system starts the program and creates a process.
4. The process receives memory and processor time, performs its instructions, and may read input or write output.
5. The process ends, and the operating system releases its temporary resources.

The exact translation stages depend on the language and implementation.

## 2. Compiler and interpreter comparison

| Tool or approach | Main idea | Typical result |
| --- | --- | --- |
| Compiler | Translates source code into machine code or another lower-level form before execution. | Errors may be reported before the program runs, and the translated result can often run repeatedly. |
| Interpreter | Reads and executes source instructions during a run, often using a runtime environment. | It supports an interactive workflow, although errors may appear when execution reaches the affected instruction. |
| Hybrid runtime | Combines translation and runtime execution stages. | Source code may be converted to an intermediate form and then executed by a virtual machine or runtime. |

These are useful models rather than strict labels for every modern language. A language may have several implementations with different execution strategies.

## 3. Python as an example

Python source code is stored in a text file and is passed to a Python implementation. The implementation checks the syntax and executes the code through its runtime. A common implementation first converts source into an intermediate bytecode form, which is then handled by a virtual machine.

For example:

```python
message = "Hello"
print(message)
```

The source contains an assignment and a function call. During execution, the runtime creates the values needed by the program, sends the text to its output, and the operating system handles the underlying process and output device.

## 4. Errors at different stages

| Stage | Example problem | What happens |
| --- | --- | --- |
| Syntax checking | Missing punctuation or an invalid keyword arrangement. | The language tool reports that the source does not follow the language rules. |
| Translation or loading | A required module or dependency cannot be found. | The program cannot prepare all the code it needs. |
| Runtime | A file is missing or a calculation receives an invalid value. | The process reports an error while it is running. |
| Logic | The code runs but produces the wrong result. | The tool may report no error, so testing and checking the output are needed. |

This distinction helps me decide whether to inspect the code's structure, its dependencies, the current input, or the intended algorithm.
