# Importamos math para poder usar la raíz cuadrada (sqrt)
import math

# Ejercicio 8: Obligar a introducir un positivo y hacer su raíz cuadrada con while
numero = -1  # Empezamos con un número negativo para forzar que entre al bucle

# Repetimos hasta que el usuario introduzca un número positivo (o 0)
while numero < 0:
    numero = float(input("Introduce un número positivo: "))

    # Si es negativo avisamos y el bucle vuelve a pedirlo
    if numero < 0:
        print("¡Error! El número es negativo. Inténtalo de nuevo.")

# Cuando salimos del bucle, calculamos la raíz
raiz = math.sqrt(numero)
print("La raíz cuadrada es:", raiz)
