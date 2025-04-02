def fibonacci_subsequence(n):
    """
    Generate a Fibonacci subsequence of specified length.

    Args:
        n (int): The length of the Fibonacci subsequence to generate.

    Returns:
        list: A list containing the first n numbers of the Fibonacci subsequence.

    Raises:
        ValueError: If the input is not a positive integer.
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Handle special cases
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    # Generate Fibonacci subsequence
    subsequence = [0, 1]
    while len(subsequence) < n:
        next_num = subsequence[-1] + subsequence[-2]
        subsequence.append(next_num)
    
    return subsequence