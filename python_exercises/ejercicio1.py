# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 20:52:32 2024

@author: dano_
"""
# Definir el diccionario con los datos climáticos
datos_climaticos = {
    'Ciudad de México': [15, 16, 17, 18, 19, 20, 21],
    'Guadalajara': [25, 26, 27, 28, 29, 30, 31],
    'Monterrey': [22, 23, 24, 25, 26, 27, 28],
    'Cancún': [30, 31, 32, 33, 34, 35, 36],
    'Tijuana': [18, 19, 20, 21, 22, 23, 24]
}

# Calcular estadísticas de temperatura
estadisticas = {}
for ciudad, temperaturas in datos_climaticos.items():
    temp_promedio = sum(temperaturas) / len(temperaturas)
    temp_max = max(temperaturas)
    temp_min = min(temperaturas)
    estadisticas[ciudad] = {
        'Promedio': temp_promedio,
        'Máxima': temp_max,
        'Mínima': temp_min
    }

# Determinar la ciudad con la temperatura promedio más alta y más baja
ciudad_temp_mas_alta = max(estadisticas, key=lambda x: estadisticas[x]['Promedio'])
ciudad_temp_mas_baja = min(estadisticas, key=lambda x: estadisticas[x]['Promedio'])

# Mostrar las estadísticas y resultados
print("Estadísticas de temperaturas:")
for ciudad, stats in estadisticas.items():
    print(f"{ciudad}: Promedio={stats['Promedio']}°C, Máxima={stats['Máxima']}°C, Mínima={stats['Mínima']}°C")

print(f"\nLa ciudad con la temperatura promedio más alta es {ciudad_temp_mas_alta} con {estadisticas[ciudad_temp_mas_alta]['Promedio']}°C")
print(f"La ciudad con la temperatura promedio más baja es {ciudad_temp_mas_baja} con {estadisticas[ciudad_temp_mas_baja]['Promedio']}°C")
