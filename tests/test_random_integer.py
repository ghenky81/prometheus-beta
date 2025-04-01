import pytest
import random

from src.random_integer import generate_random_integer

def test_generate_random_integer_basic_range():
    """Test generating a random integer within a basic range."""
    min_val, max_val = 1, 10
    result = generate_random_integer(min_val, max_val)
    
    # Check that the result is within the specified range (inclusive)
    assert min_val <= result <= max_val, f"Result {result} not in range [{min_val}, {max_val}]"

def test_generate_random_integer_same_min_max():
    """Test generating a random integer when min and max are the same."""
    result = generate_random_integer(5, 5)
    assert result == 5, "Should return the same number when min and max are equal"

def test_generate_random_integer_negative_range():
    """Test generating a random integer in a negative range."""
    min_val, max_val = -10, -1
    result = generate_random_integer(min_val, max_val)
    
    # Check that the result is within the specified range (inclusive)
    assert min_val <= result <= max_val, f"Result {result} not in range [{min_val}, {max_val}]"

def test_generate_random_integer_mixed_range():
    """Test generating a random integer in a mixed range including zero."""
    min_val, max_val = -5, 5
    result = generate_random_integer(min_val, max_val)
    
    # Check that the result is within the specified range (inclusive)
    assert min_val <= result <= max_val, f"Result {result} not in range [{min_val}, {max_val}]"

def test_generate_random_integer_invalid_range():
    """Test that an error is raised when min_value > max_value."""
    with pytest.raises(ValueError, match="min_value must be less than or equal to max_value"):
        generate_random_integer(10, 5)

def test_generate_random_integer_invalid_type():
    """Test that an error is raised when input types are invalid."""
    with pytest.raises(TypeError, match="Both min_value and max_value must be integers"):
        generate_random_integer(1.5, 10)
    
    with pytest.raises(TypeError, match="Both min_value and max_value must be integers"):
        generate_random_integer("1", 10)

def test_generate_random_integer_distribution():
    """Test that the function generates a reasonably uniform distribution."""
    min_val, max_val = 1, 100
    num_trials = 10000
    results = [generate_random_integer(min_val, max_val) for _ in range(num_trials)]
    
    # Check that each expected value appears with approximately equal frequency
    unique_results = set(results)
    for val in unique_results:
        # Check that the count of each number is within expected range
        count = results.count(val)
        lower_bound = num_trials / (max_val - min_val + 1) * 0.5
        upper_bound = num_trials / (max_val - min_val + 1) * 1.5
        
        assert lower_bound < count < upper_bound, f"Potential distribution bias for {val}"