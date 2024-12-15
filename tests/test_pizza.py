import unittest
from src.pizza import Margherita, Pepperoni

class TestPizza(unittest.TestCase):
    def test_margherita(self):
        pizza = Margherita()
        self.assertEqual(pizza.get_description(), "Margherita")
        self.assertEqual(pizza.get_cost(), 5.0)

    def test_pepperoni(self):
        pizza = Pepperoni()
        self.assertEqual(pizza.get_description(), "Pepperoni")
        self.assertEqual(pizza.get_cost(), 6.0)

if __name__ == '__main__':
    unittest.main()