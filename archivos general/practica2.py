import matplotlib.pyplot as plt
import random as rd

def generar(n, min, max):
    algoritmo_1 = [0.0, 0.0010018348693847656, 0.0, 0.0009751319885253906, 0.0]
    algoritmo_2 = [0.002063274383544922, 0.0009036064147949219, 0.0009953975677490234, 0.0010013580322265625, 0.0009975433349609375]

    plt.plot(n, algoritmo_1, marker="o", label="Selection Sort")
    plt.plot(n, algoritmo_2, marker="o", label="Bubble Sort")
    plt.title("Comparación de algoritmos")
    plt.xlabel("Tamaño de entrada n")
    plt.ylabel("Tiempo de ejecución (s)")
    plt.legend()


n = [100, 200, 300, 400, 500]
generar(n, 0, 1)
plt.show()
