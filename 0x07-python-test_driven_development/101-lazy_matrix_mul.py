#!/usr/bin/python3

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    try:
        # Try to convert the input matrices to NumPy arrays
        m_a = np.array(m_a)
        m_b = np.array(m_b)
    except ValueError as e:
        # If the conversion fails, raise a custom exception
        raise TypeError("Input matrices must be a list of lists containing integers or floats") from e

    # Check if the matrices are compatible for multiplication
    if m_a.shape[1] != m_b.shape[0]:
        raise ValueError("Incompatible matrices for multiplication")

    # Use NumPy's dot function to multiply the matrices
    result = np.dot(m_a, m_b)

    return result
