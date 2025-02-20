from merge_sort_bidirecional_buiatti import merge_sort_bidirecional

def test_ordenacao_basica():
    arr = [64, 34, 25, 12, 22, 11, 90]
    merge_sort_bidirecional(arr)
    print(f"Array ordenado: {arr}")
    assert arr == [11, 12, 22, 25, 34, 64, 90]

def test_ordenacao_por_chave():
    arr = ["banana", "maçã", "uva", "pera"]
    merge_sort_bidirecional(arr, key=len)
    print(f"Array ordenado por tamanho: {arr}")
    assert arr == ["uva", "pera", "maçã", "banana"]

if __name__ == '__main__':
    print("Executando testes...")
    test_ordenacao_basica()
    test_ordenacao_por_chave()
    print("Todos os testes passaram!")
