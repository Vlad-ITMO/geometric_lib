import unittest

from triangle import area, perimeter


class TestsTriangleArea(unittest.TestCase):

    def test_area_simple(self):
        self.assertEqual(area(4, 1), 4 * 1 / 2)

    def test_area_long(self):
        self.assertEqual(area(35, 984), 35 * 984 / 2)

    def test_area_zero(self):
        self.assertRaises(ValueError, lambda: area(0, 6))

    def test_area_negative(self):
        self.assertRaises(ValueError, lambda: area(-78, 567))

    def test_area_char(self):
        self.assertRaises(TypeError, lambda: area('a', 857))
        

class TestsTrianglePerimeter(unittest.TestCase):

    def test_perimeter_simple(self):
        self.assertEqual(perimeter(6, 5, 7), 6 + 5 + 7)

    def test_perimeter_long(self):
        self.assertEqual(perimeter(46, 58, 48), 46 + 58 + 48)

    def test_perimeter_zero(self):
        self.assertRaises(ValueError, lambda: perimeter(0, 4, 2))

    def test_perimeter_negative(self):
        self.assertRaises(ValueError, lambda: perimeter(-2, 35, 46))

    def test_perimeter_char(self):
        self.assertRaises(TypeError, lambda: perimeter('a', 53, 242))



