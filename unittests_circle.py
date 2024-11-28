import unittest
import math

from circle import area, perimeter




class TestsCircleArea(unittest.TestCase):
    
    def test_area_simple(self):
        self.assertEqual(area(3), math.pi * 3 * 3)

    def test_area_long(self):
        self.assertEqual(area(72), math.pi * 72 * 72)

    def test_area_zero(self):
        self.assertRaises(ValueError, lambda: area(0))

    def test_area_negative(self):
        self.assertRaises(ValueError, lambda: area(-45))

    def test_area_char(self):
        self.assertRaises(TypeError, lambda: area('a'))


class TestCirclePerimeter(unittest.TestCase):

    def test_perimeter_simple(self):
        self.assertEqual(perimeter(3), 2 * math.pi * 3)

    def test_perimeter_long(self):
        self.assertEqual(perimeter(276), 2 * math.pi * 276)

    def test_perimeter_zero(self):
        self.assertRaises(ValueError, lambda: perimeter(0))

    def test_perimeter_negative(self):
        self.assertRaises(ValueError, lambda: perimeter(-4))

    def test_perimeter_char(self):
        self.assertRaises(TypeError, lambda: perimeter('a'))
