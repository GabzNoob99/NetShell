from rich.progress import track
from time import sleep

def exit_command(args):

    for tarefa in track(range(10), 'Encerrando...'):
        sleep(0.01)

    exit()