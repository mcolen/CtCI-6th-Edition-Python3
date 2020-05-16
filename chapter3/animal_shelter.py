"""Solution to 3.6 Animal Shelter

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

from enum import Enum
from typing import Any


class NoAvailablePetError(Exception):
    """Raised when an adoption request cannot be fulfilled."""


class PetType(Enum):
    """Type of pet in animal shelter."""
    DOG = 1
    CAT = 2


class AnimalShelter:
    """Adoption service for cats and dogs."""

    class Node:
        """Node with links for any pet and pets of same type."""

        def __init__(self, pet: Any = None, next_=None, prev=None):
            self.pet = pet
            self.next = next_
            self.prev = prev
            self.next_same_type = self.prev_same_type = None

        def splice_out(self):
            """Removes self out of enclosing linked list."""
            self.prev.next = self.next
            self.next.prev = self.prev
            self.next_same_type.prev_same_type = self.prev_same_type
            self.prev_same_type.next_same_type = self.next_same_type

        def update_neighbors(self):
            """Updates neighbors of self to point to self."""
            self.prev.next = self
            self.next.prev = self
            self.prev_same_type.next_same_type = self
            self.next_same_type.prev_same_type = self

    def __init__(self):
        self.head, self.tail = self.Node(), self.Node()
        self.head.next = self.tail
        self.tail.prev = self.head

        self.head_dog, self.tail_dog = self.Node(), self.Node()
        self.head_dog.next_same_type = self.tail_dog
        self.tail_dog.prev_same_type = self.head_dog

        self.head_cat, self.tail_cat = self.Node(), self.Node()
        self.head_cat.next_same_type = self.tail_cat
        self.tail_cat.prev_same_type = self.head_cat

    def enqueue(self, pet: Any, type_: PetType) -> None:
        """Put pet of given type_ up for adoption."""
        node = self.Node(pet, next_=self.tail, prev=self.tail.prev)
        if type_ == PetType.DOG:
            node.next_same_type = self.tail_dog
            node.prev_same_type = self.tail_dog.prev_same_type
        else:
            node.next_same_type = self.tail_cat
            node.prev_same_type = self.tail_cat.prev_same_type
        node.update_neighbors()

    def dequeue_any(self) -> Any:
        """Returns "oldest" (based on arrival time) pet for adoption."""
        node = self.head.next
        if node is self.tail:
            raise NoAvailablePetError
        node.splice_out()
        return node.pet

    def dequeue_dog(self) -> Any:
        """Returns "oldest" (based on arrival time) dog for adoption."""
        node = self.head_dog.next_same_type
        if node is self.tail_dog:
            raise NoAvailablePetError
        node.splice_out()
        return node.pet

    def dequeue_cat(self) -> Any:
        """Returns "oldest" (based on arrival time) cat for adoption."""
        node = self.head_cat.next_same_type
        if node is self.tail_cat:
            raise NoAvailablePetError
        node.splice_out()
        return node.pet
