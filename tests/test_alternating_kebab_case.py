import pytest
from src.alternating_kebab_case import to_alternating_kebab_case

def test_basic_conversion():
    """Test basic string conversion."""
    assert to_alternating_kebab_case("hello world") == "hello-WORLD"
    assert to_alternating_kebab_case("python is awesome") == "python-IS-awesome"

def test_single_word():
    """Test conversion with a single word."""
    assert to_alternating_kebab_case("hello") == "hello"
    assert to_alternating_kebab_case("HELLO") == "hello"

def test_empty_string():
    """Test conversion of an empty string."""
    assert to_alternating_kebab_case("") == ""

def test_multiple_words():
    """Test conversion with multiple words."""
    assert to_alternating_kebab_case("one two three four") == "one-TWO-three-FOUR"

def test_mixed_case_input():
    """Test conversion with mixed case input."""
    assert to_alternating_kebab_case("HeLLo WoRLd") == "hello-WORLD"

def test_invalid_input():
    """Test that invalid input raises TypeError."""
    with pytest.raises(TypeError):
        to_alternating_kebab_case(123)
    with pytest.raises(TypeError):
        to_alternating_kebab_case(None)

def test_whitespace_handling():
    """Test handling of multiple whitespaces."""
    assert to_alternating_kebab_case("  hello   world  ") == "hello-WORLD"