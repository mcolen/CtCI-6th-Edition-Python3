"""Solution to 1.7 Rotate Matrix.

Given an image represented by an N x N matrix, where each pixel in the
image is represented by an integer, write a method to rotate the image
by 90 degrees. Can you do this in place?
"""

from typing import MutableSequence, Sequence


def rotate_matrix(matrix: Sequence[MutableSequence[int]]) -> None:
    """Rotates matrix clockwise by 90 degrees in place."""
    n = len(matrix)
    for i in range((n + 1) // 2):
        for j in range(n // 2):
            x, y, tmp = i, j, matrix[i][j]
            for _ in range(3):
                matrix[x][y] = matrix[n - y - 1][x]
                x, y = n - y - 1, x
            matrix[x][y] = tmp
