#!/usr/bin/python3
"""Minimum operations module.

Computes the fewest number of Copy All / Paste operations needed
to get exactly n 'H' characters in a file that starts with one 'H'.
"""


def minOperations(n):
    """Return the fewest operations needed to obtain n 'H' characters.

    The only operations allowed are `Copy All` and `Paste`. The answer is
    the sum of the prime factors of n, because each prime factor p costs
    one Copy All plus (p - 1) Paste operations, i.e. p operations.

    Args:
        n (int): the target number of 'H' characters.

    Returns:
        int: the minimum number of operations, or 0 if n is impossible
        to achieve (n is not an integer, or n < 2).
    """
    if not isinstance(n, int) or n < 2:
        return 0

    operations = 0
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    return operations
