import os
from rich import print

def ls_command(args):

    for item in os.listdir():
        print(item)