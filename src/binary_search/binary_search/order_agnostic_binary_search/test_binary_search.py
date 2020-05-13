from unittest import TestCase

from src.binary_search.binary_search.order_agnostic_binary_search.binary_search import binary_search


class Test(TestCase):
    def test_binary_search(self):
        nums = [4, 6, 10]
        self.assertEqual(2, binary_search(nums, 10))

    def test_2(self):
        result = binary_search([1, 2, 3, 4, 5, 6, 7], 5)
        self.assertEqual(4, result)

    def test_3(self):
        self.assertEqual(0, binary_search([10, 6, 4], 10))

    def test_4(self):
        self.assertEqual(2, binary_search([10, 6, 4], 4))