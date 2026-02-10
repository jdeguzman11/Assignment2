# Justin DeGuzman
# justicd1@uci.edu
# 72329664

from ui import UI


def main() -> None:
    ui = UI()

    print("Weclome!")
    print("Type 'admin' to enter admin mode, or press enter to continue.")

    try:
        first = input("> ").strip()
    except EOFError:
        return

    if first == "admin":
        ui.run_admin()
    else:
        ui.run_friendly(first)


if __name__ == "__main__":
    main()
