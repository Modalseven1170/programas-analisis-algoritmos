import random as rd 
import time
import matplotlib.pyplot as plt
import benchmark

def grafica():
    #'''
    algoritmo_1 = [3.5400000342633575e-05, 3.9799999285605736e-05, 0.000119099999210448, 0.00010400000064691994, 0.00014729999929841142]
    algoritmo_2 = [3.9799999285605736e-05, 0.00010279999878548551, 0.00019320000137668103, 0.0003233999996155035, 0.0004639999988285126]
    algoritmo_3 = [1.5300000086426735e-05, 3.590000051190145e-05, 6.570000005012844e-05, 8.709999929124024e-05, 0.00013559999933931977]
    algoritmo_4 = [3.229999856557697e-05, 9.489999865763821e-05, 0.00017389999993611127, 0.00022630000057688449, 0.0003935999993700534]
    algoritmo_5 = [2.0600000425474718e-05, 5.149999924469739e-05, 0.0001156999987870222, 0.00014270000065153, 0.0002106000010826392]
    #'''
    algoritmo_6=[0.0014154000000417, 0.003038599999854341, 0.009608699998352677, 0.009081700000024284, 0.024853900000380236]
    n = [30,50,70,90,110]
    #'''
    plt.plot(n, algoritmo_1, marker="o", label="Selection Sort")
    plt.plot(n, algoritmo_2, marker="o", label="Bubble Sort")
    plt.plot(n, algoritmo_3, marker="o", label="Insertion Sort")
    plt.plot(n, algoritmo_4, marker="o", label="Gnome Sort")
    plt.plot(n, algoritmo_5, marker="o", label="Exchange Sort")
    #'''
    plt.plot(n, algoritmo_6, marker="o", label="Stooge Sort")
    plt.title("Comparación de algoritmos")
    plt.xlabel("Tamaño de entrada n")
    plt.ylabel("Tiempo de ejecución (s)")
    plt.legend()
    plt.show()
grafica()
