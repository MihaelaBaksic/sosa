from math import isnan
import unittest
from dodatak_A import OperationsManager


class TestStringMethods(unittest.TestCase):

    def test_zero_division(self):
        
        om = OperationsManager(10.2, 0)
        self.assertTrue(isnan(om.perform_division()))
        

    def test_infiniti_division(self):
        om = OperationsManager(10.2,float('inf'))
        self.assertEquals(0, om.perform_division())


    def test_circumference_positive(self):
        om = OperationsManager(2, 223)
        self.assertFalse(isnan(om.calculate_circumference()))


    def test_circumference_one_negative(self):        
        om = OperationsManager(-2, 223)
        self.assertTrue(isnan(om.calculate_circumference()))


    def test_circumference_both_negative(self):        
        om = OperationsManager(-2, -223)
        self.assertTrue(isnan(om.calculate_circumference()))

    


if __name__ == '__main__':
    unittest.main()
