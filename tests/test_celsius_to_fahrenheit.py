import pytest
import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.celsius_to_fahrenheit import celsius_to_fahrenheit

def test_positive_celsius():
    """Test conversion of positive Celsius temperatures."""
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(37) == 98.6

def test_negative_celsius():
    """Test conversion of negative Celsius temperatures."""
    assert celsius_to_fahrenheit(-40) == -40
    assert celsius_to_fahrenheit(-273.15) == -459.67

def test_float_input():
    """Test conversion with float inputs."""
    assert celsius_to_fahrenheit(25.5) == 77.9
    assert celsius_to_fahrenheit(-10.5) == 13.1

def test_error_handling():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError):
        celsius_to_fahrenheit("not a number")
    
    with pytest.raises(TypeError):
        celsius_to_fahrenheit(None)

def test_precision():
    """Test conversion precision."""
    # Check exact rounding to 2 decimal places
    assert celsius_to_fahrenheit(10) == 50