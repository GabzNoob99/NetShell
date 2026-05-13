import os
from rich import print

def mkdir_command(args):

    if not args:
        dir_name = input('> ').strip()

    else:
        dir_name = args[0]

    if not dir_name:
        print("[red]mkdir requires a directory name.[/red]")
        return

    try:

        os.mkdir(dir_name)

        print(
            f"[green]Info: Directory "
            f"'{dir_name}' created successfully![/green]"
        )

    except FileExistsError:

        print(
            f"[red]Error: Directory "
            f"'{dir_name}' already exists.[/red]"
        )