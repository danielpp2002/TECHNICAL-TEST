import random

def generar_monedas_aleatorias(tamaño, rango_min=1, rango_max=10):
    return [random.randint(rango_min, rango_max) for _ in range(tamaño)]

def minChange(coins):
    coins.sort()  # Ordenar el arreglo de monedas
    minChange = 1  # Inicializar el cambio mínimo

    for coin in coins:
        if coin > minChange:
            break
        minChange += coin

    return minChange

# Ciclo para repetir la operación hasta que el usuario decida salir
while True:
    tamaño = int(input("Ingrese el tamaño de la lista de monedas: "))

    # Generamos la lista de monedas aleatorias
    monedas = generar_monedas_aleatorias(tamaño)

    # Mostramos la lista generada y el resultado
    print(f"Monedas generadas: {monedas}")
    print(f"El mínimo cambio que no se puede crear es: {minChange(monedas)}")

    # Preguntamos si el usuario desea continuar
    opcion = input("¿Desea generar otra lista? (s/n): ").strip().lower()
    if opcion != 's':
        print("Saliendo del programa...")
        break
