#ejercicio 1
class Estudiante:
    def __init__(self, nombre, nota):

        self.nombre = nombre
        self.nota = nota

    def imprimir_datos(self):
        
        print(f"Nombre del estudiante: {self.nombre}")
        print(f"Nota del estudiante: {self.nota}")

    def mostrar_resultado(self):

        if self.nota >= 5:
            print(f"{self.nombre} ha aprobado.")
        else:
            print(f"{self.nombre} ha suspendido.")


if __name__ == "__main__":

    estudiante = Estudiante("Julian", 7.5)

    estudiante.imprimir_datos();
    estudiante.mostrar_resultado();
