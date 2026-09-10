import random as rd 
import time
import matplotlib.pyplot as plt
import benchmark

def grafica():
    algoritmo_1 = []
    algoritmo_2 = []
    algoritmo_3 = []
    algoritmo_4 = []
    n = [30]
    plt.plot(n, algoritmo_1, marker="o", label="Selection Sort")
    #plt.plot(n, algoritmo_2, marker="o", label="Bubble Sort")
    #plt.plot(n, algoritmo_3, marker="o", label="Insertion Sort")
    #plt.plot(n, algoritmo_4, marker="o", label="Gnome Sort")
    #plt.plot(n, algoritmo_4, marker="o", label="Exchange Sort")
    #plt.title("Comparación de algoritmos")
    plt.xlabel("Tamaño de entrada n")
    plt.ylabel("Tiempo de ejecución (s)")
    plt.legend()
    plt.show()
grafica()
