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
    
    # Compute all possible subarrays of length k
    subarrays = [arr[i:i+k] for i in range(len(arr) - k + 1)]
    
    # If no subarrays found, return empty list
    if not subarrays:
        return []
    
    # Find the subarray with the maximum sum
    max_subarray = max(subarrays, key=sum)
    
    return max_subarray