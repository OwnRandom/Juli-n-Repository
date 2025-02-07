# Lista de las asignaturas
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua", "Anatomía", "SGE"]

# Lista de las notas (por rellenar)
notas = {}

# Pedir al usuario las notas de cada asignatura
for asignatura in asignaturas:
    while True:
        try:
            # Solicitar la nota al usuario
            nota = float(input(f"Introduce la nota de {asignatura}: "))
            # Comprobar que el numero es valido
            if 0 <= nota <= 10:
                # Almacenar la nota si es válida
                notas[asignatura] = nota
                break
            else:
                print("Por favor, introduce una nota entre 0 y 10.")
                # Control de errores
        except ValueError:
            print("Entrada no válida. Introduce un número.")

# Mostrar las asignaturas con sus notas
print("\nResultados:")
for asignatura, nota in notas.items():
    print(f"En {asignatura} has sacado {nota}.")