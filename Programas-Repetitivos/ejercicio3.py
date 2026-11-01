# Ejercicio 3: Decir si 5 números son nulos, positivos o negativos

# Repetimos 5 veces (una por número)
for u in range(5):
    numero = int(input("Introduce un número: "))
    # Si es 0 es nulo
    if numero == 0 :
        print("Es nulo")
    # Si es mayor que 0 es positivo
    elif numero > 0:
        print("Es positivo")
    # En otro caso es menor que 0, negativo
    else:
        print("Es negativo")
