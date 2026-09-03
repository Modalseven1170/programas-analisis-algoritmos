import matplotlib.pyplot as plt
import random as rd

def generar(n, min, max):
    algoritmo_1 = [0.001, 0.002, 0.003, 0.004, 0.005]
    algoritmo_2 = [0.002, 0.008, 0.018, 0.032, 0.050]

    plt.plot(n, algoritmo_1, marker="o", label="Selection Sort")
    plt.plot(n, algoritmo_2, marker="o", label="Bubble Sort")
    plt.title("Comparación de algoritmos")
    plt.xlabel("Tamaño de entrada n")
    plt.ylabel("Tiempo de ejecución (s)")
    plt.legend()


n = [100, 200, 300, 400, 500]
generar(n, 0, 1)
plt.show()
