def count_vowels(text):
    """
    Counts the number of vowels in a string.

    Args:
        text (str): The string to count vowels in.

    Returns:
        int: The number of vowels in the string.
    """
    vowels = 'aeiou'
    return sum(1 for char in text.lower() if char in vowels)