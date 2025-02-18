''' Leer una cantidad indeterminada de números e informar si se ingresó 
ordenadamente. '''

anterior = None
ordenado = True

while True:
    try:
        num = input("Ingrese un número (o cualquier letra para salir): ")
        num = int(num)
        
        if anterior is not None and num < anterior:
            ordenado = False
        
        anterior = num
    except ValueError:
        break

if ordenado:
    print("Los números fueron ingresados en orden ascendente.")
else:
    print("Los números no fueron ingresados en orden ascendente.")