import pytest
from src.array_rotation import rotate_array_left

def test_basic_rotation():
    """Test basic left rotation of an array"""
    assert rotate_array_left([1, 2, 3, 4, 5], 2) == [3, 4, 5, 1, 2]

def test_rotation_full_length():
    """Test rotation by full array length should return original array"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_array_left(arr, 5) == arr

def test_rotation_larger_than_length():
    """Test rotation amount larger than array length"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_array_left(arr, 7) == [3, 4, 5, 1, 2]

def test_empty_array():
    """Test rotation of an empty array"""
    assert rotate_array_left([], 3) == []

def test_single_element_array():
    """Test rotation of a single-element array"""
    assert rotate_array_left([42], 1) == [42]

def test_zero_rotation():
    """Test rotation of 0 positions"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_array_left(arr, 0) == arr

def test_invalid_input_type():
    """Test invalid input types raise TypeError"""
    with pytest.raises(TypeError, match="Input must be a list"):
        rotate_array_left("not a list", 2)
    
    with pytest.raises(TypeError, match="Rotation amount must be an integer"):
        rotate_array_left([1, 2, 3], "2")

def test_negative_rotation():
    """Test negative rotation amount raises ValueError"""
    with pytest.raises(ValueError, match="Rotation amount cannot be negative"):
        rotate_array_left([1, 2, 3], -1)