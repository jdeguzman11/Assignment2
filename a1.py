# a2.py

# Justin DeGuzman
# justicd1@uci.edu
# 72329664

from shlex import split
from command_processor import CommandProcessor

def main():
    processor = CommandProcessor()

    while True:
        try:
            raw_input = input().strip()
        except EOFError:
            break

        if raw_input == "Q":
            break
        
        try:
            parts = split(raw_input)
        except ValueError:
            print("ERROR")
            continue

        if len(parts) < 2:
            print("ERROR")
            continue

        command, path, *options = parts
        processor.handle(command, path, options)

if __name__ == "__main__":
    main()