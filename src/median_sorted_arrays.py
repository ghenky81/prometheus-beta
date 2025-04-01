def find_median_sorted_arrays(nums1, nums2):
    """
    Find the median of two sorted arrays with O(log(min(m,n))) time complexity.
    
    Args:
        nums1 (list): First sorted input array
        nums2 (list): Second sorted input array
    
    Returns:
        float: Median of the two sorted arrays
    
    Raises:
        TypeError: If inputs are not lists
        ValueError: If inputs contain non-numeric elements
    """
    # Type checking
    if not (isinstance(nums1, list) and isinstance(nums2, list)):
        raise TypeError("Inputs must be lists")
    
    # Validate numeric inputs
    if not (all(isinstance(x, (int, float)) for x in nums1) and 
            all(isinstance(x, (int, float)) for x in nums2)):
        raise ValueError("Arrays must contain only numeric elements")
    
    # Ensure nums1 is the smaller array to optimize binary search
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    left, right = 0, m
    
    while left <= right:
        # Partition point for nums1
        partitionX = (left + right) // 2
        # Corresponding partition point for nums2
        partitionY = (m + n + 1) // 2 - partitionX
        
        # Handle edge cases for max/min elements
        maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
        minRightX = float('inf') if partitionX == m else nums1[partitionX]
        
        maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
        minRightY = float('inf') if partitionY == n else nums2[partitionY]
        
        # Check if we have found the correct partition
        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            # If total length is odd
            if (m + n) % 2 == 1:
                return max(maxLeftX, maxLeftY)
            
            # If total length is even
            return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
        
        # Adjust binary search boundaries
        elif maxLeftX > minRightY:
            right = partitionX - 1
        else:
            left = partitionX + 1
    
    # If no valid partition found
    raise ValueError("Input arrays are not sorted")