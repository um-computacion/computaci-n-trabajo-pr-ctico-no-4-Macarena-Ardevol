import unittest
from factorial import factorial_iterativo, factorial_recursivo

class TestFactorial(unittest.TestCase):

    def test_factorial_iterativo_caso_base(self):
        self.assertEqual(factorial_iterativo(0), 1)
        self.assertEqual(factorial_iterativo(1), 1)

    def test_factorial_iterativo_caso_general(self):
        self.assertEqual(factorial_iterativo(5), 120)
        self.assertEqual(factorial_iterativo(3), 6)

    def test_factorial_iterativo_negativo(self):
        with self.assertRaises(ValueError):
            factorial_iterativo(-5)

    def test_factorial_recursivo_caso_base(self):
        self.assertEqual(factorial_recursivo(0), 1)
        self.assertEqual(factorial_recursivo(1), 1)

    def test_factorial_recursivo_caso_general(self):
        self.assertEqual(factorial_recursivo(5), 120)
        self.assertEqual(factorial_recursivo(3), 6)

    def test_factorial_recursivo_negativo(self):
        with self.assertRaises(ValueError):
            factorial_recursivo(-5)

if __name__ == '__main__':
    unittest.main()
