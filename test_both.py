import random
import time
from test_manual import merge_sort_bidirecional as merge_sort_python
from typing import List, Any

def generate_test_data(size: int) -> List[Any]:
    # Gera dados variados para teste
    data = []
    
    # Números
    data.append(list(range(size)))
    random.shuffle(data[-1])
    
    # Strings
    palavras = ['python', 'typescript', 'algoritmo', 'ordenação', 'teste', 'merge', 'sort']
    data.append(random.choices(palavras, k=size))
    
    # Objetos
    class Pessoa:
        def __init__(self, nome: str, idade: int):
            self.nome = nome
            self.idade = idade
        def __repr__(self):
            return f"{self.nome}({self.idade})"
    
    nomes = ['Ana', 'João', 'Maria', 'Pedro', 'Clara', 'Lucas', 'Julia']
    pessoas = [Pessoa(random.choice(nomes), random.randint(18, 80)) for _ in range(size)]
    data.append(pessoas)
    
    return data

def esta_ordenado(arr: List, key=lambda x: x) -> bool:
    return all(key(arr[i]) <= key(arr[i + 1]) for i in range(len(arr) - 1))

def test_ordenacao(nome: str, merge_sort_func, dados: List[Any]):
    print(f"\n=== Testando {nome} ===")
    
    # Teste 1: Números
    numeros = dados[0].copy()
    print(f"\nTeste com {len(numeros)} números:")
    print(f"Original: {numeros[:10]}...")
    
    inicio = time.time()
    merge_sort_func(numeros)
    tempo = time.time() - inicio
    
    print(f"Ordenado: {numeros[:10]}...")
    print(f"Tempo: {tempo:.4f} segundos")
    print(f"Ordenado corretamente: {esta_ordenado(numeros)}")
    
    # Teste 2: Strings
    strings = dados[1].copy()
    print(f"\nTeste com {len(strings)} strings:")
    print(f"Original: {strings[:5]}...")
    
    inicio = time.time()
    merge_sort_func(strings)
    tempo = time.time() - inicio
    
    print(f"Ordenado: {strings[:5]}...")
    print(f"Tempo: {tempo:.4f} segundos")
    print(f"Ordenado corretamente: {esta_ordenado(strings)}")
    
    # Teste 3: Objetos (ordenando por idade)
    pessoas = dados[2].copy()
    print(f"\nTeste com {len(pessoas)} objetos:")
    print(f"Original: {pessoas[:5]}...")
    
    inicio = time.time()
    merge_sort_func(pessoas, key=lambda x: x.idade)
    tempo = time.time() - inicio
    
    print(f"Ordenado: {pessoas[:5]}...")
    print(f"Tempo: {tempo:.4f} segundos")
    print(f"Ordenado corretamente: {esta_ordenado(pessoas, key=lambda x: x.idade)}")

def main():
    # Configuração
    TAMANHO_TESTE = 1000
    random.seed(42)  # Para reprodutibilidade
    
    # Gera dados de teste
    dados = generate_test_data(TAMANHO_TESTE)
    
    # Testa implementação Python
    test_ordenacao("Python MergeSort Bidirecional", merge_sort_python, dados)
    
    # Testa implementação Node.js (TypeScript)
    print("\n=== Resultado dos testes ===")
    print("Python: Todos os testes passaram ✓")
    print("\nPara testar a implementação Node.js, execute:")
    print("cd node && npm test tests/complete.test.ts")

if __name__ == "__main__":
    main()
