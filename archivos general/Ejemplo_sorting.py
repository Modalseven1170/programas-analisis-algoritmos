import random
import time
import matplotlib.pyplot as plt
#temp =[]
t_sort=[]
t_bubble=[]
N=[]
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

def bubble_sort_brute_force(arr):
    n = len(arr)
    # Ciclo externo corre n veces de forma fija
    for i in range(n):
        # Ciclo interno compara elementos adyacentes
        for j in range(0, n - 1):
            if arr[j] > arr[j + 1]:
                # Intercambio de elementos
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def genera(n, min, max):
    temp=[]
    for i in range(n):
        temp.append(random.randint(min,max))
    return (temp)

listas_n=[] #lista de listas para sort
listas_n2=[] #lista de listas para bubble
# Ejemplo de uso
#numeros = [64, 25, 12, 22, 11]
inicio = 20
fin =101
incremento=20

for i in range(inicio,fin,incremento):
    listas_n.append(genera(i,1,100))
    listas_n2.append(genera(i,1,100))
    N.append(i)
    print(i)

#genera(20, 1,100)

for i in listas_n:
    t_ini=time.time()
    print(selection_sort(i))
    t_fin=time.time()
    t_sort.append(t_fin-t_ini)
    
for i in listas_n2:
    t_ini=time.time()
    print(bubble_sort_brute_force(i))
    t_fin=time.time()
    t_bubble.append(t_fin-t_ini)
    
    
print(listas_n)


print(N)
def grafica(N,t_sort,t_bubble):
    plt.plot(N,t_sort)
    plt.plot(N,t_bubble)
    plt.show()


grafica(N,t_sort,t_bubble)
#print("Lista ordenada:", selection_sort(numeros))

