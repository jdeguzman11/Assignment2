# ui.py

# Justin DeGuzman
# justicd1@uci.edu
# 72329664

from shlex import split
from command_processor import CommandProcessor

def run() -> None:
    processor = CommandProcessor()

    while True:
        try:
            line = input().strip()
        except EOFError:
            break

        if line == "Q":
            break
        
        try:
            parts = split(line)
        except ValueError:
            print("ERROR")
            continue

        if len(parts) < 2:
            print("ERROR")
            continue

        command, path, *options = parts
        command = command.upper()
        
        processor.handle(command, path, options)