#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    """
    This function multiplies two matrices `m_a` and `m_b`.
    
    Args:
    - m_a: A list of lists of integers or floats.
    - m_b: A list of lists of integers or floats.
    
    Returns:
    - A list of lists representing the product of `m_a` and `m_b`.
    
    Raises:
    - TypeError: If `m_a` or `m_b` is not a list, or if `m_a` or `m_b` is not a list of lists, or if one element of those list of lists is not an integer or a float.
    - ValueError: If `m_a` or `m_b` is empty, or if `m_a` or `m_b` is not a rectangle, or if `m_a` and `m_b` can't be multiplied.
    
    Example:
    >>> matrix_mul([[1, 2], [3, 4]], [[2, 0], [1, 2]])
    [[4, 4], [10, 8]]
    """
    # Validate `m_a` and `m_b`
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if not all(isinstance(elem, (int, float)) for row in m_a for elem in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(elem, (int, float)) for row in m_b for elem in row):
        raise TypeError("m_b should contain only integers or floats")
    if not m_a:
        raise ValueError("m_a can't be empty")
    if not m_b:
        raise ValueError("m_b can't be empty")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise ValueError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise ValueError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    
    # Initialize the result matrix with zeros
    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    # Perform matrix multiplication
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]
    
    return result
