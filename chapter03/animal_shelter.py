"""Solution to 3.6 Animal Shelter.

An animal shelter, which holds only dogs and cats, operates on a
strictly "first in, first out" basis. People must adopt either the
"oldest" (based on arrival time) of all animals at the shelter, or they
can select whether they would prefer a dog or a cat (and will receive
the oldest animal of that type). They cannot select which specific
animal they would like. Create the data structures to maintain this
system and implement operations such as `enqueue`, `dequeueAny`,
`dequeueDog`, and `dequeueCat`. You may use the built-in `LinkedList`
data structure.
"""

import collections
import dataclasses
import enum
from typing import Any


class NoAvailablePetError(Exception):
    """Raised when an adoption request cannot be fulfilled."""


class PetType(enum.Enum):
    """Type of pet in animal shelter."""
    DOG = 1
    CAT = 2


@dataclasses.dataclass
class _Node:
    pet: Any
    order: int


class AnimalShelter:
    """Adoption service for cats and dogs."""

    def __init__(self) -> None:
        self._dogs: collections.deque = collections.deque()
        self._cats: collections.deque = collections.deque()
        self._num_seen = 0

    def enqueue(self, pet: Any, type_: PetType) -> None:
        """Puts pet of given type_ up for adoption."""
        node = _Node(pet, self._num_seen)
        if type_ == PetType.DOG:
            self._dogs.append(node)
        else:
            self._cats.append(node)
        self._num_seen += 1

    def dequeue_any(self) -> Any:
        """Returns "oldest" (based on arrival time) pet for adoption.

        Raises:
            NoAvailablePetError: There were no pets up for adoption.
        """
        if not self._dogs:
            return self.dequeue_cat()
        if not self._cats:
            return self.dequeue_dog()
        if self._dogs[0].order < self._cats[0].order:
            return self.dequeue_dog()
        return self.dequeue_cat()

    def dequeue_dog(self) -> Any:
        """Returns "oldest" (based on arrival time) dog for adoption.

        Raises:
            NoAvailablePetError: There were no dogs up for adoption.
        """
        try:
            return self._dogs.popleft().pet
        except IndexError as e:
            raise NoAvailablePetError() from e

    def dequeue_cat(self) -> Any:
        """Returns "oldest" (based on arrival time) cat for adoption.

        Raises:
            NoAvailablePetError: There were no pets up for adoption.
        """
        try:
            return self._cats.popleft().pet
        except IndexError as e:
            raise NoAvailablePetError() from e
