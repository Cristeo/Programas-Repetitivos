# Ejercicio 5: Contar cuántos de 5 alumnos han aprobado
# Contador de aprobados, empieza en 0
aprobados_c = 0

# Repetimos 5 veces (una por alumno)
for i in range (5):
    nota = int(input("Introduce tu nota: "))

    # Con 5 o más se aprueba
    if nota >= 5:
        print("Estas aprobado")
        aprobados_c += 1  # Sumamos un aprobado
    else:
       print("Estas suspenso")

# Mostramos el total de aprobados
print ("Numero de aprobados", aprobados_c)
