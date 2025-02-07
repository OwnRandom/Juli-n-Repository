import math

def calcular_area():
    while True:
        # Preguntar al usuario qué área desea calcular
        opcion = input("¿Quieres calcular el área de un triángulo o un círculo? (escribe 'triángulo', 'círculo' o 'salir' para terminar): ").strip().lower()
        
        if opcion == "triángulo":
            # Pedir la base y la altura para calcular el área del triángulo
            try:
                base = float(input("Introduce la base del triángulo: "))
                altura = float(input("Introduce la altura del triángulo: "))
                area = (base * altura) / 2
                print(f"El área del triángulo es: {area}")
            except ValueError:
                print("Error: Por favor, introduce valores numéricos válidos.")
        
        elif opcion == "círculo":
            # Pedir el radio para calcular el área del círculo
            try:
                radio = float(input("Introduce el radio del círculo: "))
                area = math.pi * (radio ** 2)
                print(f"El área del círculo es: {area}")
            except ValueError:
                print("Error: Por favor, introduce un valor numérico válido.")
        
        elif opcion == "salir":
            print("¡Programa terminado!")
            break
        
        else:
            print("Opción no válida. Por favor, escribe 'triángulo', 'círculo' o 'salir'.")

# Llamar a la función para ejecutar el programa
calcular_area()
