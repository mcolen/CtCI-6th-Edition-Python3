"""Tests for chapter3.animal_shelter."""

import unittest

from chapter3.animal_shelter import AnimalShelter, NoAvailablePetError, PetType


class TestAnimalShelter(unittest.TestCase):

    def test_many_dequeue_any(self):
        shelter = AnimalShelter()
        shelter.enqueue('Callie', PetType.CAT)
        shelter.enqueue('Kiki', PetType.CAT)
        shelter.enqueue('Fido', PetType.DOG)
        shelter.enqueue('Dora', PetType.DOG)
        shelter.enqueue('Kari', PetType.CAT)
        shelter.enqueue('Dexter', PetType.DOG)
        shelter.enqueue('Dobo', PetType.DOG)
        shelter.enqueue('Copa', PetType.CAT)

        self.assertEqual('Callie', shelter.dequeue_any())
        self.assertEqual('Kiki', shelter.dequeue_any())
        self.assertEqual('Fido', shelter.dequeue_any())

        shelter.enqueue('Dapa', PetType.DOG)
        shelter.enqueue('Kilo', PetType.CAT)

        self.assertEqual('Dora', shelter.dequeue_any())
        self.assertEqual('Kari', shelter.dequeue_any())
        self.assertEqual('Dexter', shelter.dequeue_any())
        self.assertEqual('Dobo', shelter.dequeue_any())
        self.assertEqual('Copa', shelter.dequeue_any())
        self.assertEqual('Dapa', shelter.dequeue_any())
        self.assertEqual('Kilo', shelter.dequeue_any())
        self.assertRaises(NoAvailablePetError, shelter.dequeue_any)


if __name__ == '__main__':
    unittest.main()
