import pytest
from src.is_sorted import is_sorted

def test_sorted_ascending_integers():
    """Test ascending sorted list of integers"""
    assert is_sorted([1, 2, 3, 4, 5]) == True
    assert is_sorted([1, 1, 2, 3, 3]) == True

def test_sorted_descending_integers():
    """Test descending sorted list of integers"""
    assert is_sorted([5, 4, 3, 2, 1], ascending=False) == True
    assert is_sorted([5, 5, 4, 3, 3], ascending=False) == True

def test_unsorted_list():
    """Test unsorted lists return False"""
    assert is_sorted([3, 1, 4, 2, 5]) == False
    assert is_sorted([5, 4, 6, 3, 2], ascending=False) == False

def test_empty_list():
    """Test empty list is considered sorted"""
    assert is_sorted([]) == True
    assert is_sorted([], ascending=False) == True

def test_single_element_list():
    """Test single-element list is considered sorted"""
    assert is_sorted([42]) == True
    assert is_sorted([42], ascending=False) == True

def test_mixed_types_comparable():
    """Test sorting with comparable mixed types"""
    assert is_sorted([1, 1.5, 2, 2.5, 3]) == True
    assert is_sorted(['a', 'b', 'c']) == True
    assert is_sorted([5.5, 5, 4.3, 4, 3], ascending=False) == True

def test_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        is_sorted(None)
    with pytest.raises(TypeError):
        is_sorted("not a list")
    with pytest.raises(TypeError):
        is_sorted(123)

def test_list_with_non_comparable_types():
    """Test behavior with non-comparable types"""
    with pytest.raises(TypeError):
        is_sorted([1, 2, '3'])
    with pytest.raises(TypeError):
        is_sorted([1, 2, [3]], ascending=False)