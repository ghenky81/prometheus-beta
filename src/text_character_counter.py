def count_vowels_and_consonants(text: str) -> dict:
    """
    Count the number of vowels and consonants in a given string of English text.
    
    Args:
        text (str): Input text to analyze
    
    Returns:
        dict: A dictionary with 'vowels' and 'consonants' counts
    
    Raises:
        TypeError: If input is not a string
    """
    # Validate input type
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Convert to lowercase for consistent counting
    text = text.lower()
    
    # Define vowels (using standard ASCII vowels)
    vowels = set('aeiou')
    
    # Initialize counters
    vowel_count = 0
    consonant_count = 0
    
    # Count vowels and consonants
    for char in text:
        # Normalize accented characters to their base form
        # Use only basic ASCII letters for counting
        char = char.encode('ascii', 'ignore').decode('ascii')
        
        # Only count if not empty after normalization
        if char:
            if char.isalpha():
                if char in vowels:
                    vowel_count += 1
                else:
                    consonant_count += 1
    
    return {
        'vowels': vowel_count,
        'consonants': consonant_count
    }