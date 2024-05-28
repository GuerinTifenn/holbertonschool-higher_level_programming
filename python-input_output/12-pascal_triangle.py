#!/usr/bin/python3
"""Returns a list of lists of int representing the Pascal’s triangle of n"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal's triangle of n
    Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        # Create a new row with all elements initialized to 1
        row = [1] * (i + 1)

        # Calculate values for current row except for first and last elements
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        # Add the current row to the triangle
        triangle.append(row)

    return triangle
