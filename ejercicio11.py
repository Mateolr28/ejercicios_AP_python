'''Ingrese un número entero por teclado.  Cree una función que determine si dicho 
número pertenece a la serie de Fibonacci. '''

def es_fibonacci(n):
    if n < 0:
        return False
    
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    
    return a == n

num = int(input("Ingrese un número entero: "))

if es_fibonacci(num):
    print(f"{num} pertenece a la serie de Fibonacci.")
else:
    print(f"{num} no pertenece a la serie de Fibonacci.")
