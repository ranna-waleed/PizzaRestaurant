import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.pizza import Margherita
from src.toppings import Cheese, Olives, Mushrooms

class TestToppings(unittest.TestCase):
    def test_cheese(self):
        pizza = Margherita()
        pizza = Cheese(pizza)
        self.assertEqual(pizza.get_description(), "Margherita, Cheese")
        self.assertEqual(pizza.get_cost(), 6.0)

    def test_olives(self):
        pizza = Margherita()
        pizza = Olives(pizza)
        self.assertEqual(pizza.get_description(), "Margherita, Olives")
        self.assertEqual(pizza.get_cost(), 5.5)

    def test_mushrooms(self):
        pizza = Margherita()
        pizza = Mushrooms(pizza)
        self.assertEqual(pizza.get_description(), "Margherita, Mushrooms")
        self.assertEqual(pizza.get_cost(), 5.7)

if __name__ == '__main__':
    unittest.main()