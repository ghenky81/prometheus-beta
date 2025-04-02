import pytest
from src.text_character_counter import count_vowels_and_consonants

def test_basic_text_counting():
    """Test counting vowels and consonants in a simple string."""
    result = count_vowels_and_consonants("hello world")
    assert result == {'vowels': 3, 'consonants': 7}

def test_mixed_case_text():
    """Test that counting works with mixed case text."""
    result = count_vowels_and_consonants("HeLLo WoRLd")
    assert result == {'vowels': 3, 'consonants': 7}

def test_text_with_numbers_and_symbols():
    """Test that only alphabetic characters are counted."""
    result = count_vowels_and_consonants("hello123 world!")
    assert result == {'vowels': 3, 'consonants': 7}

def test_empty_string():
    """Test counting in an empty string."""
    result = count_vowels_and_consonants("")
    assert result == {'vowels': 0, 'consonants': 0}

def test_only_vowels():
    """Test a string with only vowels."""
    result = count_vowels_and_consonants("aeiou")
    assert result == {'vowels': 5, 'consonants': 0}

def test_only_consonants():
    """Test a string with only consonants."""
    result = count_vowels_and_consonants("bcdfg")
    assert result == {'vowels': 0, 'consonants': 5}

def test_invalid_input_type():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        count_vowels_and_consonants(123)

def test_unicode_text():
    """Test handling of text with unicode characters."""
    result = count_vowels_and_consonants("hèllö wörld")
    assert result == {'vowels': 0, 'consonants': 7}, "Function should strip non-ASCII characters"