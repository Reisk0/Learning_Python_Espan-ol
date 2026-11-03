"""
Escribe una función que reciba una frase y devuelva la misma frase pero sin ninguna vocal (a, e, i, o, u).
Debe ignorar mayúsculas y minúsculas (eliminar tanto 'a' como 'A').
Los espacios y signos se mantienen.
Si la frase no tiene vocales, se devuelve igual
"""


def sin_vocales(frase): 
    vocales = "aeiouAEIOU"
    resultado = ""
    for caracter in frase:
        if caracter not in vocales:
            resultado += caracter
    return resultado

llamado = sin_vocales("Hola, ¿cómo estás?")
print(llamado)  # Salida: "Hl, ¿cm sts?"