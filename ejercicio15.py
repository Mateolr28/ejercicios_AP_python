import math

def polar_to_cartesian(r, theta):
    x = r * math.cos(math.radians(theta))
    y = r * math.sin(math.radians(theta))
    return x, y

def cartesian_to_polar(x, y):
    r = math.sqrt(x**2 + y**2)
    theta = math.degrees(math.atan2(y, x))
    return r, theta

def main():
    while True:
        print("\nConversor de coordenadas")
        print("1. Convertir de polares a cartesianas")
        print("2. Convertir de cartesianas a polares")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            r = float(input("Ingrese el valor de r: "))
            theta = float(input("Ingrese el valor de θ (en grados): "))
            x, y = polar_to_cartesian(r, theta)
            print(f"Coordenadas cartesianas: x = {x:.2f}, y = {y:.2f}")
        elif opcion == '2':
            x = float(input("Ingrese el valor de x: "))
            y = float(input("Ingrese el valor de y: "))
            r, theta = cartesian_to_polar(x, y)
            print(f"Coordenadas polares: r = {r:.2f}, θ = {theta:.2f}°")
        elif opcion == '3':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()
