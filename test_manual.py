def merge_sort_bidirecional(arr, key=lambda x: x):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort_bidirecional(left, key)
        merge_sort_bidirecional(right, key)

        i, j = 0, 0
        i_rev, j_rev = len(left) - 1, len(right) - 1

        temp = [0] * len(arr)
        front, back = 0, len(arr) - 1

        while front <= back:
            if i <= i_rev and (j > j_rev or key(left[i]) <= key(right[j])):
                temp[front] = left[i]
                i += 1
                front += 1
            elif j <= j_rev:
                temp[front] = right[j]
                j += 1
                front += 1

            if front > back:
                break

            if i_rev >= i and (j_rev < j or key(right[j_rev]) <= key(left[i_rev])):
                temp[back] = left[i_rev]
                i_rev -= 1
                back -= 1
            elif j_rev >= j:
                temp[back] = right[j_rev]
                j_rev -= 1
                back -= 1

        arr[:] = temp

# Testes
def test_numeros():
    nums = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original: {nums}")
    merge_sort_bidirecional(nums)
    print(f"Ordenado: {nums}")
    assert nums == [11, 12, 22, 25, 34, 64, 90]

def test_strings_por_tamanho():
    palavras = ["banana", "maçã", "uva", "pera"]
    print(f"Original: {palavras}")
    merge_sort_bidirecional(palavras, key=len)
    print(f"Ordenado por tamanho: {palavras}")
    assert palavras == ["uva", "pera", "maçã", "banana"]

def test_objetos():
    class Pessoa:
        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade
        def __repr__(self):
            return f"{self.nome}({self.idade})"

    pessoas = [
        Pessoa("João", 25),
        Pessoa("Maria", 30),
        Pessoa("Ana", 20)
    ]
    print(f"Original: {pessoas}")
    merge_sort_bidirecional(pessoas, key=lambda x: x.idade)
    print(f"Ordenado por idade: {pessoas}")
    assert pessoas[0].idade == 20 and pessoas[-1].idade == 30

if __name__ == "__main__":
    print("Executando testes...")
    
    print("\nTeste 1: Ordenação de números")
    test_numeros()
    
    print("\nTeste 2: Ordenação de strings por tamanho")
    test_strings_por_tamanho()
    
    print("\nTeste 3: Ordenação de objetos por idade")
    test_objetos()
    
    print("\nTodos os testes passaram!")
