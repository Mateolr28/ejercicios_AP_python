def potencia_multiplicativa(base: int, exponente: int) -> int:
    
    if exponente == 0:
        return 1  
    resultado = 1
    for _ in range(exponente):
        resultado *= base
    return resultado


base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))


resultado = potencia_multiplicativa(base, exponente)
print(f"{base}^{exponente} = {resultado}")