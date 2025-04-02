import pytest
from src.max_subarray_sum import max_subarray_sum

def test_mixed_positive_negative():
    """Test array with mixed positive and negative numbers."""
    assert max_subarray_sum([1, -2, 3, 4, -1, 5]) == 11
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_all_positive():
    """Test array with all positive numbers."""
    assert max_subarray_sum([1, 2, 3, 4, 5]) == 15
    assert max_subarray_sum([5, 4, 3, 2, 1]) == 15

def test_all_negative():
    """Test array with all negative numbers."""
    assert max_subarray_sum([-1, -2, -3, -4]) == -1
    assert max_subarray_sum([-5, -2, -8, -1]) == -1

def test_single_element():
    """Test array with a single element."""
    assert max_subarray_sum([42]) == 42
    assert max_subarray_sum([-42]) == -42

def test_alternating_signs():
    """Test array with alternating positive and negative numbers."""
    assert max_subarray_sum([1, -1, 2, -2, 3, -3]) == 3

def test_invalid_input():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError):
        max_subarray_sum(None)
    
    with pytest.raises(TypeError):
        max_subarray_sum("not a list")
    
    with pytest.raises(TypeError):
        max_subarray_sum([1, 2, "3"])
    
    with pytest.raises(ValueError):
        max_subarray_sum([])