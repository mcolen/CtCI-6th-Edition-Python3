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
import enum
from typing import Any, NamedTuple


class NoAvailablePetError(Exception):
    """Raised when an adoption request cannot be fulfilled."""


class PetType(enum.Enum):
    """Type of pet in animal shelter."""
    DOG = 1
    CAT = 2


class AnimalShelter:
    """Adoption service for cats and dogs."""

    class _Node(NamedTuple):
        pet: Any
        order: int

    def __init__(self) -> None:
        self.dogs: collections.deque = collections.deque()
        self.cats: collections.deque = collections.deque()
        self.num_seen = 0

    def enqueue(self, pet: Any, type_: PetType) -> None:
        """Put pet of given type_ up for adoption."""
        node, self.num_seen = self._Node(pet, self.num_seen), self.num_seen + 1
        if type_ == PetType.DOG:
            self.dogs.append(node)
        else:
            self.cats.append(node)

    def dequeue_any(self) -> Any:
        """Return "oldest" (based on arrival time) pet for adoption."""
        if not self.dogs:
            return self.dequeue_cat()
        if not self.cats:
            return self.dequeue_dog()
        if self.dogs[0].order < self.cats[0].order:
            return self.dequeue_dog()
        return self.dequeue_cat()

    def dequeue_dog(self) -> Any:
        """Return "oldest" (based on arrival time) dog for adoption."""
        try:
            return self.dogs.popleft().pet
        except IndexError as e:
            raise NoAvailablePetError() from e

    def dequeue_cat(self) -> Any:
        """Return "oldest" (based on arrival time) cat for adoption."""
        try:
            return self.cats.popleft().pet
        except IndexError as e:
            raise NoAvailablePetError() from e
