'''Cree un programa que solicite cuatro datos numéricos para construir un tipo de 
dato para fechas: día de la semana entre 1 y 7 (el domingo es el día 1, el lunes el 2, 
etc.), día del mes entre 1 y 31, número del mes entre 1 y 12 (el 1 es el mes enero, el 
2 febrero, etc.) y el año.  Cree una función que devuelva una fecha en un formato 
similar a este: Jueves, 26 de Octubre de 2023, si los datos son: 5, 26, 10, 2023.  
Añada otras funciones para devolver y cambiar el día, la hora, el año, etc. '''


from datetime import datetime

dias_semana = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

def construir_fecha(dia_semana, dia_mes, mes, anio):
    return f"{dias_semana[dia_semana - 1]}, {dia_mes} de {meses[mes - 1]} de {anio}"

def cambiar_dia(fecha, nuevo_dia):
    return fecha.replace(day=nuevo_dia)

def cambiar_mes(fecha, nuevo_mes):
    return fecha.replace(month=nuevo_mes)

def cambiar_anio(fecha, nuevo_anio):
    return fecha.replace(year=nuevo_anio)

dia_semana = int(input("Ingrese el día de la semana (1-7): "))
dia_mes = int(input("Ingrese el día del mes (1-31): "))
mes = int(input("Ingrese el número del mes (1-12): "))
anio = int(input("Ingrese el año: "))

fecha_formateada = construir_fecha(dia_semana, dia_mes, mes, anio)
print("Fecha construida:", fecha_formateada)
