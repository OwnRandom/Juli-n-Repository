# Diccionario con los precios de las frutas
precios = {
    'manzana': 1.2,  # Precio por kilogramo de manzana
    'platano': 1.5,  # Precio por kilogramo de plátano
    'naranja': 1.0,  # Precio por kilogramo de naranja
    'uva': 2.0       # Precio por kilogramo de uva
}

def consultar_precio(fruta, cantidad):
    if fruta in precios:
        precio_total = precios[fruta] * cantidad
        return f"El precio total de {cantidad} kg de {fruta} es: {precio_total:.2f}€"
    else:
        return f"Error: La fruta {fruta} no está disponible en el diccionario."

# Programa principal
if __name__ == "__main__":
    while True:
        # Pedimos el nombre de la fruta
        fruta = input("Introduce el nombre de la fruta: ").lower()

        # Pedimos la cantidad vendida
        try:
            cantidad = float(input("Introduce la cantidad vendida: "))
        except ValueError:
            print("Error: La cantidad debe ser un numero.")
            continue

        # Consultamos el precio de la fruta y mostramos el resultado
        resultado = consultar_precio(fruta, cantidad)
        print(resultado)

        # Preguntamos si quiere hacer otra consulta
        respuesta = input("¿Quieres hacer otra consulta? (si/no): ").lower()
        if respuesta != 'si':
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
