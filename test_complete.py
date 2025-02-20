def test_merge_sort_bidirecional():
    """
    Função para testar exaustivamente a implementação do Merge Sort Bidirecional.
    """
    print("=== Testes Completos do Merge Sort Bidirecional ===\n")

    # Caso 1: Números inteiros
    nums = [64, 34, 25, 12, 22, 11, 90]
    nums_ordenados = sorted(nums)  # Para comparação
    merge_sort_bidirecional(nums)
    print(f"Teste 1 - Números inteiros:")
    print(f"Esperado: {nums_ordenados}")
    print(f"Obtido:   {nums}")
    print(f"Resultado: {'✓' if nums == nums_ordenados else '✗'}\n")

    # Caso 2: Números repetidos
    nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    nums_ordenados = sorted(nums)
    merge_sort_bidirecional(nums)
    print(f"Teste 2 - Números repetidos:")
    print(f"Esperado: {nums_ordenados}")
    print(f"Obtido:   {nums}")
    print(f"Resultado: {'✓' if nums == nums_ordenados else '✗'}\n")

    # Caso 3: Strings
    palavras = ["banana", "maçã", "uva", "pera"]
    palavras_ordenadas = sorted(palavras)
    merge_sort_bidirecional(palavras)
    print(f"Teste 3 - Strings:")
    print(f"Esperado: {palavras_ordenadas}")
    print(f"Obtido:   {palavras}")
    print(f"Resultado: {'✓' if palavras == palavras_ordenadas else '✗'}\n")

    # Caso 4: Strings por tamanho
    palavras = ["banana", "maçã", "uva", "pera"]
    palavras_ordenadas = sorted(palavras, key=len)
    merge_sort_bidirecional(palavras, key=len)
    print(f"Teste 4 - Strings por tamanho:")
    print(f"Esperado: {palavras_ordenadas}")
    print(f"Obtido:   {palavras}")
    print(f"Resultado: {'✓' if palavras == palavras_ordenadas else '✗'}\n")

    # Caso 5: Lista vazia
    vazia = []
    merge_sort_bidirecional(vazia)
    print(f"Teste 5 - Lista vazia:")
    print(f"Esperado: []")
    print(f"Obtido:   {vazia}")
    print(f"Resultado: {'✓' if vazia == [] else '✗'}\n")

    # Caso 6: Lista com um elemento
    um_elemento = [42]
    merge_sort_bidirecional(um_elemento)
    print(f"Teste 6 - Um elemento:")
    print(f"Esperado: [42]")
    print(f"Obtido:   {um_elemento}")
    print(f"Resultado: {'✓' if um_elemento == [42] else '✗'}\n")

    # Caso 7: Objetos complexos
    class Pessoa:
        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade
        def __repr__(self):
            return f"{self.nome}({self.idade})"
        def __eq__(self, other):
            return self.nome == other.nome and self.idade == other.idade

    pessoas = [
        Pessoa("João", 25),
        Pessoa("Maria", 30),
        Pessoa("Ana", 20),
        Pessoa("Pedro", 35),
        Pessoa("Clara", 28)
    ]
    pessoas_ordenadas = sorted(pessoas, key=lambda x: x.idade)
    merge_sort_bidirecional(pessoas, key=lambda x: x.idade)
    print(f"Teste 7 - Objetos:")
    print(f"Esperado: {pessoas_ordenadas}")
    print(f"Obtido:   {pessoas}")
    print(f"Resultado: {'✓' if [p.idade for p in pessoas] == [p.idade for p in pessoas_ordenadas] else '✗'}\n")

if __name__ == "__main__":
    from test_manual import merge_sort_bidirecional
    test_merge_sort_bidirecional()
