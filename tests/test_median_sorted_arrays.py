import pytest
from src.median_sorted_arrays import find_median_sorted_arrays

def test_even_length_arrays():
    """Test median for arrays with even total length"""
    assert find_median_sorted_arrays([1,3], [2]) == 2.0
    assert find_median_sorted_arrays([1,2], [3,4]) == 2.5

def test_odd_length_arrays():
    """Test median for arrays with odd total length"""
    assert find_median_sorted_arrays([1,3], [2,4]) == 2.5
    assert find_median_sorted_arrays([0,0], [0,0]) == 0.0

def test_one_empty_array():
    """Test median when one array is empty"""
    assert find_median_sorted_arrays([], [1,2,3,4,5]) == 3.0
    assert find_median_sorted_arrays([1,2,3,4,5], []) == 3.0

def test_different_length_arrays():
    """Test median for arrays of different lengths"""
    assert find_median_sorted_arrays([1,3,5], [2,4,6]) == 3.5

def test_single_element_arrays():
    """Test median for single element arrays"""
    assert find_median_sorted_arrays([1], [2]) == 1.5
    assert find_median_sorted_arrays([2], [1]) == 1.5

def test_large_arrays():
    """Test median for larger arrays"""
    arr1 = list(range(0, 100, 2))
    arr2 = list(range(1, 100, 2))
    assert find_median_sorted_arrays(arr1, arr2) == 49.5

def test_type_errors():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        find_median_sorted_arrays("not a list", [1,2,3])
    with pytest.raises(TypeError):
        find_median_sorted_arrays([1,2,3], "not a list")

def test_value_errors():
    """Test error handling for invalid input values"""
    with pytest.raises(ValueError):
        find_median_sorted_arrays([1,2,'a'], [3,4,5])
    with pytest.raises(ValueError):
        find_median_sorted_arrays([1,2,3], [4,5,'b'])

def test_float_support():
    """Test support for floating point numbers"""
    assert find_median_sorted_arrays([1.5, 2.5], [3.5, 4.5]) == 3.0