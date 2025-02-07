# Diccionario para almacenar los contactos de la agenda
agenda = {}

def añadir_o_modificar():
    nombre = input("Introduce el nombre del contacto: ")
    if nombre in agenda:
        print(f"{nombre} ya esta en la agenda. Su telefono es: {agenda[nombre]}")
        modificar = input("¿Quieres modificar el telefono? (si/no): ").lower()
        if modificar == 'si':
            telefono = input("Introduce el nuevo teléfono: ")
            agenda[nombre] = telefono
            print(f"El telefono de {nombre} ha sido actualizado a {telefono}.")
    else:
        telefono = input(f"{nombre} no esta en la agenda. Introduce el telefono: ")
        agenda[nombre] = telefono
        print(f"{nombre} ha sido añadido a la agenda.")

def buscar():
    busqueda = input("Introduce la cadena a buscar: ")
    encontrados = [nombre for nombre in agenda if nombre.lower().startswith(busqueda.lower())]
    
    if encontrados:
        print("Contactos encontrados:")
        for nombre in encontrados:
            print(f"{nombre}: {agenda[nombre]}")
    else:
        print("No se encontraron contactos que empiecen con esa cadena.")

def borrar():
    nombre = input("Introduce el nombre del contacto a borrar: ")
    if nombre in agenda:
        confirmacion = input(f"¿Estas seguro de que quieres borrar a {nombre}? (si/no): ").lower()
        if confirmacion == 'si':
            del agenda[nombre]
            print(f"{nombre} ha sido borrado de la agenda.")
        else:
            print("No se ha borrado el contacto.")
    else:
        print(f"{nombre} no está en la agenda.")

def listar():
    if agenda:
        print("Contactos en la agenda:")
        for nombre, telefono in agenda.items():
            print(f"{nombre}: {telefono}")
    else:
        print("La agenda esta vacia.")

def menu():
    while True:
        print("\nMenu:")
        print("1. Añadir/Modificar")
        print("2. Buscar")
        print("3. Borrar")
        print("4. Listar")
        print("5. Salir")
        
        opcion = input("Selecciona una opcion (1-5): ")
        
        if opcion == '1':
            añadir_o_modificar()
        elif opcion == '2':
            buscar()
        elif opcion == '3':
            borrar()
        elif opcion == '4':
            listar()
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción invalida. Por favor, selecciona una opcion entre 1 y 5.")

# Ejecutamos el programa
if __name__ == "__main__":
    menu()
