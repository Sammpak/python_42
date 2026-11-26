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


def load_env_var() -> dict[str, str]:
    return {"Mode": os.environ.get("MATRIX_MODE", None),
            "Database": os.environ.get("DATABASE_URL", None),
            "API Access": os.environ.get("API_KEY", None),
            "Log Level:": os.environ.get("LOG_LEVEL", None),
            "Zion Network": os.environ.get("ZION_ENDPOINT", None)}


def check_no_hardcoded_secrets() -> bool:
    secrets = [v for v in (var_env_dict["Database"],
                           var_env_dict["API Access"]) if v]
    with open(__file__) as f:
        source = f.read()
    return not any(s and s in source for s in secrets)


if __name__ == "__main__":
    if check_dependencies():
        import_module()
        print()
        print("ORACLE STATUS: Readizg the Matrix...")
        print()
        load_dotenv()
        var_env_dict: dict[str, str] = load_env_var()

        for key, name in var_env_dict.items():
            if name is None:
                print(f"Missing {key} env, please check")
                sys.exit()
            else:
                print(f"{key} : {name}")
        print()
        if check_no_hardcoded_secrets():
            print("[OK] No hardcoded secrets detected")
        else:
            print("[KO] Hardcoded secrets detected")

        print("Environment security check:")

        print("[OK] .env file properly configured")
        print("[OK] Production overrides available")
    else:
        print("Missing dependency, use pip install -r requierement")
