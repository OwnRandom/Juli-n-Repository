from datetime import datetime


def buscar_inmuebles_por_presupuesto(lista_inmuebles, presupuesto):

    año_actual= datetime.now().year

    inmuebles_filtrados = []

    for inmueble in lista_inmuebles:
        antiguedad = año_actual - inmueble['año']
        metros = inmueble['metros']
        habitaciones = inmueble['habitaciones']
        garaje = 1 if inmueble['garaje'] else 0
        zona = inmueble['zona']
        
        # Calcular el precio según la zona
        if zona == 'A':
            precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1 - antiguedad / 100)
        elif zona == 'B':
            precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1 - antiguedad / 100) * 1.5
        else:
            continue  # Si la zona no es A o B, ignoramos el inmueble
        
        # Si el precio es menor o igual al presupuesto, lo añadimos a la lista
        if precio <= presupuesto:
            inmueble_con_precio = inmueble.copy()  # Copiamos el diccionario original
            inmueble_con_precio['precio'] = round(precio, 2)  # Añadimos el precio calculado
            inmuebles_filtrados.append(inmueble_con_precio)
    
    return inmuebles_filtrados

inmuebles = [
    {'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
    {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
    {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
    {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
    {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}
]

presupuesto = 150000  # Cambia el presupuesto según tus necesidades
resultado = buscar_inmuebles_por_presupuesto(inmuebles, presupuesto)

print('Inmuebles filtrados:')
for r in resultado:
    print(r)