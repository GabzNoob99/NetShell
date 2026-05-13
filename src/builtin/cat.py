from rich import print

def cat_command(args):

    if not args:
        file_name = input('>').strip()

    else:
        file_name = args[0]

    if not file_name:
        print("[red]cat requires a file name.[/red]")
        return

    try:

        with open(file_name, 'r') as f:

            content = f.read()

            print(content)

    except FileNotFoundError:

        print(
            f"[red]Error: File "
            f"'{file_name}' not found.[/red]"
        )

    except Exception:

        print(
            f"[red]Error: Failed to read "
            f"file '{file_name}'.[/red]"
        )