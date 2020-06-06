"""Solution to 8.6 Towers of Hanoi.

In the classic problem of the Towers of Hanoi, you have 3 towers and `N`
disks of different sizes which can slide onto any tower. The puzzle
starts with disks sorted in ascending order of size from top to bottom
(i.e., each disk sits on top of an even larger one). You have the
following constraints:

1. Only one disk can be moved at a time.
2. A disk is slid off the top of one tower onto another tower.
3. A disk cannot be placed on top of a smaller disk.

Write a program to move the disks from the first tower to the last using
stacks.
"""

from chapter3 import stack


class DiskOnSmallerDiskError(Exception):
    """Raised when trying to slide a disk is atop a smaller disk."""


class Tower(stack.Stack[int]):
    """A stack which checks that items are always in ascending order."""

    def push(self, item: int) -> None:
        """See base class.

        Raises:
            DiskOnSmallerDiskError: item was larger than the previous
                top of the stack.
        """
        if self and self.peek() < item:
            raise DiskOnSmallerDiskError()
        super().push(item)


class TowersOfHanoi():
    """Towers of Hanoi."""

    def __init__(self, N: int) -> None:
        self._towers = [Tower() for _ in range(3)]
        for i in reversed(range(N)):
            self._towers[0].push(i)

    def slide_disk(self, from_tower: int, to_tower: int) -> None:
        """Slides top disk of from_tower to top of to_tower.

        Args:
            from_tower: Index of tower from which to slide disk. [0, 2].
            to_tower: Index of tower to which to slide disk. [0, 2].

        Raises:
            EmptyStackError: Argument from_tower was empty.
            DiskOnSmallerDiskError: disk on top of from_tower was
                smaller than disk on top of to_tower.
        """
        self._towers[to_tower].push(self._towers[from_tower].pop())

    def is_solved(self) -> bool:
        """Returns True if all disks are on the last tower."""
        return not self._towers[0] and not self._towers[1]


def solve(towers: TowersOfHanoi, N: int) -> None:
    """Moves all disks from tower1 to tower3.

    Args:
        towers: Towers of Hanoi on which to move disks. All disks
            should be on the first tower.
        N: Number of disks in argument towers.
    """
    _solve_internal(towers, N, start=0, end=2, aux=1)


def _solve_internal(towers: TowersOfHanoi, N: int, start: int,
                    end: int, aux: int) -> None:
    for i in range(N):
        _solve_internal(towers, N=i, start=end, end=aux, aux=start)
        towers.slide_disk(from_tower=start, to_tower=end)
        _solve_internal(towers, N=i, start=aux, end=end, aux=start)
