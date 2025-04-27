def flatten(data):
    """
    Aplana una estructura de datos anidada (listas, tuplas, diccionarios) en una lista plana.
    
    Parámetros:
    data (list, tuple, dict): La estructura de datos que se quiere aplanar.

    Devuelve:
    list: Una lista plana con todos los elementos de la estructura de entrada.
    """
    result = []
    if isinstance(data, list):
        for item in data:
            result.extend(flatten(item))  # Llamada recursiva para aplanar elementos de la lista
    elif isinstance(data, tuple):
        for item in data:
            result.extend(flatten(item))  # Llamada recursiva para aplanar elementos de la tupla
    elif isinstance(data, dict):
        for key, value in data.items():
            result.extend(flatten(value))  # Llamada recursiva para aplanar valores del diccionario
    else:
        result.append(data)  # Agregar elementos no anidados a la lista

    return result
