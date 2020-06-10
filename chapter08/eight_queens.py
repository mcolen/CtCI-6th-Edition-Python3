"""Solution to 8.12 Eight Queens.

Write an algorithm to print all ways of arranging eight queens on an 8x8
chess board so that none of them share the same row, column, or
diagonal. In this case, "diagonal" means all diagonals, not just the two
that bisect the board.
"""

from typing import AbstractSet, MutableSet, NamedTuple


class Square(NamedTuple):
    """Coordinates of a square on a chess board."""
    row: int
    column: int


def print_solutions(n: int = 8) -> None:
    """Prints all ways of solving the n-queens puzzle.

    https://en.wikipedia.org/wiki/Eight_queens_puzzle.
    """
    _print_solutions_internal(n, queens=set())


def _print_solutions_internal(n: int, queens: MutableSet[Square]) -> None:
    if len(queens) == n:
        _print_solution(n, queens)
        print()
        return
    for i in range(n):
        square = Square(row=len(queens), column=i)
        if any(_share_column(square, queen) or
               _share_diagonal(square, queen) for queen in queens):
            continue
        queens.add(square)
        _print_solutions_internal(n, queens)
        queens.remove(square)


def _print_solution(n: int, queens: AbstractSet[Square]) -> None:
    for i in range(n):
        print(' '.join('Q' if Square(row=i, column=j) in queens else '-'
                       for j in range(n)))


def _share_column(square1: Square, square2: Square) -> bool:
    return square1.column == square2.column


def _share_diagonal(square1: Square, square2: Square) -> bool:
    return (square1.row + square1.column == square2.row + square2.column or
            square1.row - square1.column == square2.row - square2.column)
