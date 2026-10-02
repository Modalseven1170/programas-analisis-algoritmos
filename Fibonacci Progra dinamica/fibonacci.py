import time


def fibonacci(n):
    """Fibonacci recursivo ingenuo (sin programación dinámica).
    Recalcula los mismos subproblemas muchas veces: O(2^n)."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    n = int(input("Ingresa el valor de n: "))

    inicio = time.perf_counter()
    resultado = fibonacci(n)
    fin = time.perf_counter()

    print(f"Fibonacci({n}) = {resultado}")
    print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")