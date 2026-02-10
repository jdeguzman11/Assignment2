# ui.py

# Justin DeGuzman
# justicd1@uci.edu
# 72329664

from shlex import split
from typing import Optional
from command_processor import CommandProcessor
from Profile import Profile, DsuFileError, DsuProfileError

class UI:
    def __init__(self) -> None:
        self.processor = CommandProcessor()

        self.current_path: Optional[str] = None
        self.current_profile: Optional[Profile] = None

    def _open_dsu(self, path: str) -> None:
        prof = Profile()
        
        try:
            prof.load_profile(path)
        except (DsuFileError, DsuProfileError):
            print("ERROR")
            return
        
        self.current_profile = prof
        self.current_path = path
        print(f"LOADED {path}")

    def _process_line(self, line: str) -> bool:
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

            if cmd == "O":
                self._open_dsu(path)
                return True

            self.processor.handle(cmd, path, options)
            return True
    
        if cmd in no_path_commands:
            if self.current_profile is None or self.current_path is None: 
                print("ERROR")
                return True
        
            print("ERROR")
            return True
        
        print("ERROR")
        return True

    # friendly mode
    def run_friendly(self, first_choice: str = "") -> None:
        if first_choice.strip() != "":
            if not self._process_line(first_choice):
                return
        
        while True:
            try:
                line = input("> ")
            except EOFError:
                break

            if not self._process_line(line):
                break

    # admin mode
    def run_admin(self) -> None:
        while True:
            try:
                line = input()
            except EOFError:
                break

            if not self._process_line(line):
                break
