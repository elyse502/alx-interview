#!/usr/bin/python3
"""
Module 0-island_perimeter
"""


def island_perimeter(grid):
    """
    Calculate and return perimeter of island in the grid
    Grid is a rectangular grid where 0s represent water and 1s represent land
    Each cell is a square with a side length of 1
    There is only one island
    Args:
        grid [list] : 2d list of ints either 0 or 1
    Return:
       perimeter of island
    """
    visited = set()

    if not grid:
        return 0

    def dfs(i, j):
        """ depth first search """
        if (i, j) in visited:
            return 0
        if i >= len(grid) or\
                j >= len(grid[0]) or\
                i < 0 or j < 0 or\
                grid[i][j] == 0:
            return 1
        visited.add((i, j))
        result = dfs(i, j + 1)
        result += dfs(i, j - 1)
        result += dfs(i + 1, j)
        result += dfs(i - 1, j)
        return result

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # Do a dfs for only land
            if grid[i][j]:
                return dfs(i, j)
    return 0
