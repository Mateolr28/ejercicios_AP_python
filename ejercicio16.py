def division_y_modulo(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")

    negativo = (a < 0) != (b < 0)  
    a, b = abs(a), abs(b)  

    cociente = 0
    while a >= b:
        a -= b
        cociente += 1

    if negativo:
        cociente = -cociente  

    residuo = a  

    return cociente, residuo

a = int(input("Ingrese el dividendo: "))
b = int(input("Ingrese el divisor: "))

cociente, residuo = division_y_modulo(a, b)
print(f"División entera: {cociente}")
print(f"Módulo: {residuo}")