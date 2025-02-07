class Marino:
    def hablar(self):
        print("Hola, soy un animal marino!")


class Pulpo(Marino):
    def hablar(self):
        print("Hola, soy un Pulpo!")


class Foca(Marino):
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def hablar(self):
        print(self.mensaje)


if __name__ == "__main__":

    marino = Marino()
    marino.hablar()  

   
    pulpo = Pulpo()
    pulpo.hablar()  

   
    foca = Foca("Hola, soy una Foca amigable!")
    foca.hablar()  
