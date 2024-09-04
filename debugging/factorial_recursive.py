#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer n using recursion.

    A factorial of a non-negative integer n is the product of all positive integers less than or equal to n.
    The factorial of 0 is defined as 1.

    Parameters:
    n (int): The non-negative integer for which the factorial is to be calculated.

    Returns:
    int: The factorial of the input number n.
    """
    if n == 0:
        return 1  # Base case: the factorial of 0 is 1
    else:
        return n * factorial(n-1)  # Recursive case: n! = n * (n-1)!

# Get the number from the command-line argument and calculate its factorial
f = factorial(int(sys.argv[1]))

# Print the calculated factorial
print(f)