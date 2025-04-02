import pytest
from src.alternating_dot_case import convert_to_alternating_dot_case

def test_convert_to_alternating_dot_case_basic():
    """Test basic string conversion."""
    assert convert_to_alternating_dot_case("hello") == 'h.E.l.L.o'
    assert convert_to_alternating_dot_case("Python") == 'p.Y.t.H.o.N'
    assert convert_to_alternating_dot_case("OpenAI") == 'o.P.e.N.a.I'

def test_convert_to_alternating_dot_case_single_char():
    """Test conversion of a single character."""
    assert convert_to_alternating_dot_case("a") == 'a'
    assert convert_to_alternating_dot_case("Z") == 'z'

def test_convert_to_alternating_dot_case_error_handling():
    """Test error handling for invalid inputs."""
    # Test non-string input
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_alternating_dot_case(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_alternating_dot_case(None)
    
    # Test empty string
    with pytest.raises(ValueError, match="Input string cannot be empty"):
        convert_to_alternating_dot_case("")

def test_convert_to_alternating_dot_case_with_spaces_and_symbols():
    """Test conversion with spaces and symbols."""
    assert convert_to_alternating_dot_case("hello world") == 'h.E.l.L.o. .W.o.R.l.D'
    assert convert_to_alternating_dot_case("hello!") == 'h.E.l.L.o.!'