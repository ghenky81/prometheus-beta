def is_sorted(lst, ascending=True):
    """
    Check if a list is sorted in ascending or descending order.

    Args:
        lst (list): The list to check for sorting.
        ascending (bool, optional): If True, check for ascending order. 
                                    If False, check for descending order. 
                                    Defaults to True.

    Returns:
        bool: True if the list is sorted according to the specified order, 
              False otherwise.

    Raises:
        TypeError: If the input is not a list or contains non-comparable elements.
    """
    # Check if input is a list
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")

    # Handle empty or single-element lists (always considered sorted)
    if len(lst) <= 1:
        return True

    try:
        # Check if all elements can be compared with each other
        if ascending:
            return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
        else:
            return all(lst[i] >= lst[i+1] for i in range(len(lst)-1))
    except TypeError:
        # If comparison fails, it means elements are not comparable
        raise TypeError("List contains elements that cannot be compared")