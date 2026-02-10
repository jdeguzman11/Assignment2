# command_processor

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

        if not path.exists() or not path.isdir():
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
            self._list_extenstion(files, dirs, options)
            return

        for f in files:
            print(f)
        
        for d in dirs:
            if "-f" not in options:
                print(d)
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
                print(f)

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
                print(f)

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

        if not directory.exists() or not directory.isdir():
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
            print(full_path.resolve())
        except Exception:
            print("ERROR")

    # defining function for D (delete) command
    def _delete(self, path):
        path = Path(path)

        if not path.exists() or not path.is_file() or path.suffix != ".dsu":
            print("ERROR")
            return
        
        try:
            resolved = path.resolve()
            path.unlink()
            print(f"{resolved} DELETED")
        except Exception:
            print("ERROR")

    