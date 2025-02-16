'''En una fábrica contratan personal que cumpla con los siguientes requisitos para 
laborar medio tiempo: Mayor de 18 años y menor de 50, estado civil soltero y que 
actualmente se encuentre estudiando. A la fábrica se presentaron M aspirantes. 
Encuentre cuántos cumplen con los requisitos que se piden y qué porcentaje sobre 
el total de personas representan. '''

M = int(input("Ingrese la cantidad de aspirantes: "))
cumplen = 0 

for _ in range(M):
    print("\nIngrese los datos del aspirante: ")
    edad = int(input("Edad: "))
    estado_civil = input("Estado civil (Soltero/Casado): ").strip().lower()
    estudiando = input("Estudia? (si/no): ").strip().lower()

    if 18 < edad < 50 and estado_civil == "soltero" and estudiando == "si":
        cumplen += 1

procentaje = (cumplen / M) * 100 if M > 0 else 0

print("\nResultados: ")
print(f"Aspirantes que cumplen: {cumplen}")
print(f"Porcentaje: {procentaje:.2f}%")