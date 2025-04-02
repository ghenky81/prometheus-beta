def stooge_sort(arr):
    """
    Implement the Stooge Sort algorithm.
    
    Stooge sort is a recursive sorting algorithm with a time complexity of O(n^(log 3 / log 1.5)) ≈ O(n^2.7095).
    It works by recursively sorting the first 2/3 of the list, then the last 2/3, and then the first 2/3 again.
    
    Args:
        arr (list): The input list to be sorted in-place.
    
    Returns:
        list: The sorted list.
    
    Raises:
        TypeError: If the input is not a list.
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr
    
    # If first element is larger than last, swap them
    if arr[0] > arr[-1]:
        arr[0], arr[-1] = arr[-1], arr[0]
    
    # If list has 3 or more elements, recursively sort
    if len(arr) > 2:
        # Calculate two-thirds point
        t = len(arr) // 3
        
        # Recursively sort first 2/3
        stooge_sort(arr[:len(arr)-t])
        
        # Recursively sort last 2/3
        stooge_sort(arr[t:])
        
        # Recursively sort first 2/3 again
        stooge_sort(arr[:len(arr)-t])
    
    return arr