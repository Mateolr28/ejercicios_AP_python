'''A un grupo de hombres y mujeres les realizan una prueba de conocimientos. Se 
desea conocer cuántas mujeres y cuántos hombres presentaron la prueba y el total 
de personas que se procesaron. '''

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
        continue  
    
    contador += 1  

print(f"Total de hombres: {hombres}, Total de mujeres: {mujeres}, Total de personas: {total_personas}")