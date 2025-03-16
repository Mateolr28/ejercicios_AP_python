def multiplicar_suma_sucesiva(a: int, b: int) -> int:
    
    if a < b:
        a, b = b, a  
    resultado = sum(a for _ in range(b))
    return resultado

print(multiplicar_suma_sucesiva(2, 3)) 
print(multiplicar_suma_sucesiva(3, 2))  
print(multiplicar_suma_sucesiva(5, 4))  