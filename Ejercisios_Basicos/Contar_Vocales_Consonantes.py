"""
Crear un programa que cuente cuántas vocales y cuántas 
consonantes tiene una frase ingresada por el usuario, 
ignorando espacios, números y signos.
"""
vocales = "aeiou"

def contador(frase): 
    contador_vocales = 0
    contador_consonantes = 0
    
    for letra in frase.lower():
        if letra in vocales:
            contador_vocales += 1
        elif letra.isalpha():
            contador_consonantes += 1
    
    return contador_vocales, contador_consonantes


# Programa principal
entrada = input("Ingresa una frase: ")
v, c = contador(entrada)
print(f"Vocales: {v}, Consonantes: {c}")