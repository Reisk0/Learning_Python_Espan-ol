"""
El programa genera un número aleatorio entre 1 y 100.
Pide al usuario que ingrese un número.
Si el usuario adivina, muestra un mensaje de victoria y termina.
Si el número ingresado es menor, dice "El número secreto es más alto".
Si es mayor, dice "El número secreto es más bajo".
El juego no termina hasta que el usuario adivine (sin límite de intentos).
Lleva un conteo de cuántos intentos necesitó el usuario.
"""
import random

numero_aleatorio = random.randint(1, 20)
contador_intentos = 0 

while True: 
    try: 
        entrada = int(input("Ingresa un número sin decimales: "))
    except ValueError: 
        print("❌ Ingresa solo números enteros")
        continue

    # Primero verificamos si acertó (así no suma un intento de más)
    if entrada == numero_aleatorio:
        contador_intentos += 1 # Sumamos este último intento ganador
        print(f"🎉 ¡Felicidades! El número aleatorio era {numero_aleatorio}.")
        print(f"📊 Número de intentos: {contador_intentos}")
        break
    elif entrada < numero_aleatorio:
        print("📉 El número secreto es más ALTO.")
        contador_intentos += 1
    else: 
        print("📈 El número secreto es más BAJO.")
        contador_intentos += 1