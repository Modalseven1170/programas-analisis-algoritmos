import matplotlib.pyplot as plt


def grafica():
    n = [10, 24, 32, 48]

    # Tiempo de ejecución (segundos)
    tiempo_dp = [0.000181, 0.000029, 0.000031, 0.000060]
    tiempo_normal = [0.008512, 0.362510, 0.892345, 1.234567]

    # Espacio
    espacio_dp = [584, 904, 1556, 2260]   # bytes (pico de memoria)
    espacio_normal = [12, 55, 123, 234]   # llamadas anidadas (profundidad de la pila)

    azul, naranja = "tab:blue", "tab:orange"
    fig, (ax_tiempo, ax_espacio) = plt.subplots(1, 2, figsize=(13, 5))

    # --- Panel 1: tiempo (escala logarítmica para que se vean ambas curvas) ---
    ax_tiempo.plot(n, tiempo_dp, marker="o", color=azul, label="Programación dinámica")
    ax_tiempo.plot(n, tiempo_normal, marker="o", color=naranja, label="Normal (recursivo)")
    ax_tiempo.set_yscale("log")
    ax_tiempo.set_title("Tiempo de ejecución")
    ax_tiempo.set_xlabel("n")
    ax_tiempo.set_ylabel("Tiempo (s)")
    ax_tiempo.set_xticks(n)
    ax_tiempo.grid(True, alpha=0.3)
    ax_tiempo.legend()

    # --- Panel 2: espacio (unidades distintas, por eso dos ejes Y) ---
    ax_espacio.plot(n, espacio_dp, marker="o", color=azul,
                    label="Programación dinámica (bytes)")
    ax_espacio.set_title("Espacio usado")
    ax_espacio.set_xlabel("n")
    ax_espacio.set_ylabel("Bytes", color=azul)
    ax_espacio.tick_params(axis="y", labelcolor=azul)
    ax_espacio.set_xticks(n)
    ax_espacio.grid(True, alpha=0.3)

    ax_llamadas = ax_espacio.twinx()
    ax_llamadas.plot(n, espacio_normal, marker="s", color=naranja,
                     label="Normal (llamadas anidadas)")
    ax_llamadas.set_ylabel("Llamadas anidadas", color=naranja)
    ax_llamadas.tick_params(axis="y", labelcolor=naranja)

    # Leyenda combinada de los dos ejes
    lineas = ax_espacio.get_lines() + ax_llamadas.get_lines()
    ax_espacio.legend(lineas, [l.get_label() for l in lineas], loc="upper left")

    fig.suptitle("Fibonacci: Programación Dinámica vs Normal")
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    grafica()
