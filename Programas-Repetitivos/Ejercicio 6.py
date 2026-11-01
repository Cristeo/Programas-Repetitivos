# Ejercicio 6: Calcular el máximo de varios números con un bucle while

# Pedimos el primer número
numero = int(input("Introduce un número entero: "))
maximo = numero  # Guardamos este número como el máximo provisional

# Preguntamos si quiere seguir
continuar = input("¿Quieres introducir otro número? (s/n): ")

# Mientras responda "s" seguimos pidiendo números
while continuar == "s":
    numero = int(input("Introduce otro número entero: "))

    # Si el nuevo es mayor que el máximo actual, lo actualizamos
    if numero > maximo:
        maximo = numero

    # Volvemos a preguntar para decidir si el bucle continúa
    continuar = input("¿Quieres introducir otro número? (s/n): ")

# Al salir del bucle mostramos el máximo
print("El número máximo introducido es:", maximo)
