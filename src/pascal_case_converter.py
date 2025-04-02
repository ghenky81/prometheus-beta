def convert_to_pascal_case(input_string: str) -> str:
    """
    Convert a given string to Pascal case.
    
    Pascal case is a naming convention where the first letter of each word is capitalized,
    and there are no spaces or punctuation between words.
    
    Args:
        input_string (str): The input string to be converted to Pascal case.
    
    Returns:
        str: The input string converted to Pascal case.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> convert_to_pascal_case("hello world")
        'HelloWorld'
        >>> convert_to_pascal_case("python_programming_language")
        'PythonProgrammingLanguage'
        >>> convert_to_pascal_case("test-case-conversion")
        'TestCaseConversion'
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If input is empty, return empty string
    if not input_string:
        return ""
    
    # Check if the input is already in Pascal case and meets requirements
    if input_string.isalpha() and input_string[0].isupper() and all(c.isupper() or c.islower() for c in input_string[1:]):
        return input_string
    
    # Replace non-alphanumeric characters with spaces
    cleaned_string = ''.join(char if char.isalnum() else ' ' for char in input_string)
    
    # Split the string into words and capitalize each word
    words = cleaned_string.split()
    pascal_case_words = [word.capitalize() for word in words]
    
    # Join the capitalized words without spaces
    return ''.join(pascal_case_words)