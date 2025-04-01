import pytest
from src.string_reversal import reverse_string

def test_reverse_string_basic():
    """Test basic string reversal."""
    assert reverse_string("hello") == "olleh"
    assert reverse_string("python") == "nohtyp"

def test_reverse_string_empty():
    """Test reversing an empty string."""
    assert reverse_string("") == ""

def test_reverse_string_special_chars():
    """Test reversing strings with special characters."""
    assert reverse_string("a1b2c3") == "3c2b1a"
    assert reverse_string("!@#$%^") == "^%$#@!"

def test_reverse_string_single_char():
    """Test reversing a single character string."""
    assert reverse_string("a") == "a"

def test_reverse_string_whitespace():
    """Test reversing strings with whitespace."""
    assert reverse_string("  hello  ") == "  olleh  "

def test_reverse_string_invalid_input():
    """Test that TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(["list"])