"""Solution to 1.8 Zero Matrix

Write an algorithm such that if an element in an M x N matrix is 0, its
entire row and column are set to 0.
"""

from typing import Sequence


def zero_matrix(matrix: Sequence[Sequence[int]]) -> None:
    """Sets entire row and column to 0 for all 0 elements in matrix."""
    m, n = len(matrix), len(matrix[0])
    rows = [i for i in range(m) if any(matrix[i][j] == 0 for j in range(n))]
    cols = [j for j in range(n) if any(matrix[i][j] == 0 for i in range(m))]
    for i in rows:
        for j in range(n):
            matrix[i][j] = 0
    for j in cols:
        for i in range(m):
            matrix[i][j] = 0
