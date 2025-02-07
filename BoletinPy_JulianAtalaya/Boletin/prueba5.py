class Fabrica:
    def __init__(self, llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio

    def mostrar_atributos(self):
        return f"Llantas: {self.llantas}, Color: {self.color}, Precio: ${self.precio}"


class Moto(Fabrica):
    def __init__(self, color, precio):
        super().__init__(llantas=2, color=color, precio=precio)


class Carro(Fabrica):
    def __init__(self, color, precio):
        super().__init__(llantas=4, color=color, precio=precio)


if __name__ == "__main__":
    moto = Moto(color="Rojo", precio=1500)
    print("Atributos de la Moto:")
    print(moto.mostrar_atributos())

    carro = Carro(color="Azul", precio=20000)
    print("\nAtributos del Carro:")
    print(carro.mostrar_atributos())
