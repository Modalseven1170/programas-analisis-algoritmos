import time 
tiempos_bubble_sort=[]
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-1-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

#numeros = [147, 227, 234, 168, 967, 872, 259, 605, 686, 812, 60, 535, 256, 286, 718, 124, 757, 64, 71, 288, 774, 648, 524, 229, 893, 75, 779, 509, 409, 21]
numeros = [147, 227, 234, 168, 967, 872, 259, 605, 686, 812, 60, 535, 256, 286, 718, 124, 757, 64, 71, 288, 774, 648, 524, 229, 893, 75, 779, 509, 409, 21, 147, 227, 234, 168, 967, 872, 259, 605, 686, 812, 60, 535, 256, 286, 718, 124, 757, 64, 71, 288, 774, 648, 524, 229, 893, 75, 779, 509, 409, 21]

Tini_ssort=time.time()
print("Lista ordenada:", bubble_sort(numeros))
Tfin_ssort=time.time()
tiempos_bubble_sort.append(Tfin_ssort - Tini_ssort)
print("Tiempos de ejecución (s):", tiempos_bubble_sort)

bubble_sort(numeros)
print("\n")
print ("Lista ordenada:", numeros , "\n")
print ("------------------------------")