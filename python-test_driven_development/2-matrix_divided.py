#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Args:
        matrix (list of lists): Matrix to be divided.
        div (int or float): Divisor.

    Returns:
        list of lists: New matrix with elements divided by the divisor.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats,
                   or if div is not a number.
        ZeroDivisionError: If div is zero.
    """
    # Message d'Error
    list_matr = "matrix must be a matrix (list of lists) of integers/floats"
    size_matr = "Each row of the matrix must have the same size"
    div_matr = "div must be a number"
    div_matr0 = "division by zero"
    # Validate matrix
    if not (isinstance(matrix, list) and
            all(isinstance(row, list) for row in matrix)):
        raise TypeError(list_matr)

    # Validate elements of matrix
    for row in matrix:
        if not all(isinstance(x, (int, float)) for x in row):
            raise TypeError(list_matr)
        if len(row) != len(matrix[0]):
            raise TypeError(size_matr)

    # Validate divisor
    if not isinstance(div, (int, float)):
        raise TypeError(div_matr)
    if div == 0:
        raise ZeroDivisionError(div_matr0)

    # Divide elements of matrix by div
    new_matrix = []
    for row in matrix:
        new_row = [round(x / div, 2) for x in row]
        new_matrix.append(new_row)

    return new_matrix
