import os
from rich import print

def pwd_command(args):

    print(os.getcwd())