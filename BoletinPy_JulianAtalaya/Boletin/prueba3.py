class Calculadora:
    def __init__(self):
        self.valor1 = int(input("Introduce el primer número entero: "))
        self.valor2 = int(input("Introduce el segundo número entero: "))

    def sumar(self):
        return self.valor1 + self.valor2

    def restar(self):
        return self.valor1 - self.valor2

    def multiplicar(self):
        return self.valor1 * self.valor2

    def dividir(self):
        if self.valor2 != 0:
            return self.valor1 / self.valor2
        else:
            return "Error: División por cero no permitida."

if __name__ == "__main__":
    calculadora = Calculadora()

    print(f"La suma es: {calculadora.sumar()}")
    print(f"La resta es: {calculadora.restar()}")
    print(f"La multiplicación es: {calculadora.multiplicar()}")
    print(f"La división es: {calculadora.dividir()}")
