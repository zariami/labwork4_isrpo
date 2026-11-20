import math
import unittest

from circle import area, perimeter


class CircleAreaTestCase(unittest.TestCase):
    def test_zero_radius(self):
        self.assertEqual(area(0), 0)

    def test_unit_radius(self):
        self.assertAlmostEqual(area(1), math.pi)

    def test_integer_radius(self):
        self.assertAlmostEqual(area(5), 78.5398, places=4)

    def test_float_radius(self):
        self.assertAlmostEqual(area(2.5), 19.6350, places=4)

    def test_large_radius(self):
        self.assertAlmostEqual(area(1000), math.pi * 10**6)

    def test_returns_float(self):
        self.assertIsInstance(area(3), float)


class CirclePerimeterTestCase(unittest.TestCase):
    def test_zero_radius(self):
        self.assertEqual(perimeter(0), 0)

    def test_unit_radius(self):
        self.assertAlmostEqual(perimeter(1), 2 * math.pi)

    def test_integer_radius(self):
        self.assertAlmostEqual(perimeter(5), 31.4159, places=4)

    def test_float_radius(self):
        self.assertAlmostEqual(perimeter(2.5), 15.7080, places=4)

    def test_large_radius(self):
        self.assertAlmostEqual(perimeter(1000), 2000 * math.pi)

    def test_returns_float(self):
        self.assertIsInstance(perimeter(3), float)


if __name__ == '__main__':
    unittest.main()
