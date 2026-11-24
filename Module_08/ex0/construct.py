import sys
from pathlib import Path


def in_venv():
    return sys.prefix != sys.base_prefix


if __name__ == "__main__":
    is_in_venv: bool = in_venv()
    if (is_in_venv):
        print("MATRIX STATUS: Welcome to the construct")
        venv_path = Path(sys.prefix)
        venv_name = venv_path.name
    else:
        print("MATRIX STATUS: You're still plugged in")
    print(f"Current Python: {sys.version}")
    if (is_in_venv):
        print(f"Virtual environment {venv_path}")
        print(f"Virtual environment {venv_name}")

    else:
        print(" ")
        print("Virtual Environment: None detected")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print(" ")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print(r"matrix_env\Scripts\activate  # On Windows")
        print(" ")
        print("Then run this program again.")
