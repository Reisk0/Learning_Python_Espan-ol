"""
Escribe una función que reciba dos cosas:
Una lista de palabras.
Una letra.
La función debe devolver cuántas palabras de la lista empiezan con esa letra.
Reglas:
Ignora mayúsculas y minúsculas (busca tanto 'a' como 'A').
Si la lista está vacía, devuelve 0.
"""

def contar_palabras(lista_palabras, letra):
    contador = 0
    letra = letra.lower()

    for palabra in lista_palabras: 
        if palabra.lower().startswith(letra):   # ✅ Corregido
            contador += 1
            
    return contador


entrada = input("Ingresa una frase: ")
lista_palabras = entrada.split()   # ✅ Convierte a lista de palabras

while True: 
    letra = input("Ingresa una letra: ").lower()
    
    # Validar que sea solo 1 letra
    if len(letra) != 1:
        print("❌ Ingresa solo una letra.")
        continue

    llamar_funcion = contar_palabras(lista_palabras, letra)
    print(f"Palabras que empiezan con '{letra}': {llamar_funcion}")
    print("Gracias por usar el programa.")
    break