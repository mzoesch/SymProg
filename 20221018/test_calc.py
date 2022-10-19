# test_calc.py is naming convention for test files
# always with _

# Run from console:
# python3 -m unittest testCalc.py
# or use __main__:

import unittest
import whatToTest


class TestCalc(unittest.TestCase):

    def test_add(self):  # Counts as a test
        # result = whatToTest.add(10, 5)
        # self.assertEqual(result, 15)
        self.assertEqual(whatToTest.add(10, 5), 15)
        self.assertEqual(whatToTest.add(-1, 1), 0)
        self.assertEqual(whatToTest.add(-1, -1), -2)  # Ran 1 test in 0.000s

    def test_subtract(self):
        self.assertEqual(whatToTest.subtract(10, 5), 5)
        self.assertEqual(whatToTest.subtract(-1, 1), -2)
        self.assertEqual(whatToTest.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(whatToTest.multiply(10, 5), 50)
        self.assertEqual(whatToTest.multiply(-1, 1), -1)
        self.assertEqual(whatToTest.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(whatToTest.divide(10, 5), 2)
        self.assertEqual(whatToTest.divide(-1, 1), -1)
        self.assertEqual(whatToTest.divide(-1, -1), 1)
        self.assertEqual(whatToTest.divide(5, 2), 2.5)

        # self.assertRaises(ValueError, whatToTest.divide, 10, 0)
        with self.assertRaises(ValueError):
            whatToTest.divide(10, 0)

    def test_divideInt(self):
        self.assertEqual(whatToTest.divideInt(10, 5), 2)
        self.assertEqual(whatToTest.divideInt(-1, 1), -1)
        self.assertEqual(whatToTest.divideInt(-1, -1), 1)
        self.assertEqual(whatToTest.divideInt(5, 2), 2)

        # self.assertRaises(ValueError, whatToTest.divide, 10, 0)
        with self.assertRaises(ValueError):
            whatToTest.divideInt(10, 0)


if __name__ == '__main__':
    unittest.main()
