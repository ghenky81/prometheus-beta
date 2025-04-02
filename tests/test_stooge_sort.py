import pytest
from src.stooge_sort import stooge_sort

def test_stooge_sort_basic():
    """Test basic sorting functionality"""
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert stooge_sort(arr) == sorted(arr)

def test_stooge_sort_already_sorted():
    """Test sorting an already sorted list"""
    arr = [1, 2, 3, 4, 5]
    assert stooge_sort(arr) == sorted(arr)

def test_stooge_sort_reverse_sorted():
    """Test sorting a reverse-sorted list"""
    arr = [5, 4, 3, 2, 1]
    assert stooge_sort(arr) == sorted(arr)

def test_stooge_sort_duplicate_elements():
    """Test sorting with duplicate elements"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert stooge_sort(arr) == sorted(arr)

def test_stooge_sort_empty_list():
    """Test sorting an empty list"""
    arr = []
    assert stooge_sort(arr) == []

def test_stooge_sort_single_element():
    """Test sorting a single-element list"""
    arr = [42]
    assert stooge_sort(arr) == [42]

def test_stooge_sort_negative_numbers():
    """Test sorting with negative numbers"""
    arr = [-5, 3, -2, 0, 1, -9]
    assert stooge_sort(arr) == sorted(arr)

def test_stooge_sort_invalid_input():
    """Test error handling for invalid input"""
    with pytest.raises(TypeError):
        stooge_sort("not a list")
    with pytest.raises(TypeError):
        stooge_sort(123)

def test_stooge_sort_original_list_modified():
    """Ensure the original list is modified in-place"""
    arr = [3, 1, 4, 1, 5, 9]
    original = arr.copy()
    stooge_sort(arr)
    assert arr == sorted(original)