import pytest
from src.palindrome_mirror import create_palindrome_mirror

def test_basic_string():
    """Test basic string palindrome mirror creation."""
    assert create_palindrome_mirror("hello") == "helloolleh"

def test_empty_string():
    """Test empty string creates empty palindrome mirror."""
    assert create_palindrome_mirror("") == ""

def test_single_character():
    """Test single character string."""
    assert create_palindrome_mirror("a") == "aa"

def test_string_with_spaces():
    """Test string with spaces."""
    assert create_palindrome_mirror("hi there") == "hi thereereht ih"

def test_string_with_numbers():
    """Test string with numbers."""
    assert create_palindrome_mirror("123") == "123321"

def test_string_with_special_characters():
    """Test string with special characters."""
    assert create_palindrome_mirror("a!b@c#") == "a!b@c#c@b!a"

def test_invalid_input():
    """Test that non-string input raises TypeError."""
    with pytest.raises(TypeError, match="Input must be a string"):
        create_palindrome_mirror(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        create_palindrome_mirror(None)

def test_mixed_characters():
    """Test string with mixed characters."""
    assert create_palindrome_mirror("Test 123!") == "Test 123!!321 tseT"