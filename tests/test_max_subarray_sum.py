import pytest
from src.max_subarray_sum import max_subarray_sum

def test_max_subarray_sum_normal_case():
    """Test normal case with a typical input."""
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4
    assert max_subarray_sum(arr, k) == [10, 23, 3, 1]

def test_max_subarray_sum_all_elements():
    """Test when k is equal to the length of the array."""
    arr = [2, 3, 4, 1, 5]
    k = 5
    assert max_subarray_sum(arr, k) == [2, 3, 4, 1, 5]

def test_max_subarray_sum_k_larger_than_array():
    """Test when k is larger than the array length."""
    arr = [1, 2, 3]
    k = 5
    assert max_subarray_sum(arr, k) == []

def test_max_subarray_sum_k_zero():
    """Test when k is zero."""
    arr = [1, 2, 3, 4, 5]
    k = 0
    assert max_subarray_sum(arr, k) == []

def test_max_subarray_sum_k_negative():
    """Test when k is negative."""
    arr = [1, 2, 3, 4, 5]
    k = -1
    assert max_subarray_sum(arr, k) == []

def test_max_subarray_sum_empty_array():
    """Test with an empty array."""
    arr = []
    k = 3
    assert max_subarray_sum(arr, k) == []

def test_max_subarray_sum_multiple_max_subarrays():
    """Test case with multiple subarrays having the same maximum sum."""
    arr = [1, 1, 1, 2, 2, 2, 1, 1, 1]
    k = 3
    assert max_subarray_sum(arr, k) == [2, 2, 2]