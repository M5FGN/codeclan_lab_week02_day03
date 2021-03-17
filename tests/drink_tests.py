import unittest

from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Magner's", 3.00)

    def test_drink_has_name(self):
        self.assertEqual("Magner's", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(3.00, self.drink.price)    