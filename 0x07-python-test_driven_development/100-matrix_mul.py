#!/usr/bin/python3
"""Module for multiplying two matrices
"""

def matrix_mul(m_a, m_b):
    """Multiplies two matrices m_a and m_b
    
    Args:
        m_a (list of lists of int/float): First matrix
        m_b (list of lists of int/float): Second matrix
    
    Returns:
        list of lists of int/float: Result of the matrix multiplication
    
    Raises:
        TypeError: If m_a or m_b is not a list, or not a list of lists, or contains non-int/float elements
        ValueError: If m_a or m_b is empty, or if matrices can't be multiplied
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")

    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")

    if len(m_a) == 0 or len(m_b) == 0 or len(m_a[0]) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_a can't be empty or m_b can't be empty")

    if not all(isinstance(elem, (int, float)) for row in m_a for elem in row) or not all(isinstance(elem, (int, float)) for row in m_b for elem in row):
        raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a) or not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            result[i][j] = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b)))

    return result

