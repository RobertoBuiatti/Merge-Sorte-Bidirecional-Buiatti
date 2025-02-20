import random
import time
import tracemalloc
import matplotlib.pyplot as plt

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

        arr[:] = temp  # Copia os elementos ordenados de volta para o array original

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

def test_sort(sort_func, arr, runs=5):
    """
    Executa a função de ordenação várias vezes, medindo tempo médio e uso de memória.
    """
    times = []
    memory_usages = []

    for _ in range(runs):
        arr_copy = arr.copy()
        tracemalloc.start()
        start_time = time.time()
        sort_func(arr_copy)
        end_time = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        if arr_copy != sorted(arr):
            print(f"Erro: {sort_func.__name__} não ordenou corretamente!")
            print(f"Entrada: {arr[:20]} ...")
            print(f"Saída incorreta: {arr_copy[:20]} ...")
            exit(1)  # Sai do programa se houver erro

        times.append(end_time - start_time)
        memory_usages.append(peak)

    return sum(times) / runs, sum(memory_usages) / runs

def run_tests():
    """Executa testes adicionais para verificar falhas no merge_sort_bidirectional."""
    test_cases = {
        "Lista Ordenada": list(range(1000)),
        "Lista Reversa": list(range(1000, 0, -1)),
        "Elementos Iguais": [5] * 1000,
        "Lista Pequena Ímpar": [3, 1, 2],
        "Lista Pequena Par": [4, 2, 3, 1],
        "Lista Grande Aleatória": [random.randint(0, 10000) for _ in range(10000)],
    }
    
    for name, test in test_cases.items():
        arr_copy = test.copy()
        merge_sort_bidirectional(arr_copy)
        if arr_copy != sorted(test):
            print(f"Erro detectado no caso: {name}")
            print(f"Entrada: {test[:20]} ...")
            print(f"Saída incorreta: {arr_copy[:20]} ...")
            exit(1)
    print("Todos os testes passaram!")

if __name__ == "__main__":
    run_tests()
    arr_sizes = [10**i for i in range(2, 7)]  # 10^2, 10^3, 10^4, 10^5, 10^6
    results = []

    for size in arr_sizes:
        arr = [random.randint(0, 100000) for _ in range(size)]

        time_bi, memory_bi = test_sort(merge_sort_bidirectional, arr)
        time_temp, memory_temp = test_sort(merge_sort_temp, arr)

        faster_percentage = (
            ((time_temp - time_bi) / time_temp) * 100
            if time_temp > time_bi
            else ((time_bi - time_temp) / time_bi) * 100
        )
        faster_algo = "Bidirectional" if time_bi < time_temp else "Temp Array"

        print(f"\nArray Size: {size}")
        print("Merge Sort Bidirectional:")
        print(f"Tempo Médio: {time_bi:.6f} s, Memória Média: {memory_bi:.2f} bytes")

        print("Merge Sort com Array Temporário:")
        print(f"Tempo Médio: {time_temp:.6f} s, Memória Média: {memory_temp:.2f} bytes")

        print(f"{faster_algo} foi mais rápido por {faster_percentage:.2f}%")
        results.append((size, time_bi, time_temp))

    sizes, times_bi, times_temp = zip(*results)

    plt.figure(figsize=(10, 5))
    plt.plot(sizes, times_bi, label="Merge Sort Bidirectional", marker="o")
    plt.plot(sizes, times_temp, label="Merge Sort com Array Temporário", marker="s")
    plt.xlabel("Tamanho do Array")
    plt.ylabel("Tempo Médio (s)")
    plt.title("Comparação de Tempo entre Algoritmos de Merge Sort")
    plt.legend()
    plt.xscale("log")
    plt.grid(True)
    plt.show()