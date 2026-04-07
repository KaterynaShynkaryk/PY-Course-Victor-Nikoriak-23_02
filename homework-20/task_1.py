class Mathematician:

    def square_nums(self, numbers):
        return [n**2 for n in numbers]

    def remove_positives(self, numbers):
        return [n for n in numbers if n <= 0]

    def filter_leaps(self, years):
        return [y for y in years if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)]


import unittest

class TestMathematician(unittest.TestCase):
    def setUp(self):
        self.m = Mathematician()

    def test_square_nums(self):
        self.assertEqual(self.m.square_nums([7, 11, 5, 4]), [49, 121, 25, 16])
        self.assertEqual(self.m.square_nums([]), [])
        self.assertEqual(self.m.square_nums([-2, -3]), [4, 9])

    def test_remove_positives(self):
        self.assertEqual(self.m.remove_positives([26, -11, -8, 13, -90]), [-11, -8, -90])
        self.assertEqual(self.m.remove_positives([0, 1, -1]), [0, -1])
        self.assertEqual(self.m.remove_positives([5, 10, 15]), [])


    def test_filter_leaps(self):
        self.assertEqual(self.m.filter_leaps([2001, 1884, 1995, 2003, 2020]), [1884, 2020])
        self.assertEqual(self.m.filter_leaps([1600, 1700, 1800, 2000]), [1600, 2000])
        self.assertEqual(self.m.filter_leaps([]), [])


if __name__ == "__main__":
    unittest.main()


