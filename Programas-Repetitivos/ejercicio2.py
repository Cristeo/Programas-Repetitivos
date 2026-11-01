# Ejercicio 2: Decir si 5 personas son mayores o menores de edad



# Repetimos 5 veces (una por persona)
for i in range(5):
    # Pedimos la edad
    edad = int(input("Introduce tu edad: "))
    # 18 o más es mayor de edad
    if edad >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")
