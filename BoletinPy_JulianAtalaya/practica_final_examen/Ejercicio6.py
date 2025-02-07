def decimal_a_binario():
    try:
        decimal = int(input("Ingrese un numero decimal: "))
        binario = bin(decimal)[2:]  # Convertir a binario y quitar el prefijo '0b'
        print(f"El numero {decimal} en binario es: {binario}")
    except ValueError:
        print("Error: Debe ingresar un numero entero.")

def binario_a_decimal():
    try:
        binario = input("Ingrese un numero binario: ")
        decimal = int(binario, 2)  # Convertir de binario a decimal
        print(f"El numero binario {binario} en decimal es: {decimal}")
    except ValueError:
        print("Error: Debe ingresar un numero binario valido (solo 0 y 1).")

def menu():
    while True:
        print("\nSeleccione una opcion:")
        print("1. Convertir de decimal a binario")
        print("2. Convertir de binario a decimal")
        print("3. Salir")
        
        opcion = input("Ingrese el numero de opcion (1, 2 o 3): ")
        
        if opcion == '1':
            decimal_a_binario()
        elif opcion == '2':
            binario_a_decimal()
        elif opcion == '3':
            print("Hasta luego!")
            break
        else:
            print("Opcion invalida. Intente de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()
