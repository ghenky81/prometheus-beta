import pytest
from src.pascal_case_converter import convert_to_pascal_case

def test_basic_conversion():
    """Test basic string to Pascal case conversion."""
    assert convert_to_pascal_case("hello world") == "HelloWorld"
    assert convert_to_pascal_case("python programming") == "PythonProgramming"

def test_already_pascal_case():
    """Test strings that are already in Pascal case."""
    assert convert_to_pascal_case("HelloWorld") == "HelloWorld"
    assert convert_to_pascal_case("PascalCase") == "PascalCase"

def test_mixed_delimiters():
    """Test conversion with different delimiters."""
    assert convert_to_pascal_case("python_programming_language") == "PythonProgrammingLanguage"
    assert convert_to_pascal_case("test-case-conversion") == "TestCaseConversion"
    assert convert_to_pascal_case("snake_case_to_pascal") == "SnakeCaseToPascal"

def test_edge_cases():
    """Test edge cases."""
    assert convert_to_pascal_case("") == ""  # Empty string
    assert convert_to_pascal_case("a") == "A"  # Single character
    assert convert_to_pascal_case("123 abc") == "123Abc"  # Numbers and letters

def test_special_characters():
    """Test handling of special characters."""
    assert convert_to_pascal_case("hello@world") == "HelloWorld"
    assert convert_to_pascal_case("python & programming") == "PythonProgramming"
    assert convert_to_pascal_case("!special#chars") == "SpecialChars"

def test_error_handling():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        convert_to_pascal_case(123)
    with pytest.raises(TypeError):
        convert_to_pascal_case(None)
    with pytest.raises(TypeError):
        convert_to_pascal_case(["list"])