# a2.py

# Justin DeGuzman
# justicd1@uci.edu
# 72329664

from ui import run_admin, run_friendly

def main() -> None:
    print("Weclome!")
    print("Type 'admin' to enter admin mode, or press enter to continue.")

    try:
        first = input("> ").strip()
    except EOFError:
        return
    
    if first == "admin":
        run_admin()
    else:
        run_friendly(first)

if __name__ == "__main__":
    main()