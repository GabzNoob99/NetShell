from rich import print

def help_command(args):

    print(
        "[green]Comandos disponíveis:[/green]\n"
        "[blue]help[/blue] - Exibe ajuda.\n"
        "[blue]cls[/blue] - Limpa a tela.\n"
        "[blue]exit[/blue] - Encerra a shell.\n"
        "[blue]pwd[/blue] - Diretório atual.\n"
        "[blue]ls[/blue] - Lista arquivos.\n"
        "[blue]cd[/blue] - Navega diretórios.\n"
        "[blue]mkdir[/blue] - Cria diretório.\n"
        "[blue]touch[/blue] - Cria arquivo.\n"
        "[blue]cat[/blue] - Lê arquivo.\n"
        "[blue]rnm[/blue] - Renomeia.\n"
        "[blue]echo[/blue] - Exibe mensagem."
    )