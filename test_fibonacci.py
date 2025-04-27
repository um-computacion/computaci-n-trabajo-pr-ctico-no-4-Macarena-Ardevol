import unittest
from fibonacci import fibonacci_iterativo, fibonacci_recursivo

class TestFibonacci(unittest.TestCase):
    
    def test_fibonacci_iterativo(self):
        # Casos de prueba para la versión iterativa
        self.assertEqual(fibonacci_iterativo(0), 0)
        self.assertEqual(fibonacci_iterativo(1), 1)
        self.assertEqual(fibonacci_iterativo(5), 5)
        self.assertEqual(fibonacci_iterativo(10), 55)
    
    def test_fibonacci_recursivo(self):
        # Casos de prueba para la versión recursiva
        self.assertEqual(fibonacci_recursivo(0), 0)
        self.assertEqual(fibonacci_recursivo(1), 1)
        self.assertEqual(fibonacci_recursivo(5), 5)
        self.assertEqual(fibonacci_recursivo(10), 55)
        
    def test_fibonacci_invalid_input(self):
        # Casos de prueba para entradas inválidas
        with self.assertRaises(ValueError):
            fibonacci_iterativo(-1)
        with self.assertRaises(ValueError):
            fibonacci_recursivo(-1)
