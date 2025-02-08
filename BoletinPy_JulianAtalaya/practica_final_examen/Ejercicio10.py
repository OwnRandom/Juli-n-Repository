import random

def generar_codigo():
    numeros = random.sample(range(10), 4)  # Genera 4 números únicos
    return ''.join(map(str, numeros))

def evaluar_intento(codigo_secreto, intento):
    muertos = sum(1 for i in range(4) if intento[i] == codigo_secreto[i])
    heridos = sum(1 for i in range(4) if intento[i] in codigo_secreto and intento[i] != codigo_secreto[i])
    return muertos, heridos

def jugar_mastermind():
    codigo_secreto = generar_codigo()
    print("¡Bienvenido al juego Mastermind!")
    print("Tienes que adivinar un número de 4 cifras sin cifras repetidas.")
    intentos = 0
    
    while True:
        intento = input("Introduce tu intento (un número de 4 cifras sin repetir): ")
        
        if len(intento) != 4 or not intento.isdigit() or len(set(intento)) != 4:
            print("Entrada inválida. Asegúrate de ingresar un número de 4 cifras únicas.")
            continue
        
        intentos += 1
        muertos, heridos = evaluar_intento(codigo_secreto, intento)
        print(f"Resultado: {muertos} MUERTOS, {heridos} HERIDOS")
        
        if muertos == 4:
            print(f"¡Felicidades! Has adivinado el código {codigo_secreto} en {intentos} intentos.")
            break

if __name__ == "__main__":
    jugar_mastermind()
