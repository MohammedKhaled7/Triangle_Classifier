import unittest
from src.triangle_classifier import classify_triangle

class TestTriangleClassifier(unittest.TestCase):

    def test_equilateral(self):
        self.assertEqual(classify_triangle(["1", "1", "1"]), "Equilateral")

    def test_isosceles(self):
        self.assertEqual(classify_triangle(["2", "2", "3"]), "Isosceles")

    def test_scalene(self):
        self.assertEqual(classify_triangle(["3", "4", "5"]), "Scalene")

    def test_no_triangle(self):
        self.assertEqual(classify_triangle(["1", "2", "3"]), "NoTriangle")

    def test_missing_sides(self):
        self.assertEqual(classify_triangle(["1"]), "Error: Two sides missing")

    def test_invalid_input(self):
        self.assertEqual(classify_triangle(["abc", "def", "ghi"]), "Error: Invalid input")

    def test_negative_side(self):
        self.assertEqual(classify_triangle(["-1", "2", "3"]), "Error: Side lengths must be positive")

if __name__ == "__main__":
    unittest.main()
