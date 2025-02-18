'''Convierta un número a letras.  Por ejemplo: 1584 → mil quinientos ochenta y 
cuatro.'''

def unidades(n):
    if n == 1: return "uno"
    if n == 2: return "dos"
    if n == 3: return "tres"
    if n == 4: return "cuatro"
    if n == 5: return "cinco"
    if n == 6: return "seis"
    if n == 7: return "siete"
    if n == 8: return "ocho"
    if n == 9: return "nueve"
    return ""

def decenas(n):
    if n == 10: return "diez"
    if n == 11: return "once"
    if n == 12: return "doce"
    if n == 13: return "trece"
    if n == 14: return "catorce"
    if n == 15: return "quince"
    if n < 20: return "dieci" + unidades(n - 10)
    if n == 20: return "veinte"
    if n < 30: return "veinti" + unidades(n - 20)
    if n == 30: return "treinta"
    if n == 40: return "cuarenta"
    if n == 50: return "cincuenta"
    if n == 60: return "sesenta"
    if n == 70: return "setenta"
    if n == 80: return "ochenta"
    if n == 90: return "noventa"
    return decenas(n - (n % 10)) + " y " + unidades(n % 10)

def centenas(n):
    if n == 100: return "cien"
    if n < 200: return "ciento " + decenas(n - 100)
    if n == 200: return "doscientos"
    if n < 300: return "doscientos " + decenas(n - 200)
    if n == 300: return "trescientos"
    if n < 400: return "trescientos " + decenas(n - 300)
    if n == 400: return "cuatrocientos"
    if n < 500: return "cuatrocientos " + decenas(n - 400)
    if n == 500: return "quinientos"
    if n < 600: return "quinientos " + decenas(n - 500)
    if n == 600: return "seiscientos"
    if n < 700: return "seiscientos " + decenas(n - 600)
    if n == 700: return "setecientos"
    if n < 800: return "setecientos " + decenas(n - 700)
    if n == 800: return "ochocientos"
    if n < 900: return "ochocientos " + decenas(n - 800)
    if n == 900: return "novecientos"
    if n < 1000: return "novecientos " + decenas(n - 900)
    return ""

def miles(n):
    if n < 1000: return centenas(n)
    if n == 1000: return "mil"
    if n < 2000: return "mil " + centenas(n - 1000)
    return unidades(n // 1000) + " mil " + centenas(n % 1000)

def convertir_a_letras(n):
    if n == 0: return "cero"
    return miles(n).strip()

numero = int(input("Ingrese un número: "))
print(convertir_a_letras(numero))