import pytest
from pathlib import Path
from bulk_organizer.scanner import scanner

def test_scanner_non_recursive(tmp_path):
    # Setup: create files and folders
    (tmp_path / "file1.txt").write_text("hello")
    (tmp_path / "subdir").mkdir()
    (tmp_path / "subdir" / "file2.txt").write_text("world")

    # Act
    files = list(scanner(tmp_path, recursive=False))

    # Assert
    assert len(files) == 1
    assert files[0].name == "file1.txt"

def test_scanner_recursive(tmp_path):
    (tmp_path / "file1.txt").write_text("hello")
    (tmp_path / "subdir").mkdir()
    (tmp_path / "subdir" / "file2.txt").write_text("world")

    files = list(scanner(tmp_path, recursive=True))

    assert len(files) == 2
    assert sorted([f.name for f in files]) == ["file1.txt", "file2.txt"]
