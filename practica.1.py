import time 
tiempos_bubble_sort=[]
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-1-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

numeros = [147, 227, 234, 168, 967, 872, 259, 605, 686, 812, 60, 535, 256, 286, 718, 124, 757, 64, 71, 288, 774, 648, 524, 229, 893, 75, 779, 509, 409, 21,50, 86, 78, 56, 88, 59, 31, 65, 97, 10, 30, 83, 10, 74, 20, 37, 81, 8, 13, 24,75, 13, 2, 90, 7, 1, 47, 98, 79, 95, 82, 63, 53, 92, 96, 60, 8, 75, 94, 70, 14, 66, 37, 52, 91, 45, 9, 100, 11, 92, 40, 92, 41, 14, 99, 23, 54, 64, 71, 75,85, 76, 81, 93, 18, 64, 96, 95, 47, 9, 97, 73, 38, 46, 4, 11, 42, 89, 88, 3,14, 49, 99, 84, 97, 9, 18, 12, 45, 79, 61, 56, 44, 72, 86, 2, 30, 50, 71, 36]

Tini_ssort=time.time()
print("Lista ordenada:", bubble_sort(numeros))
Tfin_ssort=time.time()
tiempos_bubble_sort.append(Tfin_ssort - Tini_ssort)
print("Tiempos de ejecución (s):", tiempos_bubble_sort)

bubble_sort(numeros)
print("\n")
print ("Lista ordenada:", numeros , "\n")
print ("------------------------------")