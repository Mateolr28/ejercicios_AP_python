hombres = 0
mujeres = 0

total_personas = int(input("Ingrese la cantidad total de personas a procesar: "))
contador = 0

while contador < total_personas:
    genero = input("Ingrese el género de la persona (H para hombre, M para mujer): ").strip().upper()
    if genero == 'H':
        hombres += 1
    elif genero == 'M':
        mujeres += 1
    else:
        print("Entrada no válida, intente nuevamente.")
        continue  # Repite la iteración sin aumentar el contador
    
    contador += 1  # Solo aumenta el contador si la entrada es válida

print(f"Total de hombres: {hombres}, Total de mujeres: {mujeres}, Total de personas: {total_personas}")