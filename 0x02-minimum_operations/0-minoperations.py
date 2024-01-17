#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n):
    """
    Calculates the minimum number of operations required to
    reach a given number 'n' by performing only two operations:
    - Copy All: Copy the current string.
    - Paste: Paste the copied string.

    Args:
        n (int): The target number.

    Returns:
        int: The minimum number of operations required.
    """
    # Check if the target number is less than or equal to 1
    if n <= 1:
        return 0

    x = 2  # Initialize x to 2
    y = 0  # Initialize y to 0

    while x <= n:  # Loop until x is less than or equal to the target number
        if n % x == 0:  # Check if the target number is divisible by x
            y += x  # Add x to y
            n = n / x  # Update the target number by dividing it by x
        else:
            x += 1  # Increment x by 1

    return y  # Return the minimum number of operations required
