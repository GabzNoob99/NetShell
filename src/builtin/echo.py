from rich import print

def echo_command(args):

    if not args:

        message = input('>')

        print(message)

    elif args[0] == '-n':

        if len(args) == 1:
            message = input('>')

        else:
            message = ' '.join(args[1:])

        print(message, end='')

    elif args[0] == '-a':

        if len(args) < 2:
            file_name = input('>').strip()

        else:
            file_name = args[1]

        if len(args) < 3:
            message = input('>')

        else:
            message = ' '.join(args[2:])

        if not file_name:

            print(
                "[red]echo -a requires file name.[/red]"
            )

            return

        try:

            with open(file_name, 'a') as f:
                f.write(message + '\n')

            print(
                f"[green]Info: Content written "
                f"to '{file_name}' successfully![/green]"
            )

        except FileNotFoundError:

            print(
                f"[red]Error: File "
                f"'{file_name}' not found.[/red]"
            )

        except Exception:

            print(
                f"[red]Error: Failed to write "
                f"to file '{file_name}'.[/red]"
            )

    else:

        message = ' '.join(args)

        print(message)