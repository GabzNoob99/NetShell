from rich import print

def touch_command(args):

    if not args:
        file_name = input('> ').strip()

    else:
        file_name = args[0]

    if not file_name:
        print("[red]touch requires a file name.[/red]")
        return

    try:

        with open(file_name, 'w'):
            pass

        print(
            f"[green]Info: File "
            f"'{file_name}' created successfully![/green]"
        )

    except Exception:

        print(
            f"[red]Error: Failed to create "
            f"file '{file_name}'.[/red]"
        )