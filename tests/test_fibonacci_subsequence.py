import pytest
from src.fibonacci_subsequence import fibonacci_subsequence

def test_fibonacci_subsequence_zero_length():
    """Test generating Fibonacci subsequence of length 0."""
    assert fibonacci_subsequence(0) == []

def test_fibonacci_subsequence_length_one():
    """Test generating Fibonacci subsequence of length 1."""
    assert fibonacci_subsequence(1) == [0]

def test_fibonacci_subsequence_length_two():
    """Test generating Fibonacci subsequence of length 2."""
    assert fibonacci_subsequence(2) == [0, 1]

def test_fibonacci_subsequence_length_five():
    """Test generating Fibonacci subsequence of length 5."""
    assert fibonacci_subsequence(5) == [0, 1, 1, 2, 3]

def test_fibonacci_subsequence_length_ten():
    """Test generating Fibonacci subsequence of length 10."""
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert fibonacci_subsequence(10) == expected

def test_fibonacci_subsequence_invalid_input_negative():
    """Test that a negative input raises a ValueError."""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        fibonacci_subsequence(-1)

def test_fibonacci_subsequence_invalid_input_type():
    """Test that a non-integer input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_subsequence("5")
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_subsequence(5.5)
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_subsequence(None)