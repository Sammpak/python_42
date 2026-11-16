

def secure_archive(file_name: str, action: int = 0,
                   to_write: str = "") -> tuple[bool, str]:
    try:
        file: str = ""
        if (action == 0):
            with open(file_name, "r") as f:
                for line in f:
                    file = file + line
            return (True, file)
        elif (action == 1):
            with open(file_name, "w", encoding="utf-8") as f:
                f.write(to_write)
                return (True, "Content successfully written to file")
    except FileNotFoundError as e:
        return (False, f"[Errno 2] {e}")
    except PermissionError as e:
        return (False, f"Errno 13]  {e}")
    return (False, "somethings went wrong")


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")
    print("")

    print("Using 'secure_archive' to read from a nonexistent file:")
    result: tuple[bool, str] = secure_archive("my_Noexistance", 0)
    print(f"{result}")

    print("")

    print("Using 'secure_archive' to read from an inaccessible file:")
    result = secure_archive("no_perm.txt")
    print(f"{result}")

    print("")

    print("Using 'secure_archive' to read from a regular file:")
    result = secure_archive("test.txt")
    print(f"{result}")

    print("")

    print("Using 'secure_archive' to write previous content to a new file:")
    if result[0]:
        to_write: str = result[1]
        result = secure_archive("new_test.txt", 1, to_write)
        print(f"{result}")
