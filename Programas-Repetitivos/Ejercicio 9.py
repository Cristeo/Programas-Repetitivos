# Ejercicio 9: Calcular la media de las notas[cite: 1]
suma_notas = 0   # Acumulador de la suma de todas las notas
cantidad = 0     # Contador de cuántas notas se han introducido
continuar = "s"  # Empieza en "s" para que entre al menos una vez al bucle

while continuar == "s":
    nota = float(input("Introduce una nota: "))
    # Acumulamos la nota y contamos una más
    suma_notas = suma_notas + nota
    cantidad = cantidad + 1

    # Preguntamos si quiere introducir más notas
    continuar = input("¿Deseas introducir otra nota? (s/n): ")

# Calculamos la media si se ha introducido al menos una nota
if cantidad > 0:
    # Media = suma de notas / número de notas
    media = suma_notas / cantidad
    print("La nota media de la evaluación es:", media)
else:
    print("No se han introducido notas.")
