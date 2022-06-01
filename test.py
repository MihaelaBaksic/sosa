import math
import unittest
from dodatak_A import OperationsManager


class TestStringMethods(unittest.TestCase):

    def test_zero_division(self):
        
        om = OperationsManager(10.2, 0)
        self.assertTrue(math.isnan(om.perform_division()))
        

    def test_infinity_division(self):
        om = OperationsManager(10.2,float('inf'))
        self.assertEqual(0, om.perform_division())


    def test_circumference_positive(self):
        om = OperationsManager(2, 223)
        self.assertFalse(math.isnan(om.calculate_circumference()))


    def test_circumference_one_negative(self):        
        om = OperationsManager(-2, 223)
        self.assertTrue(math.isnan(om.calculate_circumference()))


    def test_circumference_both_negative(self):        
        om = OperationsManager(-2, -223)
        self.assertTrue(math.isnan(om.calculate_circumference()))

    def test_logarithm_positive(self):
        self.assertEqual(2, OperationsManager.calculate_log(math.e**2))

    def test_logarithm_zero(self):
        self.assertTrue(math.isnan(OperationsManager.calculate_log(0.0)))

    def test_logarithm_negative(self):
        self.assertTrue(math.isnan(OperationsManager.calculate_log(-1)))

    
    
    

if __name__ == '__main__':
    unittest.main()
