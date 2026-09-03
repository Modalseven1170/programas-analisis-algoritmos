import time
tiempos_selection_sort=[]
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        # Suponemos que el primer elemento no ordenado es el menor
        min_idx = i
        # Buscamos en el resto de la lista
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Intercambiamos el menor encontrado con el primer elemento actual
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Ejemplo de uso
numeros = [147, 227, 234, 168, 967, 872, 259, 605, 686, 812, 60, 535, 256, 286, 718, 124, 757, 64, 71, 288, 774, 648, 524, 229, 893, 75, 779, 509, 409, 21]
Tini_ssort=time.time()
print("Lista ordenada:", selection_sort(numeros))
Tfin_ssort=time.time()
tiempos_selection_sort.append(Tfin_ssort - Tini_ssort)
print("Tiempos de ejecución (s):", tiempos_selection_sort)