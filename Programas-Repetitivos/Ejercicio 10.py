# Ejercicio 10: Suma n-ésima desde 1 hasta N[cite: 1]
# Pedimos hasta qué número sumar
N = int(input("Introduce un número entero positivo (N): "))
suma = 0  # Acumulador en 0

# Recorremos desde 1 hasta N
for i in range(1, N + 1):
    # Sumamos el valor actual al acumulador
    suma = suma + i

# Mostramos el resultado final
print("La suma n-ésima (S) es:", suma)
