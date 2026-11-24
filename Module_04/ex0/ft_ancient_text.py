import sys


def opening_file(file_name: str) -> None:
    print(f"Accessing file '{file_name}'")
    try:
        f = open(file_name, "r", encoding="utf-8")

        print("---")
        print("")
        print(f"{f.read()}")
        print("---")
        print("")

        f.close()
        print(f"File '{file_name}' closed.")
    except Exception as e:
        print(f"Error opening file '{file_name}': {e}")
        f.close()


if __name__ == "__main__":
    argv: list[str] = sys.argv[1:]
    argc: int = len(argv)

    if (argc != 1):
        print("Usage: ft_ancient_text.py <file>")
    else:
        print("=== Cyber Archives Recovery ===")
        opening_file(argv[0])
