def contar_primos(n):
    if n < 2:
        return 0
    
    # Criba de Eratóstenes
    es_primo = [True] * (n + 1)
    es_primo[0] = es_primo[1] = False  # 0 y 1 no son primos

    for i in range(2, int(n ** 0.5) + 1):
        if es_primo[i]:
            for j in range(i * i, n + 1, i):
                es_primo[j] = False

    return sum(es_primo)

# Solicitar entrada al usuario
def main():
    n = int(input("Ingrese un número: "))
    cantidad_primos = contar_primos(n)
    print(f"La cantidad de números primos entre 1 y {n} es: {cantidad_primos}")

if __name__ == "__main__":
    main()
