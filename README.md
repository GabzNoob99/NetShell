# NetShell

A lightweight shell made in Python.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/status-development-orange)
![License](https://img.shields.io/badge/license-MIT-green)

---

## About

NetShell is a custom terminal shell written in Python.

The project was created for learning:
- shell architecture
- command parsing
- filesystem operations
- modular software structure
- terminal development

---

## Features

- Command parser
- Modular builtin commands
- Directory navigation
- File management
- Colored terminal output
- Extensible architecture

---

## Builtin Commands

| Command | Description |
|---|---|
| `help` | Displays help menu |
| `cls` | Clears terminal |
| `exit` | Exits NetShell |
| `pwd` | Shows current directory |
| `ls` | Lists files/directories |
| `cd` | Changes directory |
| `mkdir` | Creates directories |
| `touch` | Creates files |
| `cat` | Reads files |
| `rnm` | Renames files/directories |
| `echo` | Prints messages |
| `gdp` | package manager (building) |

---

## Project Structure

```txt
netshell/
│
├── src/
│   ├── core/
│   └── builtin/
├── assets/
├── dist/
|    ├── documents/
|    └── ntsl_1.6.0A.exe
├── docs/
├── ntsl_main.py
└── ntsl_1.6.0A.exe
```

## Execute Without Executable:

- `pip install rich`
- `python ntsl_main.py`

## Thanks!
account:
https://github.com/GabzNoob99

project:
https://github.com/GabzNoob99/NetShell