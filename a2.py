# a2.py

# Justin DeGuzman
# justicd1@uci.edu
# 72329664

from pathlib import Path
from shlex import split

def contents(path, options):
    path = Path(path)
    
    try:
        items = list(path.iterdir())
    except Exception:
        print("ERROR")
        return
    
    files = sorted([p for p in items if p.is_file()])
    dirs = sorted([p for p in items if p.is_dir()])

    if "-s" in options:
        search = options[-1]
        for f in files:
            if f.name == search:
                print(f)
        if "-r" in options:
            for d in dirs:
                contents(d, options)
        return
    
    if "-e" in options:
        extension = options[-1]
        for f in files:
            if f.suffix == "." + extension:
                print(f)
        if "-r" in options:
            for d in dirs:
                contents(d, options)
        return
    
    for f in files:
        print(f)

    for d in dirs:
        if "-f" not in options:
            print(d)
        if "-r" in options:
            contents(d, options)
    

def create_file(path, options):
    try:
        if "-n" not in options:
            print("ERROR")
            return

        name_index = options.index("-n") + 1
        if name_index >= len(options):
            print("ERROR")
            return
        
        file_name = options[name_index]
        if not file_name.endswith(".dsu"):
            file_name += ".dsu"
        
        directory = Path(path)
        if not directory.exists() or not directory.is_dir():
            print("ERROR")
            return
        
        full_path = directory / file_name
        full_path.touch(exist_ok=False)
        print(full_path.resolve())
    
    except Exception:
        print("ERROR")
    

def delete_file(path):
    try: 
        path = Path(path)

        if not path.exists():
            print("ERROR")
            return
        
        if not path.is_file():
            print("ERROR")
            return

        if path.suffix != ".dsu":
            print("ERROR")
            return
        
        resolved = path.resolve()
        path.unlink()
        print(f"{resolved} DELETED")

    except Exception:
        print("ERROR")
        

def read_file(path):
    try:
        path = Path(path)

        if not path.exists():
            print("ERROR")
            return
        
        if not path.is_file():
            print("ERROR")
            return
        
        if path.suffix != ".dsu":
            print("ERROR")
            return
        
        if path.stat().st_size == 0:
            print("EMPTY")
            return
        
        with open(path, "r") as file:
                print(file.read(), end="")
    
    except Exception:
        print("ERROR")


def main():
    while True:
        user_inputs = input().strip()
        
        if user_inputs == "Q":
            break
        
        try:
            parts = split(user_inputs)
        except ValueError:
            print("ERROR")
            continue
        
        if len(parts) < 2:
            print("ERROR")
            continue

        user_command = parts[0]
        user_path = parts[1]
        user_options = parts[2:]

        if user_command == "L":
            contents(user_path, user_options)
        
        elif user_command == "C":
            create_file(user_path, user_options)

        elif user_command == "D":
            delete_file(user_path)
        
        elif user_command == "R":
            read_file(user_path)
    
        else:
            print("ERROR")
            
        
if __name__ == "__main__":
    main()
    