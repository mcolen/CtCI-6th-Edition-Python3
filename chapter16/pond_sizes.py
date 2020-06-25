"""Solution to 16.19 Pond Sizes.

You have an integer matrix representing a plot of land, where the value
at that location represents the height above sea leve. A value of zero
indicates water. A pond is a region of water connected vertically,
horizontally, or diagonally. The size of the pond is the total number of
connected water cells. Write a method to compute the sizes of all ponds
in the matrix.

EXAMPLE
Input:
  0 2 1 0
  0 1 0 1
  1 1 0 1
  0 1 0 1
Output: 2, 4, 1 (in any order)
"""

from typing import List, Sequence


def pond_sizes(matrix: Sequence[Sequence[int]]) -> List[int]:
    """Computes the sizes of all ponds in the matrix.

    Args:
        matrix: A matrix representing a plot of land, where the value at
            that location rpresents the height above sea level. A value
            of zero indicates water.

    Returns:
        A list of sizes of all ponds in the matrix. A pond is a region
        of water connected vertically, horizontally, or diagonally. The
        size of a pond is the total number of connected water cells.
    """
    m, n = len(matrix), len(matrix[0])
    visited = [[False] * n for _ in range(m)]

    def pond_size(r: int, c: int) -> int:
        visited[r][c] = True
        res = 1
        for r2 in [r - 1, r, r + 1]:
            for c2 in [c - 1, c, c + 1]:
                if (0 <= r2 < m and 0 <= c2 < n
                        and matrix[r2][c2] == 0 and not visited[r2][c2]):
                    res += pond_size(r2, c2)
        return res

    return [pond_size(r, c) for r in range(m) for c in range(n)
            if matrix[r][c] == 0 and not visited[r][c]]
