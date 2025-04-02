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
    
    def _stooge_sort_recursive(arr, i, j):
        """
        Recursive helper function to perform Stooge Sort.
        
        Args:
            arr (list): The list to be sorted.
            i (int): Starting index.
            j (int): Ending index.
        """
        # If first element is larger than last, swap them
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        
        # If more than 2 elements in this segment
        if j - i + 1 > 2:
            t = (j - i + 1) // 3
            
            # Recursively sort first 2/3 
            _stooge_sort_recursive(arr, i, j - t)
            
            # Recursively sort last 2/3
            _stooge_sort_recursive(arr, i + t, j)
            
            # Recursively sort first 2/3 again
            _stooge_sort_recursive(arr, i, j - t)
    
    # Call recursive helper function on full list if not empty
    if arr:
        _stooge_sort_recursive(arr, 0, len(arr) - 1)
    
    return arr