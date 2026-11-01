# Ejercicio 4: Contar cuántas de 5 personas son mayores de edad
# Contador de mayores de edad, empieza en 0
C_mayor_edad = 0

# Repetimos 5 veces (una por persona)
for i in range (5):
    edad = int(input("Introduce tu edad: "))

    if edad >= 18:
        # Es mayor: sumamos 1 al contador
        C_mayor_edad += 1
    else:
       print("Eres menor de edad")

# Mostramos el total al terminar el bucle
print ("Numero de mayores", C_mayor_edad)
