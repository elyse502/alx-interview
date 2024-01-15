#!/usr/bin/python3
'''
python Module
'''


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in
    n H characters
    """
    operations = 0
    min_operations = 2

    while n > 1:
        if (n % min_operations == 0):
            operations += min_operations
            n = n / min_operations
        else:
            min_operations += 1
    return operations
