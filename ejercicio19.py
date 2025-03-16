def logaritmo_divisiones_sucesivas(n: int, base: int = 2) -> int:
    
    if n < 1:
        raise ValueError("El número debe ser un entero positivo mayor que 0.")
    if base <= 1:
        raise ValueError("La base del logaritmo debe ser mayor que 1.")
    
    logaritmo = 0
    while n >= base:
        n //= base
        logaritmo += 1
    return logaritmo


numero = int(input("Ingrese un número entero positivo: "))
base = int(input("Ingrese la base del logaritmo (mayor que 1): "))


resultado = logaritmo_divisiones_sucesivas(numero, base)
print(f"log_{base}({numero}) ≈ {resultado}")