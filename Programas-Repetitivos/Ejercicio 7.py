# Ejercicio 7: Calcular el mínimo de varios números
# Pedimos el primer número
numero = int(input("Introduce un número entero: "))
minimo = numero  # Guardamos el primero como mínimo provisional

# Preguntamos si quiere seguir
continuar = input("¿Quieres introducir otro número? (s/n): ")

# Mientras responda "s" seguimos pidiendo números
while continuar == "s":
    numero = int(input("Introduce otro número entero: "))

    # Si el número nuevo es menor que el mínimo actual, lo actualizamos
    if numero < minimo:
        minimo = numero

    # Preguntamos de nuevo para decidir si el bucle continúa
    continuar = input("¿Quieres introducir otro número? (s/n): ")

# Al salir del bucle mostramos el mínimo
print("El número mínimo introducido es:", minimo)
