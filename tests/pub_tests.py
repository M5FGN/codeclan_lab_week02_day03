import unittest

from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.drink1 = Drink("Gin Sour", 4.00)
        self.drink2 = Drink("Magners", 3.00)
        drinks = [self.drink1, self.drink2]
        self.pub = Pub("The Prancing Pony", 100.00, drinks)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_get_cash(self):
        self.assertEqual(100, self.pub.till)

    # def test_drinks(self):
    #     self.assertEqual(4, len(self.drinks))

    def test_find_drink(self):
        drink = self.pub.find_drink(self.drink1)
        self.assertEqual(self.drink1, drink)

    def test_sell_drink(self):
        drink = self.pub.find_drink(self.drink1)   
        self.pub.sell_drink(drink)
        self.assertEqual(104.00, self.pub.till)


 
