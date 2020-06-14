"""Solution to 16.4 Tic Tac Win.

Design an algorithm to figure out if someone has won a game of
tic-tac-toe.
"""

import enum
from typing import Optional, Sequence


class Piece(enum.Enum):
    """A marker on a tic-tac-toe board."""
    RED = 1
    BLUE = 2


def has_winner(board: Sequence[Sequence[Optional[Piece]]]) -> bool:
    """Figures out if someone has won a game of tic-tac-toe.

    Args:
        board: A 3x3 sequence representing the squares in a tic-tac-toe
            grid. Each square may or may not have a piece on it.

    Returns:
        True if either side has achieved 3 pieces in a row.
    """
    n = 3  # Number of squares in one row/column of tic-tac-toe.
    for r in range(n):
        if board[r][0] and board[r][0] == board[r][1] == board[r][2]:
            return True
    for c in range(n):
        if board[0][c] and board[0][c] == board[1][c] == board[2][c]:
            return True
    if board[0][0] and board[0][0] == board[1][1] == board[2][2]:
        return True
    if board[0][2] and board[0][2] == board[1][1] == board[2][0]:
        return True
    return False
