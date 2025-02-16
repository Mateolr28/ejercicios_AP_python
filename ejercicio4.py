'''Leer el nombre y salario de un grupo de trabajadores.  Muestre cuál es el empleado 
de más bajo salario y a cuánto equivale éste.'''

trabajadores = int(input("Ingrese la cantidad de trabajadores: "))

menor_salario = float("inf")
empleado_menor_salario = ""

for _ in range(trabajadores):
    nombre = input("Ingrese el nombre del trabajador: ")
    salario = float(input("Ingrese el salario: "))

    if salario < menor_salario:
        menor_salario = salario
        empleado_menor_salario = nombre

print(f"\nEl empleado con el salario más bajo es {empleado_menor_salario} con un salario de {menor_salario:.2f}.")