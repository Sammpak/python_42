import sys
from typing import TextIO


def show_file(f: TextIO) -> None:
    print("---")
    print()
    print(f"{f.read()}")
    print("---")
    print()


def open_and_modify_file(new_loc: str, file_name: str) -> None:
    with open(file_name, 'r') as f_in:
        lines = f_in.readlines()

    with open(new_loc, 'w') as f_out:
        for line in lines:
            if line[-1] == "\n":
                line = line[:-1] + "#\n"
            else:
                line = line + "#\n"
            f_out.write(line)


def modify_file(file_name: str) -> None:
    print("Transform data:")
    try:
        with open(f"{file_name}", 'r') as f_in:
            for line in f_in:
                if line[-1] == "\n":
                    line = line[:-1]
                print(f"{line}#")

        new_loc: str = input("Enter new file name (or empty): ")
        if new_loc == "":
            print("Not saving data")
        else:
            open_and_modify_file(new_loc, file_name)
    except Exception as e:
        print(f"Error modify file '{file_name}': {e}")


def opening_file(file_name: str) -> None:
    print(f"Accessing file '{file_name}'")
    try:
        with open(file_name, "r") as f:
            show_file(f)
            print(f"File '{file_name}' closed.")
        print("")
    except Exception as e:
        print(f"Error opening file '{file_name}': {e}")


if __name__ == "__main__":
    argv: list[str] = sys.argv[1:]
    argc: int = len(argv)

    if (argc != 1):
        print("Usage: ft_ancient_text.py <file>")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        opening_file(argv[0])
        modify_file(argv[0])
