import unittest

from square import area, perimeter


class SquareAreaTestCase(unittest.TestCase):
    def test_zero_side(self):
        self.assertEqual(area(0), 0)

    def test_unit_side(self):
        self.assertEqual(area(1), 1)

    def test_integer_side(self):
        self.assertEqual(area(4), 16)

    def test_float_side(self):
        self.assertAlmostEqual(area(1.5), 2.25)

    def test_large_side(self):
        self.assertEqual(area(10**6), 10**12)


class SquarePerimeterTestCase(unittest.TestCase):
    def test_zero_side(self):
        self.assertEqual(perimeter(0), 0)

    def test_unit_side(self):
        self.assertEqual(perimeter(1), 4)

    def test_integer_side(self):
        self.assertEqual(perimeter(4), 16)

    def test_float_side(self):
        self.assertAlmostEqual(perimeter(1.5), 6.0)

    def test_large_side(self):
        self.assertEqual(perimeter(10**6), 4 * 10**6)


if __name__ == '__main__':
    unittest.main()
