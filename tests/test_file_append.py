import os
import pytest
from src.file_append import append_to_file

def test_append_to_file(tmp_path):
    """Test appending text to an existing file."""
    # Create a temporary file
    test_file = tmp_path / "test_append.txt"
    test_file.write_text("Initial content\n")
    
    # Append text
    append_to_file(str(test_file), "Additional text\n")
    
    # Verify content
    with open(test_file, 'r') as f:
        content = f.read()
    assert content == "Initial content\nAdditional text\n"

def test_append_to_empty_file(tmp_path):
    """Test appending to an empty file."""
    test_file = tmp_path / "empty_file.txt"
    test_file.touch()  # Create an empty file
    
    append_to_file(str(test_file), "Some text\n")
    
    with open(test_file, 'r') as f:
        content = f.read()
    assert content == "Some text\n"

def test_append_multiple_times(tmp_path):
    """Test appending multiple times to the same file."""
    test_file = tmp_path / "multiple_append.txt"
    test_file.write_text("First line\n")
    
    append_to_file(str(test_file), "Second line\n")
    append_to_file(str(test_file), "Third line\n")
    
    with open(test_file, 'r') as f:
        content = f.read()
    assert content == "First line\nSecond line\nThird line\n"

def test_invalid_file_path():
    """Test error handling for invalid file path."""
    with pytest.raises(TypeError, match="file_path must be a string"):
        append_to_file(None, "test")
    
    with pytest.raises(ValueError, match="file_path cannot be an empty string"):
        append_to_file("", "test")
    
    with pytest.raises(ValueError, match="file_path cannot be an empty string"):
        append_to_file("   ", "test")

def test_invalid_text():
    """Test error handling for invalid text input."""
    with pytest.raises(TypeError, match="text must be a string"):
        append_to_file("test.txt", None)
    
    # Empty string is valid to append
    test_file = os.path.join(os.path.dirname(__file__), "test_empty.txt")
    open(test_file, 'w').close()  # Create empty file
    append_to_file(test_file, "")  # Should not raise an error
    os.unlink(test_file)  # Clean up