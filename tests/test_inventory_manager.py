import unittest
from src.inventory_manager import InventoryManager

class TestInventoryManager(unittest.TestCase):
    def test_singleton(self):
        manager1 = InventoryManager()
        manager2 = InventoryManager()
        self.assertIs(manager1, manager2)

    def test_check_and_decrement(self):
        manager = InventoryManager()
        self.assertTrue(manager.check_and_decrement("Cheese"))
        self.assertFalse(manager.check_and_decrement("NonExistentItem"))

if __name__ == '__main__':
    unittest.main()