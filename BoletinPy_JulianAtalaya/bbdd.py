import mariadb
import getpass

def conectar_bbdd(usuario, contrasena):
    try:
        conexion = mariadb.connect(host="localhost", user="root", password="root", database="pedidos")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (usuario, contrasena))
        registros = cursor.fetchall()

        if registros:
            print("Conexión exitosa. username autenticado.")
            for registro in registros:
                print(f"username: {registro[1]}, password: {registro[2]}, email: {registro[3]}")
        else:
            print("username o password incorrectos.")

        cursor.close()
        conexion.close()
    except mariadb.Error as e:
        print(f"Error de conexión: No se pudo conectar a la base de datos. {e}")

usuario = input("Introduce el nombre de username: ")
contrasena = getpass.getpass("Introduce la password: ")

if usuario == "" or contrasena == "":
    print("Por favor, ingresa ambos campos.")
else:
    conectar_bbdd(usuario, contrasena)
