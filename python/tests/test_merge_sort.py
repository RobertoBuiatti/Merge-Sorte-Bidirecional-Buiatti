"""
Testes unitários para o algoritmo Merge Sort Bidirecional.
"""

import unittest
from merge_sort_bidirecional_buiatti import merge_sort_bidirecional

class TestMergeSortBidirecional(unittest.TestCase):
    def test_ordenacao_numeros(self):
        """Testa ordenação de números inteiros"""
        arr = [64, 34, 25, 12, 22, 11, 90]
        merge_sort_bidirecional(arr)
        self.assertEqual(arr, [11, 12, 22, 25, 34, 64, 90])

    def test_lista_vazia(self):
        """Testa ordenação de lista vazia"""
        arr = []
        merge_sort_bidirecional(arr)
        self.assertEqual(arr, [])

    def test_lista_um_elemento(self):
        """Testa ordenação de lista com um elemento"""
        arr = [1]
        merge_sort_bidirecional(arr)
        self.assertEqual(arr, [1])

    def test_lista_elementos_repetidos(self):
        """Testa ordenação com elementos repetidos"""
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        merge_sort_bidirecional(arr)
        self.assertEqual(arr, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

    def test_ordenacao_strings(self):
        """Testa ordenação de strings"""
        arr = ["banana", "maçã", "uva", "pera"]
        merge_sort_bidirecional(arr)
        self.assertEqual(arr, ["banana", "maçã", "pera", "uva"])

    def test_ordenacao_por_chave(self):
        """Testa ordenação usando função key personalizada"""
        arr = ["banana", "maçã", "uva", "pera"]
        merge_sort_bidirecional(arr, key=len)
        self.assertEqual(arr, ["uva", "pera", "maçã", "banana"])

    def test_ordenacao_objetos(self):
        """Testa ordenação de objetos usando atributo como chave"""
        class Pessoa:
            def __init__(self, nome, idade):
                self.nome = nome
                self.idade = idade
            
            def __eq__(self, other):
                return self.nome == other.nome and self.idade == other.idade

        p1 = Pessoa("João", 25)
        p2 = Pessoa("Maria", 30)
        p3 = Pessoa("Ana", 20)
        
        arr = [p1, p2, p3]
        merge_sort_bidirecional(arr, key=lambda x: x.idade)
        self.assertEqual(arr, [p3, p1, p2])

if __name__ == '__main__':
    unittest.main()
