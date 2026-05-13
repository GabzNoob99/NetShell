import os
from rich import print

def rnm_command(args):

    if len(args) >= 2:

        old_name = args[0]

        new_name = args[1]

    else:

        old_name = input('>').strip()

        new_name = input('>').strip() if old_name else ''

    if not old_name or not new_name:

        print(
            "[red]rnm requires "
            "old name and new name.[/red]"
        )

        return

    try:

        os.rename(old_name, new_name)

        print(
            f"[green]Info: '{old_name}' renamed "
            f"to '{new_name}' successfully![/green]"
        )

    except FileNotFoundError:

        print(
            f"[red]Error: File or directory "
            f"'{old_name}' not found.[/red]"
        )

    except Exception:

        print(
            f"[red]Error: Failed to rename "
            f"'{old_name}' to '{new_name}'.[/red]"
        )