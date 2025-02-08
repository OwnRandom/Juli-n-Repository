def calcular_nota_final():
    try:
        # Solicitar calificaciones parciales
        parciales = []
        for i in range(1, 4):
            while True:
                try:
                    calificacion = float(input(f"Ingrese la calificación del parcial {i} (0-10): "))
                    if 0 <= calificacion <= 10:
                        parciales.append(calificacion)
                        break
                    else:
                        print("Error: La calificación debe estar entre 0 y 10.")
                except ValueError:
                    print("Error: Ingrese un número válido.")
        
        # Solicitar calificación del examen final
        while True:
            try:
                examen_final = float(input("Ingrese la calificación del examen final (0-10): "))
                if 0 <= examen_final <= 10:
                    break
                else:
                    print("Error: La calificación debe estar entre 0 y 10.")
            except ValueError:
                print("Error: Ingrese un número válido.")
        
        # Solicitar calificación del trabajo final
        while True:
            try:
                trabajo_final = float(input("Ingrese la calificación del trabajo final (0-10): "))
                if 0 <= trabajo_final <= 10:
                    break
                else:
                    print("Error: La calificación debe estar entre 0 y 10.")
            except ValueError:
                print("Error: Ingrese un número válido.")
        
        # Calcular promedio de parciales
        promedio_parciales = sum(parciales) / len(parciales)
        
        # Calcular calificación final
        calificacion_final = (promedio_parciales * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15)
        
        # Mostrar resultado
        print(f"La calificación final es: {calificacion_final:.2f}")
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")

# Llamar a la función
calcular_nota_final()
