'''Una empresa tiene 5 sucursales y en cada sucursal hay M empleados. De cada 
empleado se conoce su cédula y salario. Encuentre: El salario promedio de cada 
sucursal y de toda la empresa.  El empleado que gana mayor salario en cada 
sucursal y en toda la empresa. El empleado que gana menor salario en cada 
sucursal y en toda la empresa.  El monto pagado por concepto de salarios en cada 
sucursal y en toda la empresa.'''

NUM_SUCURSALES = 5

total_salarios_empresa = 0
total_empleados_empresa = 0
empleado_mayor_salario_global = None
empleado_menor_salario_global = None

for i in range(1, NUM_SUCURSALES + 1):
    print(f"\n--- Sucursal {i} ---")
    
    num_empleados = int(input(f"Ingrese la cantidad de empleados en la sucursal {i}: "))
    
    if num_empleados == 0:
        print("⚠️ No hay empleados en esta sucursal.")
        continue

    total_salarios_sucursal = 0
    empleado_mayor_salario = None
    empleado_menor_salario = None

    for _ in range(num_empleados):
        cedula = input("Ingrese la cédula del empleado: ")
        salario = float(input("Ingrese el salario del empleado: "))

        total_salarios_sucursal += salario

        if not empleado_mayor_salario or salario > empleado_mayor_salario[1]:
            empleado_mayor_salario = (cedula, salario)

        if not empleado_menor_salario or salario < empleado_menor_salario[1]:
            empleado_menor_salario = (cedula, salario)

    total_salarios_empresa += total_salarios_sucursal
    total_empleados_empresa += num_empleados

    if not empleado_mayor_salario_global or empleado_mayor_salario[1] > empleado_mayor_salario_global[1]:
        empleado_mayor_salario_global = empleado_mayor_salario

    if not empleado_menor_salario_global or empleado_menor_salario[1] < empleado_menor_salario_global[1]:
        empleado_menor_salario_global = empleado_menor_salario

    print(f"\nSucursal {i}:")
    print(f"Salario promedio: {total_salarios_sucursal / num_empleados:.2f}")
    print(f"Monto total en salarios: {total_salarios_sucursal:.2f}")
    print(f"Empleado con mayor salario: {empleado_mayor_salario[0]} con {empleado_mayor_salario[1]:.2f}")
    print(f"Empleado con menor salario: {empleado_menor_salario[0]} con {empleado_menor_salario[1]:.2f}")

if total_empleados_empresa > 0:
    print("\n--- Resumen de la empresa ---")
    print(f"Salario promedio de la empresa: {total_salarios_empresa / total_empleados_empresa:.2f}")
    print(f"Monto total en salarios en toda la empresa: {total_salarios_empresa:.2f}")
    print(f"Empleado con mayor salario en la empresa: {empleado_mayor_salario_global[0]} con {empleado_mayor_salario_global[1]:.2f}")
    print(f"Empleado con menor salario en la empresa: {empleado_menor_salario_global[0]} con {empleado_menor_salario_global[1]:.2f}")
else:
    print("\n⚠️ No se ingresaron empleados en ninguna sucursal.")
