import random as rd 
import time
import matplotlib.pyplot as plt

def grafica():
    #'''
    algoritmo_1 = [3.5400000342633575e-05, 3.9799999285605736e-05, 0.000119099999210448, 0.00010400000064691994, 0.00014729999929841142]
    algoritmo_2 = [3.9799999285605736e-05, 0.00010279999878548551, 0.00019320000137668103, 0.0003233999996155035, 0.0004639999988285126]



    n = [30,50,70,90,110]
    
    plt.plot(n, algoritmo_1, marker="o", label="Selection Sort")
    plt.plot(n, algoritmo_2, marker="o", label="Bubble Sort")
    
    plt.title("Comparación de algoritmos")
    plt.xlabel("Tamaño de entrada n")
    plt.ylabel("Tiempo de ejecución (s)")
    plt.legend()
    plt.show()
grafica()
