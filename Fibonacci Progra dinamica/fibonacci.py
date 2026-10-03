import time


def fibonacci(n):
    """Fibonacci recursivo ingenuo (sin programación dinámica).
    Recalcula los mismos subproblemas muchas veces: O(2^n) en tiempo."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def profundidad_maxima(n):
    """Misma recursión, pero registra la profundidad máxima de la pila
    de llamadas. Ese es el espacio que usa la versión recursiva: O(n)."""
    maxima = 0

    def aux(k, nivel):
        nonlocal maxima
        maxima = max(maxima, nivel)
        if k <= 1:
            return k
        return aux(k - 1, nivel + 1) + aux(k - 2, nivel + 1)

    aux(n, 1)
    return maxima


if __name__ == "__main__":
    n = int(input("Ingresa el valor de n: "))

    # 1) Medir el tiempo con la función original
    inicio = time.perf_counter()
    resultado = fibonacci(n)
    fin = time.perf_counter()

    # 2) Medir el espacio: profundidad máxima de la pila de llamadas
    profundidad = profundidad_maxima(n)

    print(f"Fibonacci({n}) = {resultado}")
    print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")
    print(f"Espacio usado (pila de recursión): {profundidad} llamadas anidadas como máximo")
    print("Complejidad de espacio: O(n)")