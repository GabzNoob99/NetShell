import os
from rich import print

def cd_command(args):

    if not args:
        path = input('> ').strip()

    else:
        path = args[0]

    if not path:
        print("[red]cd requires a path.[/red]")
        return

    try:
        os.chdir(path)

    except FileNotFoundError:

        print(
            f"[red]Diretório não encontrado: "
            f"{path}[/red]"
        )