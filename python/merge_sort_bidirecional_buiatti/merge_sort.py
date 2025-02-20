"""
MergeSortBidirecional - Implementação do algoritmo de ordenação Merge Sort Bidirecional.

Este módulo implementa uma variação do algoritmo clássico Merge Sort que realiza
a fusão dos arrays de forma bidirecional, preenchendo simultaneamente as posições
do início (com os menores elementos) e do fim (com os maiores elementos) do array.

Autor: Roberto Buiatti
"""

from typing import List, TypeVar, Callable

T = TypeVar('T')

def merge_sort_bidirecional(
    arr: List[T], 
    key: Callable[[T], T] = lambda x: x
) -> None:
    """
    Ordena um array utilizando o algoritmo Merge Sort Bidirecional.

    Args:
        arr: Lista a ser ordenada
        key: Função opcional que especifica uma chave de ordenação personalizada

    Examples:
        >>> numeros = [64, 34, 25, 12, 22, 11, 90]
        >>> merge_sort_bidirecional(numeros)
        >>> print(numeros)
        [11, 12, 22, 25, 34, 64, 90]

        >>> palavras = ["banana", "maçã", "uva", "pera"]
        >>> merge_sort_bidirecional(palavras, key=len)  # Ordena por tamanho
        >>> print(palavras)
        ['uva', 'pera', 'maçã', 'banana']
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # Ordena recursivamente as sublistas
        merge_sort_bidirecional(left, key)
        merge_sort_bidirecional(right, key)

        # Ponteiros para percorrer as sublistas
        i, j = 0, 0  # Para o início
        i_rev, j_rev = len(left) - 1, len(right) - 1  # Para o final

        temp = [0] * len(arr)
        front, back = 0, len(arr) - 1  # Posições de preenchimento

        while front <= back:
            # Processa elementos pelo início
            if i <= i_rev and (j > j_rev or key(left[i]) <= key(right[j])):
                temp[front] = left[i]
                i += 1
                front += 1
            elif j <= j_rev:
                temp[front] = right[j]
                j += 1
                front += 1

            if front > back:  # Evita sobrescrever valores
                break

            # Processa elementos pelo final
            if i_rev >= i and (j_rev < j or key(left[i_rev]) >= key(right[j_rev])):
                temp[back] = left[i_rev]
                i_rev -= 1
                back -= 1
            elif j_rev >= j:
                temp[back] = right[j_rev]
                j_rev -= 1
                back -= 1

        arr[:] = temp
