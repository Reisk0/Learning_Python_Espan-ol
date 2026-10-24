"""
🎯 Enunciado
Escribe una función que reciba una cadena de texto (string) y devuelva la misma cadena pero invertida.
Regla especial: NO puedes usar el truco de Python [::-1] ni la función reversed(). Tienes que hacerlo usando un bucle.
"""

def invertir_cadena(texto): 
    frase_invertida = ""

    for letra in texto: 
        frase_invertida = letra + frase_invertida
        
    return frase_invertida

while True:
    frase = input("Ingresa una frase: ")
    
    # Validar que no esté vacía (opcional)
    if frase == "":
        print("❌ Ingresa una frase válida.")
        continue
    
    llamar_funcion = invertir_cadena(frase) 
    print(f"Frase invertida: {llamar_funcion}")
    break
"""
"Para invertir una cadena sin [::-1], recorre las letras de izquierda a derecha y agrega cada letra al PRINCIPIO del resultado."
"""