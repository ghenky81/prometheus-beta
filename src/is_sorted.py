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

    # Check if all elements can be compared numerically
    try:
        numeric_lst = [float(x) for x in lst]
    except (TypeError, ValueError):
        # If elements can't be converted to numeric, check direct comparison
        first_type = type(lst[0])
        if not all(isinstance(x, first_type) for x in lst):
            raise TypeError("All list elements must have the same comparable type")

        # Proceed with type-specific comparison
        if ascending:
            return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
        else:
            return all(lst[i] >= lst[i+1] for i in range(len(lst)-1))

    # Numeric comparison
    if ascending:
        return all(numeric_lst[i] <= numeric_lst[i+1] for i in range(len(numeric_lst)-1))
    else:
        return all(numeric_lst[i] >= numeric_lst[i+1] for i in range(len(numeric_lst)-1))