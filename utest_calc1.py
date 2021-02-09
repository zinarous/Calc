import unittest
from calc_tk import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(self, 1, 2), 3)

    def test_subtract(self):
        self.assertEqual(Calc.subtract(self,4, 2), 2)
        
    def test_multiply(self):
        self.assertEqual(Calc.multiply(self, 2, 5), 10)
        
    def test_divide(self):
        self.assertEqual(Calc.divide(self, 8, 4), 2)

if __name__ == '__main__':
    unittest.main()