"""
Escribe un programa que genere una contraseña aleatoria y segura.
Requisitos:
Debe pedir al usuario la longitud deseada (ej: 12 caracteres).
La contraseña debe incluir al menos:
1 letra mayúscula
1 letra minúscula
1 número
1 símbolo (ej: !@#$%^&*)
La contraseña debe ser aleatoria (usar el módulo random o secrets).
"""
import random

# ============================================
# 1. DEFINIR LOS CARACTERES PERMITIDOS
# ============================================
letras_minusculas = "abcdefghijklmnopqrstuvwxyz"
letras_mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
simbolos = "!@#$%^&*"

# ============================================
# 2. PEDIR LA LONGITUD (MÍNIMO 4)
# ============================================
while True:
    try:
        longitud = int(input("Ingresa la longitud de la contraseña (mínimo 4): "))
        if longitud >= 4:
            break
        else:
            print("❌ La longitud debe ser al menos 4.")
    except ValueError:
        print("❌ Ingresa un número válido.")

# ============================================
# 3. CREAR LA LISTA CON LOS OBLIGATORIOS
# ============================================
lista_contrasena = []

# Agregamos 1 de cada tipo (obligatorios)
lista_contrasena.append(random.choice(letras_minusculas))
lista_contrasena.append(random.choice(letras_mayusculas))
lista_contrasena.append(random.choice(numeros))
lista_contrasena.append(random.choice(simbolos))

# ============================================
# 4. RELLENAR EL RESTO DE LA CONTRASEÑA
# ============================================
todos_los_caracteres = letras_minusculas + letras_mayusculas + numeros + simbolos

for i in range(longitud - 4):
    lista_contrasena.append(random.choice(todos_los_caracteres))

# ============================================
# 5. MEZCLAR Y UNIR
# ============================================
random.shuffle(lista_contrasena)
contrasena_final = "".join(lista_contrasena)

# ============================================
# 6. MOSTRAR RESULTADO
# ============================================
print(f"Tu nueva contraseña es: {contrasena_final}")