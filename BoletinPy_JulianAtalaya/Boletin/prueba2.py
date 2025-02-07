class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def cumpleaños(self):
        self.edad += 1
        print(f"Feliz cumpleaños ahora tienes: {self.edad}")
        

    def mostrar_datos(self):
        print(f"Nombre de la persona: {self.nombre}")
        print(f"Edad de la persona: {self.edad}")

if __name__ == "__main__":
    persona = Persona("julian", 19)

    persona.mostrar_datos()
    persona.cumpleaños()