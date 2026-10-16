"""
CALCULAFR IDNICE DE MASA CORPORAL (IMC)
Pida al usuario su peso (en kg) y su altura (en metros)
Calcule el IMC (Índice de Masa Corporal)
Muestre el resultado y una categoría según el IMC
"""


def calcular_IMC(peso_Kg, altura_cm): 
    altura_m = altura_cm / 100
    IMC = peso_Kg / (altura_m ** 2)
    IMC_redondeado = round(IMC, 2)
    return IMC_redondeado


while True: 
    try: 
        peso = float(input("Ingresa tu peso en kilogramos: "))
        altura = float(input("Ingresa tu altura en centímetros: "))
    except ValueError: 
        print("❌ Ingresa solo números.")
        continue

    calcular = calcular_IMC(peso, altura)
    print(f"Tu índice de masa corporal (IMC) es de: {calcular}.")
    break
        