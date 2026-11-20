import unittest

from rectangle import area, perimeter


class RectangleAreaTestCase(unittest.TestCase):
    def test_zero_mul(self):
        self.assertEqual(area(10, 0), 0)

    def test_both_zero(self):
        self.assertEqual(area(0, 0), 0)

    def test_square_mul(self):
        self.assertEqual(area(10, 10), 100)

    def test_different_sides(self):
        self.assertEqual(area(4, 5), 20)

    def test_commutative(self):
        self.assertEqual(area(3, 7), area(7, 3))

    def test_float_sides(self):
        self.assertAlmostEqual(area(2.5, 4.2), 10.5)

    def test_large_values(self):
        self.assertEqual(area(10**6, 10**6), 10**12)


class RectanglePerimeterTestCase(unittest.TestCase):
    def test_zero_sides(self):
        self.assertEqual(perimeter(0, 0), 0)

    def test_one_side_zero(self):
        self.assertEqual(perimeter(10, 0), 20)

    def test_square_sides(self):
        self.assertEqual(perimeter(10, 10), 40)

    def test_different_sides(self):
        self.assertEqual(perimeter(4, 5), 18)

    def test_commutative(self):
        self.assertEqual(perimeter(3, 7), perimeter(7, 3))

    def test_float_sides(self):
        self.assertAlmostEqual(perimeter(2.5, 4.2), 13.4)


if __name__ == '__main__':
    unittest.main()
