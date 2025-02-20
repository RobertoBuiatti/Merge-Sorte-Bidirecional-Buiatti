import random
import time
import tracemalloc

def merge_sort_bidirectional(arr):
    """
    Merge sort utilizando a fusão bidirecional: 
    preenche o array resultado simultaneamente da frente (com os menores)
    e de trás (com os maiores).
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort_bidirectional(left)
        merge_sort_bidirectional(right)
        
        # Ponteiros para a fusão:
        i = 0             # início de left
        j = 0             # início de right
        i_rev = len(left) - 1   # fim de left
        j_rev = len(right) - 1  # fim de right
        
        temp = [0] * len(arr)
        front = 0         # índice para o início do array final
        back = len(arr) - 1  # índice para o final do array final
        
        # Enquanto não se encontrarem:
        while front < back:
            # Fusão da frente: pega o menor entre left[i] e right[j]
            if i <= i_rev and (j > j_rev or left[i] <= right[j]):
                temp[front] = left[i]
                i += 1
            elif j <= j_rev:
                temp[front] = right[j]
                j += 1
            front += 1
            
            # Fusão de trás: pega o maior entre left[i_rev] e right[j_rev]
            if i_rev >= i and (j_rev < j or left[i_rev] >= right[j_rev]):
                temp[back] = left[i_rev]
                i_rev -= 1
            elif j_rev >= j:
                temp[back] = right[j_rev]
                j_rev -= 1
            back -= 1
        
        # Se front == back, resta um elemento (caso tamanho ímpar)
        if front == back:
            if i <= i_rev and (j > j_rev or left[i] <= right[j]):
                temp[front] = left[i]
            elif j <= j_rev:
                temp[front] = right[j]
        
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

def test_sort(sort_func, arr):
    """
    Executa a função de ordenação, medindo o tempo de execução e o uso de memória.
    """
    tracemalloc.start()
    start_time = time.time()
    sort_func(arr)
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return end_time - start_time, current, peak

if __name__ == "__main__":
    # Gerando um array aleatório para teste
    arr_size = 10000
    arr_original = [random.randint(0, 100000) for _ in range(arr_size)]
    
    # Cria cópias para testar ambas as versões com o mesmo array
    arr_bidirectional = arr_original.copy()
    arr_temp = arr_original.copy()
    
    time_bi, current_bi, peak_bi = test_sort(merge_sort_bidirectional, arr_bidirectional)
    time_temp, current_temp, peak_temp = test_sort(merge_sort_temp, arr_temp)
    
    print("Merge Sort Bidirectional:")
    print("Tempo: {:.6f} s, Memória Atual: {} bytes, Pico de Memória: {} bytes".format(
        time_bi, current_bi, peak_bi))
    
    print("\nMerge Sort com Array Temporário:")
    print("Tempo: {:.6f} s, Memória Atual: {} bytes, Pico de Memória: {} bytes".format(
        time_temp, current_temp, peak_temp))
