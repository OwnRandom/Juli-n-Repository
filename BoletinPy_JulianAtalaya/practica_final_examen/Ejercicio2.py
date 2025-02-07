def ConvertirEspaciado(texto):
    # Convertimos la cadena en una lista de caracteres y luego unimos con un espacio entre ellos.
    return ' '.join(texto)

# Programa principal
if __name__ == "__main__":
    # Pedimos la entrada al usuario
    cadena = input("Introduce una cadena: ")
    
    # Llamamos a la función para convertir la cadena
    resultado = ConvertirEspaciado(cadena)
    
    # Mostramos el resultado
    print("La cadena con espacios entre los caracteres:", resultado)
