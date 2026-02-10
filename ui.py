# ui.py

# Justin DeGuzman
# justicd1@uci.edu
# 72329664

from shlex import split
from command_processor import CommandProcessor

def _process_line(line: str, processor: CommandProcessor) -> bool:
    line = line.strip()

    if line == "Q":
        return False
    
    if line == "":
        print("ERROR")
        return True
    
    try:
        parts = split(line)
    except ValueError:
        print("ERROR")
        return True
    
    cmd = parts[0].upper()
    
    path_commands = {"L", "C", "D", "R", "O"}
    no_path_commands = {"E", "P"}

    if cmd in path_commands:
        if len(parts) < 2:
            print("ERROR")
            return True
        
        path = parts[1]
        options = parts[2:]
        processor.handle(cmd, path, options)
        return True
    
    if cmd in no_path_commands:
        print("ERROR")
        return True

# friendly mode
def run_friendly(first_choice: str = "") -> None:
    processor = CommandProcessor()

    if first_choice.strip() != "":
        if not _process_line(first_choice, processor):
            return
        
    while True:
        try:
            line = input("> ")
        except EOFError:
            break

        if not _process_line(line, processor):
            break

# admin mode
def run_admin() -> None:
    processor = CommandProcessor()

    while True:
        try:
            line = input()
        except EOFError:
            break

        if not _process_line(line, processor):
            break
