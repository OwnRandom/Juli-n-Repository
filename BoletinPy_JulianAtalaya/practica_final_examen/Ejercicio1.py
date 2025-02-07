from math import gcd
from fractions import Fraction

# Función para leer una fracción y simplificarla
def leer_fraccion():
    numerador = int(input("Introduce el numerador: "))
    denominador = int(input("Introduce el denominador: "))
    if denominador == 0:
        print("El denominador no puede ser cero. Intenta nuevamente.")
        return leer_fraccion()
    return Fraction(numerador, denominador)

# Función para escribir una fracción
def escribir_fraccion(fraccion):
    if fraccion.denominator == 1:
        print(f"La fracción es: {fraccion.numerator}")
    else:
        print(f"La fracción es: {fraccion.numerator}/{fraccion.denominator}")

# Función para simplificar la fracción (usando la librería fractions)
def simplificar_fraccion(fraccion):
    return fraccion

# Función para sumar dos fracciones
def sumar_fracciones(fraccion1, fraccion2):
    return fraccion1 + fraccion2

# Función para restar dos fracciones
def restar_fracciones(fraccion1, fraccion2):
    return fraccion1 - fraccion2

# Función para multiplicar dos fracciones
def multiplicar_fracciones(fraccion1, fraccion2):
    return fraccion1 * fraccion2

# Función para dividir dos fracciones
def dividir_fracciones(fraccion1, fraccion2):
    if fraccion2 == 0:
        print("No se puede dividir por cero.")
        return None
    return fraccion1 / fraccion2

# Menú interactivo
def menu():
    while True:
        print("\nMenu:")
        print("1. Sumar dos fracciones")
        print("2. Restar dos fracciones")
        print("3. Multiplicar dos fracciones")
        print("4. Dividir dos fracciones")
        print("5. Salir")
        
        opcion = int(input("Seleccione una opcion: "))
        
        if opcion == 1:
            print("Introduce la primera fraccion:")
            fraccion1 = leer_fraccion()
            print("Introduce la segunda fraccion:")
            fraccion2 = leer_fraccion()
            resultado = sumar_fracciones(fraccion1, fraccion2)
            print(f"El resultado de la suma es: {resultado}")
        
        elif opcion == 2:
            print("Introduce la primera fraccion:")
            fraccion1 = leer_fraccion()
            print("Introduce la segunda fraccion:")
            fraccion2 = leer_fraccion()
            resultado = restar_fracciones(fraccion1, fraccion2)
            print(f"El resultado de la resta es: {resultado}")
        
        elif opcion == 3:
            print("Introduce la primera fraccion:")
            fraccion1 = leer_fraccion()
            print("Introduce la segunda fraccion:")
            fraccion2 = leer_fraccion()
            resultado = multiplicar_fracciones(fraccion1, fraccion2)
            print(f"El resultado de la multiplicacion es: {resultado}")
        
        elif opcion == 4:
            print("Introduce la primera fraccion:")
            fraccion1 = leer_fraccion()
            print("Introduce la segunda fraccion:")
            fraccion2 = leer_fraccion()
            resultado = dividir_fracciones(fraccion1, fraccion2)
            if resultado is not None:
                print(f"El resultado de la division es: {resultado}")
        
        elif opcion == 5:
            print("¡Hasta luego!")
            break
        
        else:
            print("Opcion no valida. Intenta nuevamente.")


menu()
