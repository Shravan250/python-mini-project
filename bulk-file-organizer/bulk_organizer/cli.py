import argparse
import tomllib 
from pathlib import Path

def get_version():
    toml_path = Path(__file__).resolve().parent.parent / "pyproject.toml"
    with open(toml_path, "rb") as f:
        pyproject = tomllib.load(f)
    return pyproject["project"]["version"]


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--version", action="version", version=f"bulk-organizer {get_version()}")
    parser.add_argument("directory", type=str, help="Path to the directory to organize")
    parser.add_argument("--dry-run", action="store_true", help="Simulate the organization without making changes")
    args = parser.parse_args()

    print(f"Organizing: {args.directory}")
    if args.dry_run:
        print("Dry run mode enabled")

if __name__ == "__main__":
    main()
