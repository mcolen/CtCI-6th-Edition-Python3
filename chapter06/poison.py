"""You have 1000 bottles of soda, and exactly one is poisoned. You have 10
test strips which can be used to detect poison. A single drop of poison
will turn the test strip positive permanently. You can put any number of
drops on a test strip at once and you can reuse a test strip as many
times as you'd like (as long as the results are negative). However, you
can only run tests once per day and it takes seven days to return a
result. How would you figure out the poisoned bottle in as few days as
possible?

FOLLOW UP
Write code to simulate your approach.
"""

import dataclasses
import random
from typing import List

DAYS_FOR_RESULT = 7


@dataclasses.dataclass
class _TestStrip:
    has_poison: bool = False
    day_poisoned: int = -1


class World:
    """Timed environment with bottles and test strips.

    Exactly one bottle is poisoned.

    Attributes:
        num_bottles: The number of bottles of soda. The bottles are
            numbered [0, num_bottles).
        num_test_strips: The number of test strips. The test strips are
            numbered [0, num_test_strips).
        day: The current day. Starts at 0. May be incremented to move
            time forward, but may never be decremented.
    """

    def __init__(self, num_test_strips: int, num_bottles: int,
                 poisoned_bottle_num: int) -> None:
        self._num_test_strips = num_test_strips
        self._test_strips = [_TestStrip() for i in range(num_test_strips)]
        self._num_bottles = num_bottles
        self._poisoned_bottle_num = poisoned_bottle_num
        self._day = 0

    @property
    def num_bottles(self) -> int:
        """Gets the number of bottles of soda in this environment."""
        return self._num_bottles

    @property
    def num_test_strips(self) -> int:
        """Gets the number of test strips in this environment."""
        return self._num_test_strips

    @property
    def day(self) -> int:
        """Gets or sets the current day number in this environment.

        Raises:
            ValueError: An attempt was made to decrease the day number.
        """
        return self._day

    @day.setter
    def day(self, day: int) -> None:
        if day < self._day:
            raise ValueError('day cannot be decreased')
        self._day = day

    def add_drop(self, bottle_num: int, test_strip_num: int) -> None:
        """Adds a drop from given bottle to given test_strip."""
        test_strip = self._test_strips[test_strip_num]
        if (bottle_num == self._poisoned_bottle_num
                and not test_strip.has_poison):
            test_strip.has_poison, test_strip.day_poisoned = True, self.day

    def positive_test_strips(self) -> List[int]:
        """Returns list of strip numbers with a positive test result."""
        res: List[int] = []
        for test_strip_num, test_strip in enumerate(self._test_strips):
            if (test_strip.has_poison and
                    self.day - test_strip.day_poisoned >= DAYS_FOR_RESULT):
                res.append(test_strip_num)
        return res


def find_poison(world: World) -> int:
    """Finds poisioned bottle in world in as few days as possible.

    This algorithm assumes that the number of bottles is no more than
    2 ** N, where N is the number of test strips.

    Args:
        world: World containing test strips and bottles, exactly one of
            which is poisoned. world.day will be advanced as necessary
            during testing.

    Returns:
        The bottle number of the poisoned bottle in argument world.
    """
    for i in range(world.num_bottles):
        for j in range(world.num_test_strips):
            if i & (1 << j):
                world.add_drop(bottle_num=i, test_strip_num=j)
    world.day += DAYS_FOR_RESULT
    return sum(1 << i for i in world.positive_test_strips())


def main() -> None:
    """Simulates finding poision with 1000 botles and 10 test strips."""
    poisoned_bottle_num = random.randrange(1000)
    world = World(num_bottles=1000, num_test_strips=10,
                  poisoned_bottle_num=poisoned_bottle_num)
    assert poisoned_bottle_num == find_poison(world)
    print(world.day)


if __name__ == '__main__':
    main()
