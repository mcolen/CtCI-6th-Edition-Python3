"""Solution to 16.22 Langton's Ant.

An ant is sitting on an infinite grid of white and black squares.
Initially, the grid is all white and the ant faces right. At each step,
it does the following:

(1) At a white square, flip the color of the square, turn 90 degrees
right (clockwise), and move forward one unit.
(2) At a black square, flip the color of the square, turn 90 degrees
left (counter-clockwise), and move forward one unit.

Write a program  to simulate the first `K` moves that the ant makes and
print the final board as a grid. Note that you are not provided with the
data structure to represent the grid. This is something you must design
yourself. The only input to your method is `K`. You should print the
final grid and return nothing. The method signature might be something
like `void printKMoves(int K)`.
"""

import enum


class Color(enum.Enum):
    """Color of a square on the grid."""
    WHITE = 0
    BLACK = 1


class Orientation(enum.Enum):
    """Possible orientations of the ant."""
    LEFT = enum.auto()
    UP = enum.auto()
    RIGHT = enum.auto()
    DOWN = enum.auto()


CLOCKWISE = {
    Orientation.LEFT: Orientation.UP,
    Orientation.UP: Orientation.RIGHT,
    Orientation.RIGHT: Orientation.DOWN,
    Orientation.DOWN: Orientation.LEFT,
}

COUNTER_CLOCKWISE = {
    Orientation.LEFT: Orientation.DOWN,
    Orientation.DOWN: Orientation.RIGHT,
    Orientation.RIGHT: Orientation.UP,
    Orientation.UP: Orientation.LEFT,
}

MOVEMENT = {
    Orientation.LEFT: (-1, 0),
    Orientation.UP: (0, 1),
    Orientation.RIGHT: (1, 0),
    Orientation.DOWN: (0, -1),
}


def print_k_moves(k: int) -> None:
    """Simulates the first k moves of Langton's ant.

    Prints the resulting board as a grid.
    """
    board, orientation, x, y = {(0, 0): Color.WHITE}, Orientation.RIGHT, 0, 0
    for _ in range(k):
        if board[x, y] == Color.WHITE:
            orientation = CLOCKWISE[orientation]
            board[x, y] = Color.BLACK
        else:
            assert board[x, y] == Color.BLACK
            orientation = COUNTER_CLOCKWISE[orientation]
            board[x, y] = Color.WHITE
        x, y = x + MOVEMENT[orientation][0], y + MOVEMENT[orientation][1]
        if (x, y) not in board:
            board[x, y] = Color.WHITE

    min_x, max_x = min(x for x, _ in board), max(x for x, _ in board)
    min_y, max_y = min(y for _, y in board), max(y for _, y in board)
    for r in range(max_y, min_y - 1, -1):
        print(' '.join(str(board.get((c, r), Color.WHITE).value)
                       for c in range(min_x, max_x + 1)))
