"""
Bugs sweet_test
Black box tests:
- prueban inputs y outputs
- Unit testing o integration testing
"""

import unittest

def suma(num_1, num_2):
    return num_1 + num_2

class BlackBoxTest(unittest.TestCase):
    
    def test_sum_two_positive(self):
        num_1 = 10
        num_2 = 5

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, 15)
    
    def test_sum_two_negatives(self):
        num_1 = -10
        num_2 = -7

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, -17)

if __name__ == "__main__":
    unittest.main()