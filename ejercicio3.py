'''Leer el nombre y la nota de un grupo de T estudiantes. Encuentre quien sacó la 
mejor nota y de cuanto fue ésta. '''

T = int(input("Ingrese la cantidad de estudiantes: "))

mejor_nota = -1
mejor_estudiante = ""

for _ in range(T):
    nombre = input("Ingrese el nombre del estudiante: ")
    nota = float(input("Ingrese la nota: "))

    if nota > mejor_nota:
        mejor_nota = nota
        mejor_estudiante = nombre

print(f"\nEl estudiante con mejor nota es {mejor_estudiante} con {mejor_nota}")
        