# Lista para almacenar los numeros
numeros = []

def anadir_numero():
    try:
        numero = int(input("Introduce un numero: "))
        numeros.append(numero)
        print(f"{numero} ha sido anadido al final de la lista.")
    except ValueError:
        print("Error: Debes introducir un numero entero.")

def anadir_numero_posicion():
    try:
        numero = int(input("Introduce un numero: "))
        posicion = int(input("Introduce la posicion (1 para la primera posicion): "))
        if 1 <= posicion <= len(numeros) + 1:
            numeros.insert(posicion - 1, numero)
            print(f"{numero} ha sido anadido en la posicion {posicion}.")
        else:
            print("Error: La posicion no es valida.")
    except ValueError:
        print("Error: Debes introducir un numero entero.")

def longitud_lista():
    print(f"La longitud de la lista es: {len(numeros)}.")

def eliminar_ultimo():
    if numeros:
        ultimo = numeros.pop()
        print(f"El numero {ultimo} ha sido eliminado de la lista.")
    else:
        print("Error: La lista esta vacia.")

def eliminar_numero():
    try:
        posicion = int(input("Introduce la posicion (1 para la primera posicion): "))
        if 1 <= posicion <= len(numeros):
            eliminado = numeros.pop(posicion - 1)
            print(f"El numero {eliminado} ha sido eliminado de la posicion {posicion}.")
        else:
            print("Error: La posicion no es valida.")
    except ValueError:
        print("Error: Debes introducir un numero entero.")

def contar_numeros():
    try:
        numero = int(input("Introduce un numero para contar sus apariciones: "))
        count = numeros.count(numero)
        print(f"El numero {numero} aparece {count} veces en la lista.")
    except ValueError:
        print("Error: Debes introducir un numero entero.")

def posiciones_de_un_numero():
    try:
        numero = int(input("Introduce un numero para encontrar sus posiciones: "))
        posiciones = [i + 1 for i, x in enumerate(numeros) if x == numero]
        if posiciones:
            print(f"El numero {numero} esta en las posiciones: {', '.join(map(str, posiciones))}.")
        else:
            print(f"El numero {numero} no esta en la lista.")
    except ValueError:
        print("Error: Debes introducir un numero entero.")

def mostrar_numeros():
    if numeros:
        print("Los numeros en la lista son:")
        print(", ".join(map(str, numeros)))
    else:
        print("La lista esta vacia.")

def menu():
    while True:
        print("\nMenu:")
        print("1. Anadir numero a la lista")
        print("2. Anadir numero de la lista en una posicion")
        print("3. Longitud de la lista")
        print("4. Eliminar el ultimo numero")
        print("5. Eliminar un numero")
        print("6. Contar numeros")
        print("7. Posiciones de un numero")
        print("8. Mostrar numeros")
        print("9. Salir")
        
        opcion = input("Selecciona una opcion (1-9): ")
        
        if opcion == '1':
            anadir_numero()
        elif opcion == '2':
            anadir_numero_posicion()
        elif opcion == '3':
            longitud_lista()
        elif opcion == '4':
            eliminar_ultimo()
        elif opcion == '5':
            eliminar_numero()
        elif opcion == '6':
            contar_numeros()
        elif opcion == '7':
            posiciones_de_un_numero()
        elif opcion == '8':
            mostrar_numeros()
        elif opcion == '9':
            print("¡Hasta luego!")
            break
        else:
            print("Opcion invalida. Por favor, selecciona una opcion entre 1 y 9.")

# Ejecutamos el programa
if __name__ == "__main__":
    menu()
