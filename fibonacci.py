def fibonacci_iterativo(n):
    """
    Calcula el n-ésimo número de Fibonacci de manera iterativa.

    Parámetros:
    n (int): El índice del número de Fibonacci a calcular.

    Retorna:
    int: El n-ésimo número de Fibonacci.

    Levanta:
    ValueError: Si n es negativo.
    """
    if n < 0:
        raise ValueError("El índice no puede ser negativo.")
    
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def fibonacci_recursivo(n):
    """
    Calcula el n-ésimo número de Fibonacci de manera recursiva.

    Parámetros:
    n (int): El índice del número de Fibonacci a calcular.

    Retorna:
    int: El n-ésimo número de Fibonacci.

    Levanta:
    ValueError: Si n es negativo.
    """
    if n < 0:
        raise ValueError("El índice no puede ser negativo.")
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)
