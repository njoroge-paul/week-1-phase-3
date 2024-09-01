def calculate_factorial(n):
    """
    Calculates the factorial of a non-negative integer.

    Args:
        n (int): The number to calculate the factorial of.

    Returns:
        int: The factorial of n.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n == 0:
        return 1
    else:
        return n * calculate_factorial(n-1)