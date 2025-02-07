# EJERCICIO 3
def decimal_a_binario(decimal):
#Convierte un número decimal a binario
    return bin(decimal)[2:]  # bin() devuelve una cadena con '0b' al inicio

def binario_a_decimal(binario):
#Convierte un número binario a decimal
    return int(binario, 2)

# Ejemplo de uso
decimal = 70
binario = "101010"

print(f"{decimal} en binario es: {decimal_a_binario(decimal)}")
print(f"{binario} en decimal es: {binario_a_decimal(binario)}")