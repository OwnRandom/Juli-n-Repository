import tkinter as tk
from tkinter import messagebox
import mariadb

# Configuración de la base de datos
db_config = {
    "host": "juanan.me",
    "user": "escuela",
    "password": "escuela",
    "database": "escuela"
}

# Conectar con la base de datos
try:
    conn = mariadb.connect(**db_config)
    cursor = conn.cursor()
except mariadb.Error as e:
    messagebox.showerror("Error", f"Error al conectar con la base de datos: {e}")
    exit()

# Función para cargar los estudiantes en la lista
def cargar_estudiantes():
    lista.delete(*lista.get_children())
    cursor.execute("SELECT id, nombre, edad, curso FROM estudiantes")
    for row in cursor.fetchall():
        lista.insert("", "end", values=row)

# Función para agregar un nuevo estudiante
def agregar_estudiante():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    curso = entry_curso.get()
    if nombre and edad and curso:
        cursor.execute("INSERT INTO estudiantes (nombre, edad, curso) VALUES (?, ?, ?)", (nombre, edad, curso))
        conn.commit()
        cargar_estudiantes()
        limpiar_campos()
    else:
        messagebox.showerror("Error", "Todos los campos son obligatorios")

# Función para seleccionar un estudiante de la lista
def seleccionar_estudiante(event):
    seleccion = lista.selection()
    if seleccion:
        datos = lista.item(seleccion[0], "values")
        entry_id.config(state="normal")
        entry_id.delete(0, tk.END)
        entry_id.insert(0, datos[0])
        entry_id.config(state="disabled")
        entry_nombre.delete(0, tk.END)
        entry_nombre.insert(0, datos[1])
        entry_edad.delete(0, tk.END)
        entry_edad.insert(0, datos[2])
        entry_curso.delete(0, tk.END)
        entry_curso.insert(0, datos[3])

# Función para actualizar un estudiante
def actualizar_estudiante():
    id_estudiante = entry_id.get()
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    curso = entry_curso.get()
    if id_estudiante and nombre and edad and curso:
        cursor.execute("UPDATE estudiantes SET nombre=?, edad=?, curso=? WHERE id=?", (nombre, edad, curso, id_estudiante))
        conn.commit()
        cargar_estudiantes()
        limpiar_campos()
    else:
        messagebox.showerror("Error", "Todos los campos son obligatorios")

# Función para eliminar un estudiante
def eliminar_estudiante():
    id_estudiante = entry_id.get()
    if id_estudiante:
        cursor.execute("DELETE FROM estudiantes WHERE id=?", (id_estudiante,))
        conn.commit()
        cargar_estudiantes()
        limpiar_campos()
    else:
        messagebox.showerror("Error", "Selecciona un estudiante para eliminar")

# Función para limpiar los campos de entrada
def limpiar_campos():
    entry_id.config(state="normal")
    entry_id.delete(0, tk.END)
    entry_id.config(state="disabled")
    entry_nombre.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_curso.delete(0, tk.END)

# Crear la ventana principal
tk_root = tk.Tk()
tk_root.title("Gestión de Estudiantes")
tk_root.configure(bg="black")

# Estilos generales
label_style = {"bg": "black", "fg": "white", "font": ("Arial", 12)}
entry_style = {"bg": "#333", "fg": "white", "insertbackground": "white", "font": ("Arial", 12)}
button_style = {"bg": "#555", "fg": "white", "font": ("Arial", 12, "bold"), "width": 20, "height": 2}

# Campos de entrada
tk.Label(tk_root, text="ID:", **label_style).grid(row=0, column=0, padx=10, pady=5)
entry_id = tk.Entry(tk_root, state="disabled", **entry_style)
entry_id.grid(row=0, column=1, padx=10, pady=5)

tk.Label(tk_root, text="Nombre:", **label_style).grid(row=1, column=0, padx=10, pady=5)
entry_nombre = tk.Entry(tk_root, **entry_style)
entry_nombre.grid(row=1, column=1, padx=10, pady=5)

tk.Label(tk_root, text="Edad:", **label_style).grid(row=2, column=0, padx=10, pady=5)
entry_edad = tk.Entry(tk_root, **entry_style)
entry_edad.grid(row=2, column=1, padx=10, pady=5)

tk.Label(tk_root, text="Curso:", **label_style).grid(row=3, column=0, padx=10, pady=5)
entry_curso = tk.Entry(tk_root, **entry_style)
entry_curso.grid(row=3, column=1, padx=10, pady=5)

# Botones
tk.Button(tk_root, text="Agregar Estudiante", command=agregar_estudiante, **button_style).grid(row=4, column=0, columnspan=2, pady=5)
tk.Button(tk_root, text="Actualizar Estudiante", command=actualizar_estudiante, **button_style).grid(row=5, column=0, columnspan=2, pady=5)
tk.Button(tk_root, text="Eliminar Estudiante", command=eliminar_estudiante, **button_style).grid(row=6, column=0, columnspan=2, pady=5)
tk.Button(tk_root, text="Limpiar Campos", command=limpiar_campos, **button_style).grid(row=7, column=0, columnspan=2, pady=5)

# Lista de estudiantes mejorada
from tkinter import ttk
lista = ttk.Treeview(tk_root, columns=("ID", "Nombre", "Edad", "Curso"), show="headings", height=10)
lista.heading("ID", text="ID")
lista.heading("Nombre", text="Nombre")
lista.heading("Edad", text="Edad")
lista.heading("Curso", text="Curso")
lista.column("ID", width=50, anchor="center")
lista.column("Nombre", width=150, anchor="center")
lista.column("Edad", width=50, anchor="center")
lista.column("Curso", width=100, anchor="center")
lista.grid(row=8, column=0, columnspan=2, pady=10)
lista.bind("<ButtonRelease-1>", seleccionar_estudiante)

# Cargar los estudiantes al iniciar
cargar_estudiantes()

# Ejecutar la aplicación
tk_root.mainloop()

# Cerrar la conexión
cursor.close()
conn.close()
