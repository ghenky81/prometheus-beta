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

    # Ensure all elements have the same type and are comparable
    first_type = type(lst[0])
    if not all(isinstance(x, first_type) for x in lst):
        raise TypeError("All list elements must have the same comparable type")

    # Determine comparison function based on ascending parameter
    if ascending:
        # Check if each element is less than or equal to the next
        return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
    else:
        # Check if each element is greater than or equal to the next
        return all(lst[i] >= lst[i+1] for i in range(len(lst)-1))