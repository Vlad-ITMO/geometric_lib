import unittest

from rectangle import area, perimeter


class TestsRectangleArea(unittest.TestCase):

    def test_area_simple(self):
        self.assertEqual(area(6, 3), 6 * 3)

    def test_area_long(self):
        self.assertEqual(area(567, 98), 567 * 98)

    def test_area_zero(self):
        self.assertRaises(ValueError, lambda: area(0, 5))

    def test_area_negative(self):
        self.assertRaises(ValueError, lambda: area(-4, 34))

    def test_area_char(self):
        self.assertRaises(TypeError, lambda: area('t', 309))


class TestsRectanglePerimeter(unittest.TestCase):

    def test_perimeter_simple(self):
        self.assertEqual(perimeter(3, 2), 2 * (3 + 2))

    def test_perimeter_long(self):
        self.assertEqual(perimeter(234, 843), 2 * (234 + 843))

    def test_perimeter_zero(self):
        self.assertRaises(ValueError, lambda: perimeter(0, 567))

    def test_perimeter_negative(self):
        self.assertRaises(ValueError, lambda: perimeter(-2, 5))

    def test_perimeter_char(self):
        self.assertRaises(TypeError, lambda: perimeter('a', 7))
