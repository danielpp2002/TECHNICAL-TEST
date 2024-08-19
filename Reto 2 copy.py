import random

# Ordenamiento por Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        # Dividir el arreglo en mitades
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        # Ordenar cada mitad
        merge_sort(left_half)
        merge_sort(right_half)
        
        # Inicializar índices para fusionar
        i = j = k = 0
        
        # Fusionar las mitades en el arreglo original
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        # Copiar los elementos restantes de left_half, si los hay
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        # Copiar los elementos restantes de right_half, si los hay
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    
    return arr

def sorted_squares(array, S):
    # Juntar las cifras de S para formar SS
    SS = int(f"{S}{S}")  # Si S es 3, SS será 33
    
    # Calcular el cuadrado de cada número y filtrar fuera del rango
    squares = [x * x for x in array if 0 <= x * x <= SS]
    
    # Ordenar los cuadrados usando Merge Sort
    sorted_squares = merge_sort(squares)
    
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
    
    # Ordenar la lista original
    sorted_list1 = merge_sort(list1)
    
    print("Lista 1:", sorted_list1)

    # Mostrar los resultados usando la función
    print("Resultado para Lista 1 (cuadrados ordenados):", sorted_squares(list1, S))

    # Preguntar al usuario si desea continuar o salir
    opcion = input("¿Desea generar nuevas listas? (s/n): ").strip().lower()
    if opcion != 's':
        print("Saliendo del programa...")
        break
