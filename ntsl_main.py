from rich import print
import sys
import os

from src.core.prompt import get_prompt
from src.core.parser import parse_command

from src.builtin.help import help_command
from src.builtin.cls import cls_command
from src.builtin.exit import exit_command
from src.builtin.pwd import pwd_command
from src.builtin.ls import ls_command
from src.builtin.cd import cd_command
from src.builtin.mkdir import mkdir_command
from src.builtin.touch import touch_command
from src.builtin.cat import cat_command
from src.builtin.rnm import rnm_command
from src.builtin.echo import echo_command
from src.builtin.about import about_command

os.chdir(os.path.dirname(os.path.abspath(__file__)))

if getattr(sys, 'frozen', False):
    os.chdir(os.path.dirname(sys.executable))

print(
    "[yellow]NetShell(c) [v1.6-alfa]\n"
    "All rights reserved by NetShell Team.[/yellow]"
)

commands = {
    "help": help_command,
    "cls": cls_command,
    "exit": exit_command,
    "pwd": pwd_command,
    "ls": ls_command,
    "cd": cd_command,
    "mkdir": mkdir_command,
    "touch": touch_command,
    "cat": cat_command,
    "rnm": rnm_command,
    "echo": echo_command,
    "about": about_command
}

while True:

    command_line = input(get_prompt())

    cmd, args = parse_command(command_line)

    if not cmd:
        continue

    if cmd in commands:
        commands[cmd](args)

    else:
        print(
            f"[red]Syntax Error: "
            f"'{cmd}' is not a defined command.[/red]"
        )