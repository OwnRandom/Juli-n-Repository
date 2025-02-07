#metdodo que crea la lista y elimina las posciones que son multiplos de 3
def ejercicio_2():
    abecedario = list("abcdefghijklmnopqrstuvwxyz")
    # Eliminamos las letras en posiciones múltiplos de 3 (considerando índice 0)
    resultado = [letra for i, letra in enumerate(abecedario) if (i + 1) % 3 != 0]
    print("Lista resultante:", resultado)

ejercicio_2()