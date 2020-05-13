from unittest import TestCase

from src.binary_search.binary_search.search_ceiling_of_a_number.search_ceiling_of_a_number import \
    search_ceiling_of_a_number


class Test(TestCase):
    def test1(self):
        self.assertEqual(1, search_ceiling_of_a_number([4, 6, 10], 6))

    def test1(self):
        self.assertEqual(4, search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))

    def test2(self):
        self.assertEqual(-1, search_ceiling_of_a_number([4, 6, 10], 17))

    def test3(self):
        self.assertEqual(0, search_ceiling_of_a_number([4, 6, 10], -1))
