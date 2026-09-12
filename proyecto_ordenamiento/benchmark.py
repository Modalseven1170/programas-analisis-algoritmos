import random as rd 
import time
import matplotlib.pyplot as plt
import ordenamientos

tiempos_selection_sort=[]
tiempos_bubble_sort=[]
tiempos_insertion_sort=[]
tiempos_gnome_sort=[]


lista= []
listadelistas=[]
def genera(n, min, max):
    return [rd.randint(min, max) for i in range(n)]

lista=genera(30, 1, 100)
print (lista)
listadelistas.append(lista)

lista=genera(50, 1, 100)
print (lista)
listadelistas.append(lista)

print (listadelistas)

numeros = []
Tini_ssort=time.time()
print("Lista ordenada:", ordenamientos.selection_sort(numeros))
Tfin_ssort=time.time()
tiempos_selection_sort.append(Tfin_ssort - Tini_ssort)
print("Tiempos de ejecución (s):", tiempos_selection_sort)

numeros = []
Tini_ssort=time.time()
print("Lista ordenada:", ordenamientos.bubble_sort_brute_force(numeros))
Tfin_ssort=time.time()
tiempos_bubble_sort.append(Tfin_ssort - Tini_ssort)
print("Tiempos de ejecución (s):", tiempos_bubble_sort)

numeros = []
Tini_ssort=time.time()
print("Lista ordenada:", ordenamientos.insertion_sort(numeros))
Tfin_ssort=time.time()
tiempos_insertion_sort.append(Tfin_ssort - Tini_ssort)
print("Tiempos de ejecución (s):", tiempos_insertion_sort)

numeros = []
Tini_ssort=time.time()
print("Lista ordenada:", ordenamientos.gnome_sort(numeros))
Tfin_ssort=time.time()
tiempos_gnome_sort.append(Tfin_ssort - Tini_ssort)
print("Tiempos de ejecución (s):", tiempos_gnome_sort)
