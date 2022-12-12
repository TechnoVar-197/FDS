from operator import truediv
import unittest
breakpoint()

class TestArithmetic(unittest.TestCase):
    # test function to test equality of two value
    def Add(self, a, b):
        a = 20
        b = 10

        # error message in case if test case got failed
        # assertEqual() to check equality of first & second value
        self.assertEqual(a + b, 30, "Should be 30")
        if (a + b) == 30:
            x = True
        self.assertTrue(x, "Should be true")

    def subtrac(self):
        a = 25
        b = 15

        self.assertEqual(a - b, 10, "Should be 10")

    def multiply(self):
        a = 10
        b = 20
        self.assertEqual(a * b, 200, "should be 200")

    def division(self):
        a = 20
        b = 10
        self.assertEqual(a / b, 2, "Should be 2")


if __name__ == '__main__':
    unittest.main()