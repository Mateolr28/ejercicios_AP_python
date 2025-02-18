'''Realizar el cálculo de una devuelta.  Debe contar con denominaciones de monedas 
y billetes para especificar cuántos de cada uno debe entregar.  Por ejemplo, si la 
devuelta son $450, podría devolver 2 monedas de $200 y una de $50.'''

def calcular_devuelta(monto):
    billetes_monedas = {
        100000:  "billetes de $100,000",
        50000:   "billetes de $50,000",
        20000:   "billetes de $20,000",
        10000:   "billetes de $10,000",
        5000:    "billetes de $5,000",
        2000:    "billetes de $2,000",
        1000:    "billetes de $1,000",
        500:     "monedas de $500",
        200:     "monedas de $200",
        100:     "monedas de $100",
        50:      "monedas de $50"
    }
    
    resultado = ""
    for valor, descripcion in billetes_monedas.items():
        cantidad = monto // valor
        if cantidad > 0:
            resultado += f"{cantidad} {descripcion}\n"
            monto -= cantidad * valor
    
    return resultado.strip()

# Solicitar el monto al usuario
monto = int(input("Ingrese la cantidad de devuelta: "))
devuelta = calcular_devuelta(monto)
print(devuelta)