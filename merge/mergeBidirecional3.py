import random
import time
import tracemalloc
import matplotlib.pyplot as plt
import psutil
import os
import gc

def merge_sort_bidirectional(arr):
    """
    Merge Sort utilizando fusão bidirecional.
    Preenche o array simultaneamente da frente (com os menores)
    e de trás (com os maiores).
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort_bidirectional(left)
        merge_sort_bidirectional(right)

        i, j = 0, 0  # Ponteiros para o início das listas
        i_rev, j_rev = len(left) - 1, len(right) - 1  # Ponteiros para o final das listas

        temp = [0] * len(arr)
        front, back = 0, len(arr) - 1  # Posições de preenchimento

        while front <= back:
            if i <= i_rev and (j > j_rev or left[i] <= right[j]):  # Menor elemento na frente
                temp[front] = left[i]
                i += 1
                front += 1
            elif j <= j_rev:
                temp[front] = right[j]
                j += 1
                front += 1

            if front > back:  # Evita sobrescrever se front ultrapassou back
                break

            if i_rev >= i and (j_rev < j or left[i_rev] >= right[j_rev]):  # Maior elemento atrás
                temp[back] = left[i_rev]
                i_rev -= 1
                back -= 1
            elif j_rev >= j:
                temp[back] = right[j_rev]
                j_rev -= 1
                back -= 1

        arr[:] = temp

def merge_sort_temp(arr):
    """
    Merge sort clássico utilizando array temporário para mescla.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort_temp(left)
        merge_sort_temp(right)

        i = j = k = 0
        temp = [0] * len(arr)
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                temp[k] = left[i]
                i += 1
            else:
                temp[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            temp[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            temp[k] = right[j]
            j += 1
            k += 1

        arr[:] = temp

def get_process_memory():
    """Retorna o uso atual de memória em MB."""
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 / 1024

def is_sorted(arr):
    """Verifica se o array está ordenado em ordem crescente."""
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

def test_sort(sort_func, arr):
    """
    Executa a função de ordenação uma vez, medindo tempo e uso de memória.
    """
    gc.collect()  # Força coleta de lixo antes do teste
    arr_copy = arr.copy()
    
    # Início das medições
    process = psutil.Process(os.getpid())
    start_memory = get_process_memory()
    tracemalloc.start()
    
    start_time = time.time()
    start_cpu = process.cpu_percent()
    
    # Execução do algoritmo
    sort_func(arr_copy)
    
    # Coleta das métricas
    end_time = time.time()
    end_cpu = process.cpu_percent()
    current, peak = tracemalloc.get_traced_memory()
    end_memory = get_process_memory()
    tracemalloc.stop()

    # Validação da ordenação
    if not is_sorted(arr_copy):
        print(f"Erro: {sort_func.__name__} não ordenou corretamente!")
        print(f"Entrada: {arr[:20]} ...")
        print(f"Saída incorreta: {arr_copy[:20]} ...")
        return None
    
    if sort_func.__name__ == 'merge_sort_bidirectional':
        print(f"✓ Array ordenado corretamente ({len(arr_copy)} elementos)")

    return {
        'tempo': end_time - start_time,
        'memoria': end_memory - start_memory,
        'cpu': (end_cpu + start_cpu) / 2,
        'memoria_pico': peak / 1024 / 1024  # Convertendo para MB
    }

def run_tests():
    """Executa testes adicionais para verificar casos específicos."""
    test_cases = {
        "Lista Ordenada": list(range(1000)),
        "Lista Reversa": list(range(1000, 0, -1)),
        "Elementos Iguais": [5] * 1000,
        "Lista Pequena Ímpar": [3, 1, 2],
        "Lista Pequena Par": [4, 2, 3, 1],
        "Lista Grande Aleatória": [random.randint(0, 10000) for _ in range(10000)],
        "Lista com Duplicatas": [random.randint(0, 100) for _ in range(1000)],
        "Lista com Números Negativos": [random.randint(-1000, 1000) for _ in range(1000)],
        "Lista com Um Elemento": [1],
        "Lista Vazia": [],
    }
    
    for name, test in test_cases.items():
        print(f"\nTestando: {name}")
        arr_copy = test.copy()
        merge_sort_bidirectional(arr_copy)
        if arr_copy != sorted(test):
            print(f"Erro detectado no caso: {name}")
            print(f"Entrada: {test[:20]} ...")
            print(f"Saída incorreta: {arr_copy[:20]} ...")
            return False
        print(f"{name}: ✓ Passou")
    return True

def plot_performance_comparison(sizes, bi_results, temp_results):
    """Plota gráficos comparativos de performance."""
    metrics = ['tempo', 'memoria', 'cpu', 'memoria_pico']
    titles = ['Tempo de Execução (s)', 'Memória (MB)', 'CPU (%)', 'Memória de Pico (MB)']
    
    plt.figure(figsize=(15, 10))
    for idx, (metric, title) in enumerate(zip(metrics, titles)):
        plt.subplot(2, 2, idx + 1)
        
        bi_metric = [result[metric] for result in bi_results]
        temp_metric = [result[metric] for result in temp_results]
        
        plt.plot(sizes, bi_metric, 'b-o', label='Bidirecional')
        plt.plot(sizes, temp_metric, 'r-o', label='Temporário')
        
        plt.title(title)
        plt.xlabel('Tamanho do Array')
        plt.ylabel(title)
        plt.legend()
        plt.grid(True)
        plt.xscale('log')
    
    plt.tight_layout()
    plt.savefig('merge_sort_performance.png')
    plt.close()

if __name__ == "__main__":
    if not run_tests():
        print("Falha nos testes básicos!")
        exit(1)
    
    print("\nIniciando testes de performance...")
    
    # Tamanhos de array com incremento de 40%
    base_size = 1000
    arr_sizes = []
    current_size = base_size
    
    while current_size <= 1000000:  # Limite máximo de 1 milhão
        arr_sizes.append(current_size)
        current_size = int(current_size * 1.1)  # Aumento de 40%
    
    bi_results = []
    temp_results = []
    
    for size in arr_sizes:
        print(f"\nTestando arrays de tamanho: {size}")
        arr = [random.randint(0, 100000) for _ in range(size)]
        
        print("Testando Merge Sort Bidirecional...")
        bi_metrics = test_sort(merge_sort_bidirectional, arr)
        
        print("Testando Merge Sort com Array Temporário...")
        temp_metrics = test_sort(merge_sort_temp, arr)
        
        if bi_metrics and temp_metrics:
            bi_results.append(bi_metrics)
            temp_results.append(temp_metrics)
            
            print(f"\nResultados para tamanho {size}:")
            print("\nMerge Sort Bidirecional:")
            for metric, value in bi_metrics.items():
                print(f"{metric}: {value:.4f}")
            
            print("\nMerge Sort com Array Temporário:")
            for metric, value in temp_metrics.items():
                print(f"{metric}: {value:.4f}")
            
            # Calcula diferença percentual no tempo
            tempo_diff = ((temp_metrics['tempo'] - bi_metrics['tempo']) 
                         / temp_metrics['tempo'] * 100)
            
            mais_rapido = "Bidirecional" if tempo_diff > 0 else "Temporário"
            print(f"\n{mais_rapido} foi {abs(tempo_diff):.2f}% mais rápido")
    
    # Gera gráficos de performance
    plot_performance_comparison(arr_sizes, bi_results, temp_results)
    print("\nGráficos de performance foram salvos em 'merge_sort_performance.png'")
