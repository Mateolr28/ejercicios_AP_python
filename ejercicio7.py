'''Cree un juego de azar similar al tragamonedas que muestra tres o cuatro imágenes 
usando caracteres en lugar de imágenes. Determine los premios a entregar según 
acierte el usuario y dependiendo de la imagen (carácter). '''

import random

def jugar_tragamonedas(total_monedas):
    simbolos = "@#$%&" 
    premio = {"@": 10, "#": 20, "$": 50, "%": 100, "&": 200}  
    
    if random.random() < 0.5:
        r1 = r2 = r3 = random.choice(simbolos)  
    else:
        r1 = random.choice(simbolos)
        r2 = random.choice(simbolos)
        r3 = random.choice(simbolos)
    
    print(f"\nResultado: [{r1}] [{r2}] [{r3}]")
    
    if r1 == r2 == r3:
        total_monedas += premio[r1]
        print(f"¡Felicidades! Has ganado {premio[r1]} monedas.")
    elif r1 == r2 or r2 == r3 or r1 == r3:
        total_monedas += 5
        print("¡Casi! Has acertado dos símbolos iguales. Ganas 5 monedas.")
    else:
        total_monedas -= 5
        print("Lo siento, no hay coincidencias. Pierdes 5 monedas.")
    
    return total_monedas

total_monedas = 0
while True:
    total_monedas = jugar_tragamonedas(total_monedas)
    print(f"Total de monedas actuales: {total_monedas}")
    jugar_de_nuevo = input("¿Quieres jugar otra vez? (s/n): ").strip().lower()
    if jugar_de_nuevo != "s":
        print(f"Juego terminado. Total de monedas finales: {total_monedas}")
        break
