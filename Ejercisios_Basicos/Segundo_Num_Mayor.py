"""
Escribe una función que reciba una lista de números y devuelva el segundo número más grande.
Si la lista tiene menos de 2 números, devuelve None.
Si todos los números son iguales, devuelve None.
No uses sort() ni sorted().
"""


def segundo_numero(lista_temporal): 
    # 1. Verificar longitud primero
    if len(lista_temporal) < 2: 
        return None

    # 2. Inicializar con el primer elemento
    numero_mayor = lista_temporal[0]
    segundo_mayor = None

    for num in lista_temporal:
        if num > numero_mayor: 
            # El mayor anterior pasa a ser el segundo
            segundo_mayor = numero_mayor
            numero_mayor = num
        elif num > segundo_mayor and num != numero_mayor:
            # Es un nuevo segundo mayor (diferente al primero)
            segundo_mayor = num

    return segundo_mayor