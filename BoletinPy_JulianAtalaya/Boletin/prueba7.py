class Universidad:
    def __init__(self, nombre):
        self.nombre = nombre


class Carrera:
    def __init__(self, especialidad):
        self.especialidad = especialidad


class Estudiante:
    def __init__(self, nombre, edad, universidad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.universidad = universidad
        self.carrera = carrera

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Universidad: {self.universidad.nombre}")
        print(f"Especialidad: {self.carrera.especialidad}")


if __name__ == "__main__":
    universidad = Universidad("Universidad Nacional de Ingeniería")

    carrera = Carrera("Ingeniería de Sistemas")

    persona = Estudiante("Julian", 20, universidad, carrera)

    persona.mostrar_informacion()
