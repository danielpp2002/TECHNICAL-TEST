import random

def generate_and_process_list():
    S = 3  # Fijar el valor de S a 3

    # Solicitar al usuario el valor de n y asegurarse de que n <= 100
    while True:
        n = int(input("Ingrese el tamaño de la lista (n): "))
        if n <= 100:
            break
        else:
            print("El valor de n no puede ser mayor a 100. Por favor, intente de nuevo.")

    # Generar una lista de n números aleatorios de 3 dígitos, donde cada dígito esté en el rango [0, 3]
    random_list = []
    for _ in range(n):
        num = int(''.join(str(random.randint(0, S)) for _ in range(3)))
        random_list.append(num)
    
    print("Lista aleatoria generada:", random_list)
    
    result = []
    
    for number in random_list:
        # Convertir el número a string para revisar cada dígito
        filtered_number = ''.join(d for d in str(number) if int(d) < S)  # Filtrar fuera el dígito 3 o superior
        
        # Añadir el número filtrado (como string) a la lista resultado
        if filtered_number:  # Si el resultado no está vacío
            result.append(filtered_number)
        else:
            result.append('0')  # Si se eliminan todos los dígitos, añadir '0'
    
    # Revertir la lista
    result = result[::-1]
    
    print("Lista procesada:", result)

# Ciclo para repetir la operación hasta que el usuario decida salir
while True:
    generate_and_process_list()

    # Preguntar al usuario si desea continuar o salir
    opcion = input("¿Desea generar y procesar otra lista? (s/n): ").strip().lower()
    if opcion != 's':
        print("Saliendo del programa...")
        break
