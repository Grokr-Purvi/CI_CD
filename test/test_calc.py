import unittest
from src.main import add, subtract, multiply


class TestCalc(unittest.TestCase):

    def test_add(self):
        a=10
        b=20
        expected = 30
        actual = add(a,b)
        self.assertEqual(expected, actual)

    def test_subtract(self):
        a=10
        b=20
        expected = -10
        actual = subtract(a,b)
        self.assertEqual(expected, actual)

    def test_multiply(self):
        a=10
        b=20
        expected = 200
        actual = multiply(a,b)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()

