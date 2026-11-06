"""
Escribe una función que reciba una frase y devuelva una lista con las palabras que se repiten (es decir, que aparecen más de una vez).
Ignora mayúsculas y minúsculas ("Hola" y "hola" son la misma palabra).
Ignora los signos de puntuación (,, ., !, ?).
La lista resultante no debe tener duplicados (cada palabra repetida aparece una sola vez).
Mantén el orden en que aparecen en la frase original.
"""



def frases_repetidas(frase_temporal): 
    repeticiones = []
    
    # ✅ Limpiar la frase
    frase_temporal = frase_temporal.lower()
    frase_temporal = frase_temporal.replace(",", "").replace(".", "").replace("!", "").replace("?", "")
    frase_dividida = frase_temporal.split()
    
    for palabra in frase_dividida: 
        if frase_dividida.count(palabra) > 1 and palabra not in repeticiones:
            repeticiones.append(palabra)
            
    return repeticiones


entrada = input("Ingresa una frase entera: ")

llamar_funcion = frases_repetidas(entrada)
print(llamar_funcion)


"""
def frases_repetidas(frase_temporal): 
    # Lista donde guardaremos las palabras que encontremos repetidas.
    # Usamos una lista porque mantiene el orden en que aparecen.
    repeticiones = []
    
    # 1. Limpiamos la frase: convertimos todo a minúsculas para que 
    # "Hola" y "hola" se consideren la misma palabra.
    frase_temporal = frase_temporal.lower()
    
    # 2. Quitamos los signos de puntuación comunes reemplazándolos por "nada" ("").
    frase_temporal = frase_temporal.replace(",", "").replace(".", "").replace("!", "").replace("?", "")
    
    # 3. Dividimos la frase limpia en una lista de palabras separadas por espacios.
    frase_dividida = frase_temporal.split()
    
    # 4. Recorremos la lista de palabras una por una.
    for palabra in frase_dividida: 
        
        # AQUÍ ESTÁ LA MAGIA. Esta condición tiene dos partes unidas por "and":
        #
        # PARTE 1: frase_dividida.count(palabra) > 1
        #   - .count() cuenta cuántas veces aparece esa palabra exacta en la lista.
        #   - > 1 significa "si aparece más de una vez" (es decir, si está repetida).
        #
        # PARTE 2: palabra not in repeticiones
        #   - Pregunta si la palabra NO está todavía en nuestra lista de resultados.
        #   - Si no está, significa que es la primera vez que la encontramos repetida.
        #   - Esto evita que si una palabra aparece 5 veces, la guardemos 5 veces.
        #
        # El "and" exige que AMBAS condiciones sean verdaderas para entrar al if.
        if frase_dividida.count(palabra) > 1 and palabra not in repeticiones:
            
            # Si la palabra está repetida Y no la teníamos guardada, la agregamos.
            repeticiones.append(palabra)
            
    # Finalmente, devolvemos la lista con las palabras repetidas (sin duplicados).
    return repeticiones
"""