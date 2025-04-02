def max_subarray_sum(arr, k):
    """
    Find the maximum sum of a subarray of length k in the given list.

    Args:
        arr (list): Input list of integers
        k (int): Length of the subarray to find maximum sum for

    Returns:
        list: Subarray with maximum sum, or empty list if k > len(arr)

    Examples:
        >>> max_subarray_sum([1, 4, 2, 10, 23, 3, 1, 0, 20], 4)
        [10, 23, 3, 1]
        >>> max_subarray_sum([2, 3, 4, 1, 5], 3)
        [3, 4, 1]
        >>> max_subarray_sum([1, 2, 3], 5)
        []
    """
    # If k is larger than the list length, return empty list
    if k > len(arr):
        return []
    
    # If k is 0 or negative, return empty list
    if k <= 0:
        return []
    
    # Initialize the first window sum
    window_sum = sum(arr[:k])
    max_sum = window_sum
    max_subarray = arr[:k]
    
    # Slide the window through the array
    for i in range(1, len(arr) - k + 1):
        # Remove the first element of previous window and add the next element
        window_sum = window_sum - arr[i-1] + arr[i+k-1]
        
        # Update max sum and subarray if current window sum is larger
        if window_sum > max_sum:
            max_sum = window_sum
            max_subarray = arr[i:i+k]
    
    return max_subarray