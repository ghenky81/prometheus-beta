def convert_to_alternating_dot_case(input_string):
    """
    Convert a string to alternating dot case.

    In alternating dot case, characters alternate between lowercase and uppercase,
    with each character separated by a dot. Preserves case of non-letter characters.

    Args:
        input_string (str): The input string to convert.

    Returns:
        str: The string converted to alternating dot case.

    Raises:
        TypeError: If input is not a string.
        ValueError: If input is an empty string.

    Examples:
        >>> convert_to_alternating_dot_case("hello")
        'h.E.l.L.o'
        >>> convert_to_alternating_dot_case("Python")
        'p.Y.t.H.o.N'
        >>> convert_to_alternating_dot_case("hello world")
        'h.E.l.L.o. .W.o.R.l.D'
    """
    # Validate input
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    if not input_string:
        raise ValueError("Input string cannot be empty")
    
    # Convert to alternating dot case
    result = []
    is_uppercase_turn = False
    
    for char in input_string:
        # If character is a letter, alternate case
        if char.isalpha():
            if is_uppercase_turn:
                result.append(char.upper())
            else:
                result.append(char.lower())
            is_uppercase_turn = not is_uppercase_turn
        else:
            # Non-letter characters keep their original form
            result.append(char)
        
        # Always add a dot, except after the last character
        if char != input_string[-1]:
            result.append('.')
    
    return ''.join(result)