#!/usr/bin/python3
"""
This module defines a function that divides all elements of a matrix.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix: A list of lists of integers or floats.
        div: The divisor, which must be an integer or float.

    Returns:
        A new matrix with the result of the division, rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix contains non-numeric values, if the rows are of
                   different sizes, or if div is not a number.
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]

