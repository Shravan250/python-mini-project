import argparse
import tomllib 
from pathlib import Path
from bulk_organizer.scanner import scanner


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
    parser.add_argument("--recursive", action="store_true", default=True, help="Recursively scan subdirectories")

    args = parser.parse_args()
    directory_path = Path(args.directory)

    print(f"Organizing: {directory_path}")
    if args.dry_run:
        print("Dry run mode enabled")

    
    # Scan and print file paths
    try:
        for file_path in scanner(directory_path, recursive=args.recursive):
            print(file_path)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
