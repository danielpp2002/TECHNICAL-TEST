import random

# Ordenamiento por Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Mover los elementos de arr[0..i-1] que son mayores que key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def sorted_squares(array, S):
    # Juntar las cifras de S para formar SS
    SS = int(f"{S}{S}")  # Si S es 3, SS será 33
    
    # Calcular el cuadrado de cada número y filtrar fuera del rango
    squares = [x * x for x in array if 0 <= x * x <= SS]
    
    # Ordenar los cuadrados usando Insertion Sort
    sorted_squares = insertion_sort(squares)
    
    return sorted_squares

# Generar listas de enteros aleatorios
def generate_random_list(n, min_value=-10, max_value=10):
    return [random.randint(min_value, max_value) for _ in range(n)]

# Ciclo para repetir la operación hasta que el usuario decida salir
S = 3  # Valor fijo para el rango SS

while True:
    # Ingreso del tamaño de la lista por el usuario
    n = int(input("Ingrese el tamaño de la lista: "))
    # Generar dos listas aleatorias
    list1 = generate_random_list(n)
    
    # Ordenar la lista original usando Insertion Sort
    sorted_list1 = insertion_sort(list1)
    
    print("Lista 1:", sorted_list1)

    # Mostrar los resultados usando la función
    print("Resultado para Lista 1 (cuadrados ordenados):", sorted_squares(list1, S))

    # Preguntar al usuario si desea continuar o salir
    opcion = input("¿Desea generar nuevas listas? (s/n): ").strip().lower()
    if opcion != 's':
        print("Saliendo del programa...")
        break
