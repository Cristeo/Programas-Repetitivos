# Ejercicio 1: Tabla de multiplicar de un número con un bucle for
import math
print("Tabla de multiplicar")

# Pedimos al usuario el número del que quiere la tabla
numero = int(input("Mete un numero entero: "))

print("Tabla de multiplicar del:", numero)
print("-" * 10)  # Línea separadora

# Recorremos del 1 al 10 (el 11 no se incluye)
for i in range(1, 11):
    # Multiplicamos el número por el valor actual del contador
    resultado = numero * i

    # Mostramos la operación completa
    print(numero, "*", i, "=", resultado)
