import unittest
from flatten import flatten  

class TestFlatten(unittest.TestCase):

    def test_lista_simple(self):
        lista = [1, 2, 3, 4]
        resultado_esperado = [1, 2, 3, 4]
        self.assertEqual(flatten(lista), resultado_esperado)

    def test_lista_con_listas_anidadas(self):
        lista = [1, [2, 3], [4, [5, 6]]]
        resultado_esperado = [1, 2, 3, 4, 5, 6]
        self.assertEqual(flatten(lista), resultado_esperado)

    def test_lista_con_diferentes_estructuras(self):
        lista = [1, (2, 3), {'a': 4, 'b': 5}, [6, [7, 8]]]
        resultado_esperado = [1, 2, 3, 'a', 4, 'b', 5, 6, 7, 8]
        self.assertEqual(flatten(lista), resultado_esperado)

if __name__ == '__main__':
    unittest.main()
