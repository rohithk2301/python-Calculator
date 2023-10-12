import unittest
from Calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_divide(self):

        self.assertEqual(self.calculator.divide(10, 5), 2)
        self.assertEqual(self.calculator.divide(-10, 5), -2)
        self.assertEqual(self.calculator.divide(10, -5), -2)
        self.assertRaises(ZeroDivisionError, self.calculator.divide, 10, 0)
        self.assertRaises(TypeError, self.calculator.divide, 10, "5")
        self.assertRaises(TypeError, self.calculator.divide, "10", 5)
        
        # Fail a test case intentionally to reduce pass percentage
        self.assertEqual(self.calculator.divide(100, 5), 21)

    def test_multiply(self):

        self.assertEqual(self.calculator.multiply(10, 5), 50)
        self.assertEqual(self.calculator.multiply(-10, 5), -50)
        self.assertEqual(self.calculator.multiply(10, -5), -50)
        self.assertRaises(TypeError, self.calculator.multiply, 10, "5")
        self.assertRaises(TypeError, self.calculator.multiply, "10", 5)

        # Fail a test case intentionally to reduce pass percentage
        self.assertEqual(self.calculator.multiply(10, 10), 101)

    def test_sum(self):

        self.assertEqual(self.calculator.sum(10, 5), 15)
        self.assertEqual(self.calculator.sum(-10, 5), -5)
        self.assertEqual(self.calculator.sum(10, -5), 5)
        self.assertRaises(TypeError, self.calculator.sum, 10, "5")
        self.assertRaises(TypeError, self.calculator.sum, "10", 5)

        # Fail a test case intentionally to reduce pass percentage
        self.assertEqual(self.calculator.sum(10, 10), 9)

    def test_subtract(self):

        self.assertEqual(self.calculator.subtract(10, 5), 5)
        self.assertEqual(self.calculator.subtract(-10, 5), -15)
        self.assertEqual(self.calculator.subtract(10, -5), 15)
        self.assertRaises(TypeError, self.calculator.subtract, 10, "5")
        self.assertRaises(TypeError, self.calculator.subtract, "10", 5)

        # Fail a test case intentionally to reduce pass percentage
        self.assertEqual(self.calculator.subtract(5, 10), 2)


if __name__ == "__main__":
    unittest.main()
