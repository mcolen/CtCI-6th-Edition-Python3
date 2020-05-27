"""Solution to 1.8 Zero Matrix.

Write an algorithm such that if an element in an M x N matrix is 0, its
entire row and column are set to 0.
"""

from typing import MutableSequence, Sequence


def zero_matrix(matrix: Sequence[MutableSequence[int]]) -> None:
    """Sets entire row and column to 0 for all 0 elements in matrix."""
    m, n = len(matrix), len(matrix[0])
    first_row_zero = 0 in matrix[0]
    first_col_zero = any(row[0] == 0 for row in matrix)
    # Identify rows with a 0.
    for row in matrix:
        if 0 in row:
            row[0] = 0
    # Identify cols with a 0.
    for j in range(n):
        if any(row[j] == 0 for row in matrix):
            matrix[0][j] = 0
    # Set necessary elements to 0.
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    if first_row_zero:
        for j in range(n):
            matrix[0][j] = 0
    if first_col_zero:
        for i in range(m):
            matrix[i][0] = 0
