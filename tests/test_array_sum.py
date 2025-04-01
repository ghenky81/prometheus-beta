import pytest
from src.array_sum import calculate_array_sum

def test_calculate_array_sum_positive_integers():
    """Test sum of positive integers"""
    assert calculate_array_sum([1, 2, 3, 4, 5]) == 15

def test_calculate_array_sum_negative_integers():
    """Test sum of negative integers"""
    assert calculate_array_sum([-1, -2, -3, -4, -5]) == -15

def test_calculate_array_sum_mixed_numbers():
    """Test sum of mixed positive and negative numbers"""
    assert calculate_array_sum([-1, 2, -3, 4, -5]) == -3

def test_calculate_array_sum_floating_point():
    """Test sum of floating point numbers"""
    assert calculate_array_sum([1.5, 2.5, 3.0]) == 7.0

def test_calculate_array_sum_empty_list():
    """Test sum of an empty list"""
    assert calculate_array_sum([]) == 0

def test_calculate_array_sum_invalid_input_not_list():
    """Test that a non-list input raises TypeError"""
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_array_sum("not a list")

def test_calculate_array_sum_invalid_input_non_numeric():
    """Test that a list with non-numeric elements raises TypeError"""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        calculate_array_sum([1, 2, "3", 4])