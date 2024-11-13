import unittest

from square import area, perimeter


class TestsSquareArea(unittest.TestCase):

    def test_area_simple(self):
        self.assertEqual(area(4), 4 * 4)

    def test_area_long(self):
        self.assertEqual(area(308), 308 * 308)

    def test_area_zero(self):
        self.assertRaises(ValueError, lambda: area(0))

    def test_area_negative(self):
        self.assertRaises(ValueError, lambda: area(-28))

    def test_area_char(self):
        self.assertRaises(TypeError, lambda: area('w'))


class TestsSquarePerimeter(unittest.TestCase):

    def test_perimeter_simple(self):
        self.assertEqual(perimeter(7), 7 * 4)

    def test_perimeter_long(self):
        self.assertEqual(perimeter(398), 398 * 4)

    def test_perimeter_zero(self):
        self.assertRaises(ValueError, lambda: perimeter(0))

    def test_perimeter_negative(self):
        self.assertRaises(ValueError, lambda: perimeter(-9))

    def test_perimeter_char(self):
        self.assertRaises(TypeError, lambda: perimeter('v'))
