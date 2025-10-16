import pytest
from pathlib import Path
from bulk_organizer.scanner import scanner
from bulk_organizer.mapper import map_extension_to_folder, DEFAULT_MAP

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


def test_known_extension():
    assert map_extension_to_folder(Path("photo.JPG"), DEFAULT_MAP) == "Images"
    assert map_extension_to_folder(Path("song.wav"), DEFAULT_MAP) == "Audio"

def test_unknown_extension():
    assert map_extension_to_folder(Path("weird.xyz"), DEFAULT_MAP) == "Others"

