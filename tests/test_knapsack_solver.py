import pytest
from src.knapsack_solver import solve_knapsack

def test_basic_knapsack():
    """Test a basic knapsack scenario"""
    items = [(2, 3), (3, 4), (4, 5), (5, 6)]
    capacity = 10
    assert solve_knapsack(items, capacity) == 13

def test_empty_items():
    """Test with an empty list of items"""
    assert solve_knapsack([], 10) == 0

def test_zero_capacity():
    """Test when knapsack capacity is zero"""
    items = [(2, 3), (3, 4)]
    assert solve_knapsack(items, 0) == 0

def test_small_capacity():
    """Test when capacity is very small"""
    items = [(5, 10), (4, 8), (3, 6)]
    assert solve_knapsack(items, 1) == 0

def test_exact_capacity():
    """Test when items exactly match the capacity"""
    items = [(2, 3), (3, 4), (4, 5)]
    capacity = 9
    assert solve_knapsack(items, capacity) == 12

def test_float_inputs():
    """Test with float inputs for weights and capacity"""
    items = [(2.5, 3), (3.2, 4), (4.1, 5)]
    capacity = 10.5
    assert solve_knapsack(items, capacity) == 12

def test_invalid_negative_capacity():
    """Test raising error for negative capacity"""
    with pytest.raises(ValueError, match="Capacity must be a non-negative number"):
        solve_knapsack([(1, 2)], -5)

def test_invalid_negative_weight():
    """Test raising error for negative item weight"""
    with pytest.raises(ValueError, match="Item weights must be non-negative numbers"):
        solve_knapsack([(-1, 2)], 10)

def test_invalid_negative_value():
    """Test raising error for negative item value"""
    with pytest.raises(ValueError, match="Item values must be non-negative numbers"):
        solve_knapsack([(1, -2)], 10)

def test_invalid_items_format():
    """Test raising error for invalid items format"""
    with pytest.raises(ValueError, match="Items must be a list of \\(weight, value\\) tuples"):
        solve_knapsack([1, 2, 3], 10)

def test_complex_scenario():
    """Test a more complex knapsack scenario"""
    items = [(10, 60), (20, 100), (30, 120)]
    capacity = 50
    assert solve_knapsack(items, capacity) == 220