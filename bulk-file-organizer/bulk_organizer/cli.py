import argparse
import tomllib 
from pathlib import Path
from bulk_organizer.scanner import scanner
from bulk_organizer.mapper import map_extension_to_folder


def get_version():
    toml_path = Path(__file__).resolve().parent.parent / "pyproject.toml"
    with open(toml_path, "rb") as f:
        pyproject = tomllib.load(f)
    return pyproject["project"]["version"]


def main():
    parser = argparse.ArgumentParser()

    organized = {}

    parser.add_argument("--version", action="version", version=f"bulk-organizer {get_version()}")
    parser.add_argument("directory", type=str, help="Path to the directory to organize")
    parser.add_argument("--dry-run", action="store_true", help="Simulate the organization without making changes")
    parser.add_argument("--recursive", action="store_true", default=True, help="Recursively scan subdirectories")
    parser.add_argument("--summary", action="store_true", help="Show compact summary instead of full paths")


    args = parser.parse_args()
    directory_path = Path(args.directory)

    print(f"Organizing: {directory_path}")
    if args.dry_run:
        print("Dry run mode enabled")

    
    # Scan and print file paths
    try:
        for file_path in scanner(directory_path, recursive=args.recursive):
            folder = map_extension_to_folder(file_path)

            target_path = Path(args.directory) / folder / file_path.name

            if args.summary:
                organized.setdefault(folder, []).append(file_path)
            else:
                print(f"Move: {file_path} → {target_path}")

        if args.summary:
            print("\nDry run plan:")
            for folder, files in organized.items():
                print(f"\n📁 {folder} ({len(files)} files):")
                for f in files:
                    print(f"  - {f.name}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
