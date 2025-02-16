'''Se tiene el nombre, número de horas diurnas (nhd), número de horas nocturnas 
(nhn), número de horas festivas (nhf) y salario básico hora de un grupo de 
empleados. Calcular el salario básico teniendo en cuenta que la hora nocturna tiene 
un recargo del 35% y la hora festiva un recargo del 75%. Terminar la lectura de 
datos cuando se ingrese el nombre "***". Informar cuántos empleados se ingresaron 
y el promedio de salarios básicos que devengan éstos.'''

def calcular_salario(nhd, nhn, nhf, salario_hora):
    return (nhd * salario_hora) + (nhn * salario_hora * 1.35) + (nhf * salario_hora * 1.75)

total_salarios = 0
total_empleados = 0

print("\nIngrese los datos de los empleados (Ingrese '***' como nombre para terminar):")

while True:
    nombre = input("\nNombre del empleado: ").strip()
    if nombre == "***":
        break  

    try:
        nhd = int(input("Número de horas diurnas: "))
        nhn = int(input("Número de horas nocturnas: "))
        nhf = int(input("Número de horas festivas: "))
        salario_hora = float(input("Salario básico por hora: "))
        
        salario_basico = calcular_salario(nhd, nhn, nhf, salario_hora)
        total_salarios += salario_basico
        total_empleados += 1

        print(f"Salario básico de {nombre}: {salario_basico:.2f}")
    
    except ValueError:
        print("⚠️ Entrada inválida. Intente de nuevo.")

if total_empleados:
    print(f"\nTotal de empleados ingresados: {total_empleados}")
    print(f"Promedio de salarios básicos: {total_salarios / total_empleados:.2f}")
else:
    print("\n⚠️ No se ingresaron empleados.")
