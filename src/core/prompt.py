import os

def get_prompt():

    cwd = os.getcwd()

    prompt_name = os.path.basename(cwd) or cwd

    return f"{prompt_name} $"