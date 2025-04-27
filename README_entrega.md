Trabajo Práctico 4 - Macarena Ardebol
Descripción del problema:
Este proyecto consiste en la implementación de tres funcionalidades en Python:

Factorial (versión iterativa y recursiva)
Fibonacci (versión iterativa y recursiva)
Aplanar listas (función recursiva para listas anidadas)

Cada funcionalidad incluye sus respectivos casos de prueba utilizando unittest.

Instrucciones de ejecución:
Requisitos:

-Python 3.x
-Librería unittest (incluida en la biblioteca estándar de Python)

Pasos para ejecutar los tests:

-Abrir Visual Studio Code o cualquier editor de código compatible.
-Abrir una terminal dentro del proyecto.

Ejecutar los siguientes comandos, según el archivo de test que se quiera probar:
python -m unittest test_factorial.py
python -m unittest test_fibonacci.py
python -m unittest test_flatten.py

Ejemplos de uso:

Factorial
from factorial import factorial_iterativo, factorial_recursivo
factorial_iterativo(5)  # Resultado: 120
factorial_recursivo(5)  # Resultado: 120

Fibonacci
from fibonacci import fibonacci_iterativo, fibonacci_recursivo
fibonacci_iterativo(6)  # Resultado: 8
fibonacci_recursivo(6)  # Resultado: 8

Flatten (Aplanar listas)
from flatten import flatten
flatten([1, [2, 3], [4, [5, 6]]])  
# Resultado: [1, 2, 3, 4, 5, 6]