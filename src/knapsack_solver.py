def solve_knapsack(items, capacity):
    """
    Solve the 0/1 Knapsack Problem using dynamic programming.

    Args:
        items (list): A list of tuples, where each tuple contains (weight, value)
        capacity (int): Maximum weight capacity of the knapsack

    Returns:
        int: Maximum value that can be achieved without exceeding weight capacity

    Raises:
        ValueError: If inputs are invalid (negative weights/capacity, non-numeric inputs)
    """
    # Validate inputs
    if not isinstance(capacity, (int, float)) or capacity < 0:
        raise ValueError("Capacity must be a non-negative number")
    
    # Return 0 for empty list of items
    if not items:
        return 0
    
    if not all(isinstance(item, (tuple, list)) and len(item) == 2 for item in items):
        raise ValueError("Items must be a list of (weight, value) tuples")
    
    for weight, value in items:
        if not isinstance(weight, (int, float)) or weight < 0:
            raise ValueError("Item weights must be non-negative numbers")
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Item values must be non-negative numbers")
    
    # Convert capacity to integer to handle potential float inputs
    capacity = int(capacity)
    
    # Dynamic programming solution
    n = len(items)
    # Create DP table initialized with zeros
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # Build table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        weight, value = items[i-1]
        
        for w in range(capacity + 1):
            # If including the item doesn't exceed capacity
            if weight <= w:
                # Max of including or excluding the current item
                dp[i][w] = max(
                    dp[i-1][w],  # Exclude current item
                    dp[i-1][w-int(weight)] + value  # Include current item
                )
            else:
                # Can't include item, copy previous row's value
                dp[i][w] = dp[i-1][w]
    
    # Return maximum value possible
    return dp[n][capacity]