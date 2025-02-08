import tkinter as tk
from tkinter import ttk
import time
import threading

def actualizar_cronometro():
    global corriendo, tiempo
    while corriendo:
        time.sleep(1)
        tiempo += 1
        horas, resto = divmod(tiempo, 3600)
        minutos, segundos = divmod(resto, 60)
        cronometro_label.config(text=f"{horas:02}:{minutos:02}:{segundos:02}")

def iniciar_cronometro():
    global corriendo
    if not corriendo:
        corriendo = True
        threading.Thread(target=actualizar_cronometro, daemon=True).start()

def reiniciar_cronometro():
    global tiempo, corriendo
    corriendo = False
    tiempo = 0
    cronometro_label.config(text="00:00:00")

def actualizar_temporizador():
    global temporizador_corriendo, temporizador_tiempo
    while temporizador_corriendo and temporizador_tiempo > 0:
        time.sleep(1)
        temporizador_tiempo -= 1
        horas, resto = divmod(temporizador_tiempo, 3600)
        minutos, segundos = divmod(resto, 60)
        temporizador_label.config(text=f"{horas:02}:{minutos:02}:{segundos:02}")
        
    if temporizador_tiempo == 0:
        temporizador_label.config(text="¡Tiempo terminado!")

def iniciar_temporizador():
    global temporizador_corriendo, temporizador_tiempo
    if not temporizador_corriendo:
        temporizador_corriendo = True
        temporizador_tiempo = 5 * 60  # 5 minutos en segundos
        threading.Thread(target=actualizar_temporizador, daemon=True).start()

def reiniciar_temporizador():
    global temporizador_corriendo, temporizador_tiempo
    temporizador_corriendo = False
    temporizador_tiempo = 5 * 60
    temporizador_label.config(text="05:00")

# Configuración de la ventana
root = tk.Tk()
root.title("Cronómetro y Temporizador")

# Variables globales
tiempo = 0
corriendo = False
temporizador_tiempo = 5 * 60
temporizador_corriendo = False

# Cronómetro
cronometro_label = ttk.Label(root, text="00:00:00", font=("Arial", 30))
cronometro_label.pack()

btn_iniciar_cronometro = ttk.Button(root, text="Iniciar Cronómetro", command=iniciar_cronometro)
btn_iniciar_cronometro.pack()

btn_reiniciar_cronometro = ttk.Button(root, text="Reiniciar Cronómetro", command=reiniciar_cronometro)
btn_reiniciar_cronometro.pack()

# Temporizador
temporizador_label = ttk.Label(root, text="05:00", font=("Arial", 30))
temporizador_label.pack()

btn_iniciar_temporizador = ttk.Button(root, text="Iniciar Temporizador", command=iniciar_temporizador)
btn_iniciar_temporizador.pack()

btn_reiniciar_temporizador = ttk.Button(root, text="Reiniciar Temporizador", command=reiniciar_temporizador)
btn_reiniciar_temporizador.pack()

# Iniciar aplicación
root.mainloop()
