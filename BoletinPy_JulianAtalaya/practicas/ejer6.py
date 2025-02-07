# Crear la tupla con los meses del año
meses = (
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
)

while True:
    try:
        # Pedir al usuario un número
        numero = int(input("Introduce un número (1-12) para ver el mes, o 0 para salir: "))
        
        if numero == 0:
            print("¡Programa terminado!")
            break
        elif 1 <= numero <= len(meses):
            print(f"El mes correspondiente al número {numero} es {meses[numero - 1]}.")
        else:
            print("Error: Número fuera de rango. Por favor, introduce un número entre 1 y 12.")
    except ValueError:
        print("Error: Entrada no válida. Por favor, introduce un número entero.")
