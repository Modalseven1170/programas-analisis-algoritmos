import random as rd 
import time
import ordenamientos

tiempos_selection_sort=[]
tiempos_bubble_sort=[]
tiempos_insertion_sort=[]
tiempos_gnome_sort=[]
tiempos_exchange_sort=[]
tiempos_stooge_sort=[]

def genera(n, min_val, max_val):
    return [rd.randint(min_val, max_val) for i in range(n)]

tamanos = [30, 50, 70, 90, 110]
listadelistas = []

for n in tamanos:
    lista = genera(n, 1, 100)
    print("\nLista original:", lista)
    listadelistas.append(lista)
    #'''
    numeros = lista.copy()
    Tini_ssort = time.perf_counter()
    resultado_ssort = ordenamientos.selection_sort(numeros)
    Tfin_ssort = time.perf_counter()
    print("Lista ordenada:", resultado_ssort)
    tiempos_selection_sort.append(Tfin_ssort - Tini_ssort)
    print("Tiempos de ejecución (s):", tiempos_selection_sort)

    numeros = lista.copy()
    Tini_bsort = time.perf_counter()
    resultado_bsort = ordenamientos.bubble_sort(numeros)
    Tfin_bsort = time.perf_counter()
    print("Lista ordenada:", resultado_bsort)
    tiempos_bubble_sort.append(Tfin_bsort - Tini_bsort)
    print("Tiempos de ejecución (s):", tiempos_bubble_sort)

    numeros = lista.copy()
    Tini_isort = time.perf_counter()
    resultado_isort = ordenamientos.insertion_sort(numeros)
    Tfin_isort = time.perf_counter()
    print("Lista ordenada:", resultado_isort)
    tiempos_insertion_sort.append(Tfin_isort - Tini_isort)
    print("Tiempos de ejecución (s):", tiempos_insertion_sort)

    numeros = lista.copy()
    Tini_gsort = time.perf_counter()
    resultado_gsort = ordenamientos.gnome_sort(numeros)
    Tfin_gsort = time.perf_counter()
    print("Lista ordenada:", resultado_gsort)
    tiempos_gnome_sort.append(Tfin_gsort - Tini_gsort)
    print("Tiempos de ejecución (s):", tiempos_gnome_sort)

    numeros = lista.copy()
    Tini_esort = time.perf_counter()
    resultado_esort = ordenamientos.exchange_sort(numeros)
    Tfin_esort = time.perf_counter()
    print("Lista ordenada:", resultado_esort)
    tiempos_exchange_sort.append(Tfin_esort - Tini_esort)
    print("Tiempos de ejecución (s):", tiempos_exchange_sort)
    #'''
    numeros = lista.copy()
    Tini_stooge = time.perf_counter()
    resultado_stooge = ordenamientos.stooge_sort(numeros) 
    Tfin_stooge = time.perf_counter()
    print("Lista ordenada (Stooge):", resultado_stooge)
    tiempos_stooge_sort.append(Tfin_stooge - Tini_stooge)
    print("Tiempos de ejecución (s):", tiempos_stooge_sort)