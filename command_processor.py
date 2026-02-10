# command_processor.py

# Justin DeGuzman
# justicd1@uci.edu
# 72329664

from pathlib import Path
import sys

class CommandProcessor:

    # defining function that handles what command function to call
    def handle(self, command, path, options):
        if command == "L":
            self._list(path, options)
        elif command == "C":
            self._create(path, options)
        elif command == "D":
            self._delete(path)
        elif command == "R":
            self._read(path)
        else:
            print("ERROR")
    

    # defining function for L (list) command
    def _list(self, path, options):
        path = Path(path)

        if not path.exists() or not path.is_dir():
            print("ERROR")
            return
        
        try:
            items = list(path.iterdir())
        except Exception:
            print("ERROR")
            return
        
        files = sorted(p for p in items if p.is_file())
        dirs = sorted(p for p in items if p.is_dir())

        if "-s" in options:
            self._list_search(files, dirs, options)
            return
        
        if "-e" in options:
            self._list_extension(files, dirs, options)
            return

        for f in files:
            print(str(f))
        
        for d in dirs:
            if "-f" not in options:
                print(str(d))
            if "-r" in options:
                self._list(d, options)


    # defining function for -s option
    def _list_search(self, files, dirs, options):
        try:
            name = options[options.index("-s") + 1]
        except IndexError:
            print("ERROR")
            return
        
        for f in files:
            if f.name == name:
                print(str(f))

        if "-r" in options:
            for d in dirs:
                self._list(d, options)

    # defining function for -e option
    def _list_extension(self, files, dirs, options):
        try:
            ext = options[options.index("-e") + 1]
        except IndexError:
            print("ERROR")
            return
        
        for f in files:
            if f.suffix == f".{ext}":
                print(str(f))

        if "-r" in options:
            for d in dirs:
                self._list(d, options)


    # defining function for C (create) command
    def _create(self, path, options):
        if "-n" not in options:
            print("ERROR")
            return
        
        try:
            name = options[options.index("-n") + 1]
        except IndexError:
            print("ERROR")
            return
        
        directory = Path(path)

        if not directory.exists() or not directory.is_dir():
            print("ERROR")
            return
        
        if not name.endswith(".dsu"):
            name += ".dsu"

        full_path = directory / name

        if full_path.exists():
            print("ERROR")
            return
        
        try:
            full_path.touch()
            print(str(full_path.resolve()))
        except Exception:
            print("ERROR")

    # defining function for D (delete) command
    def _delete(self, path):
        path = Path(path)

        if not path.exists() or not path.is_file() or path.suffix != ".dsu":
            print("ERROR")
            return
        
        try:
            resolved = str(path.resolve())
            path.unlink()
            print(f"{resolved} DELETED")
        except Exception:
            print("ERROR")

    # defining function for R (read) command
    def _read(self, path):
        path = Path(path)

        if not path.exists() or not path.is_file() or path.suffix != ".dsu":
            print("ERROR")
            return
        
        if path.stat().st_size == 0:
            sys.stdout.write("EMPTY")
            return
        
        try:
            with open(path, "r") as f:
                sys.stdout.write(f.read())
        except Exception:
            print("ERROR")
