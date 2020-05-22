"""Tests for chapter3.animal_shelter."""

import unittest

from chapter3 import animal_shelter


class TestAnimalShelter(unittest.TestCase):

    def test_many_dequeue_any(self) -> None:
        shelter = animal_shelter.AnimalShelter()
        shelter.enqueue('Callie', animal_shelter.PetType.CAT)
        shelter.enqueue('Kiki', animal_shelter.PetType.CAT)
        shelter.enqueue('Fido', animal_shelter.PetType.DOG)
        shelter.enqueue('Dora', animal_shelter.PetType.DOG)
        shelter.enqueue('Kari', animal_shelter.PetType.CAT)
        shelter.enqueue('Dexter', animal_shelter.PetType.DOG)
        shelter.enqueue('Dobo', animal_shelter.PetType.DOG)
        shelter.enqueue('Copa', animal_shelter.PetType.CAT)

        self.assertEqual('Callie', shelter.dequeue_any())
        self.assertEqual('Kiki', shelter.dequeue_any())
        self.assertEqual('Fido', shelter.dequeue_any())

        shelter.enqueue('Dapa', animal_shelter.PetType.DOG)
        shelter.enqueue('Kilo', animal_shelter.PetType.CAT)

        self.assertEqual('Dora', shelter.dequeue_any())
        self.assertEqual('Kari', shelter.dequeue_any())
        self.assertEqual('Dexter', shelter.dequeue_any())
        self.assertEqual('Dobo', shelter.dequeue_any())
        self.assertEqual('Copa', shelter.dequeue_any())
        self.assertEqual('Dapa', shelter.dequeue_any())
        self.assertEqual('Kilo', shelter.dequeue_any())
        self.assertRaises(animal_shelter.NoAvailablePetError,
                          shelter.dequeue_any)


if __name__ == '__main__':
    unittest.main()
