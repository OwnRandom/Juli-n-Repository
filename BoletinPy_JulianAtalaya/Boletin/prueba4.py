class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"


class Estudiante(Persona):
    def __init__(self, nombre, apellido, edad, carrera):
        super().__init__(nombre, apellido)
        self.edad = edad
        self.carrera = carrera

    def mostrar_carrera(self):
        return f"{self.nombre_completo()} está cursando la carrera de {self.carrera}."
    
if __name__ == "__main__":

    estudiante = Estudiante("Julian", "Atalaya", 20, "Desarrollo de Aplicaciones Multiplataforma")

    print("Nombre completo:", estudiante.nombre_completo())

    print(estudiante.mostrar_carrera())