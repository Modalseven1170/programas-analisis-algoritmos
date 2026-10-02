import time


def fibonacci(n):
    """Fibonacci con programación dinámica (tabulación bottom-up).
    Cada subproblema se calcula una sola vez: O(n)."""
    if n <= 1:
        return n
    tabla = [0] * (n + 1)
    tabla[1] = 1
    for i in range(2, n + 1):
        tabla[i] = tabla[i - 1] + tabla[i - 2]
    return tabla[n]


if __name__ == "__main__":
    n = int(input("Ingresa el valor de n: "))

    inicio = time.perf_counter()
    resultado = fibonacci(n)
    fin = time.perf_counter()

    print(f"Fibonacci({n}) = {resultado}")
    print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")