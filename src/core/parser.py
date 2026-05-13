def parse_command(command_line):

    r = command_line.split()

    if not r:
        return None, []

    cmd = r[0]

    args = r[1:]

    return cmd, args