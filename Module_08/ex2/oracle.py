from __future__ import annotations

import os
import sys
from importlib.metadata import PackageNotFoundError, metadata, version
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dotenv import load_dotenv


def import_module() -> None:
    global load_dotenv
    from dotenv import load_dotenv


def check_dependencies() -> bool:
    dependencies: dict[str, str] = {"python-dotenv": ".env key value pair"}
    for pkg, desc in dependencies.items():
        try:
            meta = metadata(pkg)
            pkg_name = meta["Name"]
            pkg_version = version(pkg)
            print(f"[OK] {pkg_name} {pkg_version} - {desc}")
        except PackageNotFoundError as e:
            print(f"[ERROR] missing: {e}")
            return False
    return True


def load_env() -> dict[str, str]:
    return {"Mode": os.getenv("MATRIX_MODE"),
            "Database": os.getenv("DATABASE_URL"),
            "API Access": os.getenv("API_KEY"),
            "Log Level:": os.getenv("LOG_LEVEL"),
            "Zion Network": os.getenv("ZION_ENDPOINT")}


if __name__ == "__main__":
    if check_dependencies():

        import_module()
        print()
        print("ORACLE STATUS: Readizg the Matrix...")
        print()
        load_dotenv()
        env_dict: dict[str, str] = load_env()

        for key, name in env_dict.items():
            if name is None:
                print(f"Missing {key} env, please check")
                sys.exit()
            else:
                print(f"{key} : {name}")
    else:
        print("Missing dependency")
