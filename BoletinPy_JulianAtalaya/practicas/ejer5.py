def es_bisiesto(año):
    # Un año es bisiesto si es divisible por 4 pero no por 100
    # O si es divisible por 400
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:
        return False

while True:
    try:
        # Solicitar al usuario un año
        año = int(input("Introduce un año (o escribe '0' para salir): "))
        
        if año == 0:
            print("¡Programa terminado!")
            break
        
        if es_bisiesto(año):
            print(f"El año {año} es bisiesto.")
        else:
            print(f"El año {año} no es bisiesto.")
    
    except ValueError:
        print("Error: Entrada no válida. Por favor, introduce un número entero.")
