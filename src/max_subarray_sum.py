def max_subarray_sum(arr):
    """
    Find the maximum sum of a contiguous subarray in the given list of integers.
    
    This function uses Kadane's algorithm to efficiently find the maximum sum
    of a contiguous subarray, handling both positive and negative numbers.
    
    Args:
        arr (list): A list of integers to find the maximum subarray sum from.
    
    Returns:
        int: The maximum sum of any contiguous subarray.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the input list is empty.
    
    Examples:
        >>> max_subarray_sum([1, -2, 3, 4, -1, 5])
        11
        >>> max_subarray_sum([-1, -2, -3, -4])
        -1
        >>> max_subarray_sum([])
        Traceback (most recent call last):
            ...
        ValueError: Input list cannot be empty
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Initialize max_so_far and max_ending_here with the first element
    max_so_far = max_ending_here = arr[0]
    
    # Iterate through the rest of the array
    for num in arr[1:]:
        # Choose the maximum between the current number 
        # and the sum of current number and previous max_ending_here
        max_ending_here = max(num, max_ending_here + num)
        
        # Update max_so_far if max_ending_here is larger
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far