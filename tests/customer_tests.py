import unittest

from src.customer import Customer
from src.pub import Pub
from src.drink import Drink 

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Kate Middleton", 20.00)
        self.drink1 = Drink("Gin Sour", 4.00)
        self.drink2 = Drink("Magners", 3.00)
        drinks = [self.drink1, self.drink2]
        self.pub = Pub ("The Gallows", 100, drinks)
    
    def test_customer_has_name(self):
        self.assertEqual("Kate Middleton", self.customer.name)

    def test_wallet(self):
        self.assertEqual(20.00, self.customer.wallet)

    def test_buy_drink(self):
        drink = self.pub.find_drink(self.drink1)   
        self.customer.buy_drink(drink)
        self.assertEqual(16.00, self.customer.wallet)