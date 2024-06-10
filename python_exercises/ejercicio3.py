# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 23:28:15 2024

@author: dano_
"""

import pandas as pd

df_promociones = pd.read_csv('C:/Users/nama_/Downloads/Examen IBSO_1_24-4-2024/Prueba_Promociones.csv')
ruta = 'C:/Users/nama_/Downloads/Examen IBSO_1_24-4-2024/Prueba_Promociones.csv'

from datetime import datetime, timedelta

import pandas as pd


# Función para cargar el archivo CSV
def cargar_csv(ruta):
    try:
        df = pd.read_csv(ruta)
        return df
    except Exception as e:
        print(f"Error al cargar el archivo CSV: {e}")
        return None

# Función para pedir y validar las entradas del usuario
def pedir_entradas():
    # Validación de la fecha de inicio
    while True:
        fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD) o deje vacío: ")
        if fecha_inicio == "":
            fecha_inicio = None
            break
        try:
            fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
            break
        except ValueError:
            print("Formato de fecha no válido. Intente nuevamente.")

    # Validación de la fecha de fin
    while True:
        fecha_fin = input("Ingrese la fecha de fin (YYYY-MM-DD) o deje vacío: ")
        if fecha_fin == "":
            fecha_fin = None
            break
        try:
            fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d")
            break
        except ValueError:
            print("Formato de fecha no válido. Intente nuevamente.")

    # Validación de la categoría
    while True:
        categoria = input("Ingrese la categoría o deje vacío: ")
        if categoria == "" or isinstance(categoria, str):
            break
        else:
            print("Categoría no válida. Debe ser una cadena de texto.")

    # Validación del uso
    while True:
        uso = input("Ingrese el uso o deje vacío: ")
        if uso == "" or isinstance(uso, str):
            break
        else:
            print("Uso no válido. Debe ser una cadena de texto.")

    # Validación del SKU
    while True:
        sku = input("Ingrese el SKU: ")
        if sku and isinstance(sku, str):
            break
        else:
            print("SKU no válido. Debe ser una cadena de texto no vacía.")

    # Validación del porcentaje
    while True:
        porcentaje = input("Ingrese el porcentaje (%): ")
        try:
            porcentaje = float(porcentaje)
            break
        except ValueError:
            print("Porcentaje no válido. Debe ser un número decimal.")

    # Validación del inventario inicial
    while True:
        inventario_inicial = input("Ingrese el inventario inicial: ")
        try:
            inventario_inicial = int(inventario_inicial)
            break
        except ValueError:
            print("Inventario inicial no válido. Debe ser un número entero.")

    return fecha_inicio, fecha_fin, categoria, uso, sku, porcentaje, inventario_inicial

# Ruta del archivo CSV
ruta_csv = 'C:/Users/nama_/Downloads/Examen IBSO_1_24-4-2024/Prueba_Promociones.csv'
# Cargar el archivo CSV
df = cargar_csv(ruta_csv)
if df is not None:
    print("Archivo CSV cargado exitosamente.")
    # Mostrar algunas filas del dataframe para verificar
    print(df.head())

    # Pedir y validar entradas del usuario
    entradas_usuario = pedir_entradas()
    fecha_inicio, fecha_fin, categoria, uso, sku, porcentaje, inventario_inicial = entradas_usuario

    # Generar una nueva columna con el número de semana
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    df['Semana'] = df['Fecha'].dt.isocalendar().week

    # Filtrar datos según las condiciones dadas
    if fecha_inicio and fecha_fin:
        df_filtrado = df[(df['Fecha'] >= fecha_inicio) & (df['Fecha'] <= fecha_fin)]
    elif fecha_inicio:
        df_filtrado = df[df['Fecha'] >= fecha_inicio]
    elif fecha_fin:
        df_filtrado = df[df['Fecha'] <= fecha_fin]
    else:
        df_filtrado = df.copy()

    if uso:
        df_filtrado = df_filtrado[df_filtrado['Uso'] == uso]
    elif categoria:
        df_filtrado = df_filtrado[df_filtrado['Categoría'] == categoria]

    df_filtrado = df_filtrado[df_filtrado['Modelo'] != 'real']

    # Aplicar el porcentaje de crecimiento
    df_filtrado['Piezas'] = df_filtrado['Piezas'] * (1 + porcentaje / 100)

    # Generar nuevo dataframe con información del SKU seleccionado
    df_sku = df[df['SKU'] == sku].copy()
    df_sku['Fecha'] = pd.to_datetime(df_sku['Fecha'])
    df_sku = df_sku.sort_values(by='Fecha')

    # Calcular el consumo de inventario
    inventario = inventario_inicial
    df_sku['Inventario'] = inventario_inicial
    primera_fecha_negativa = None

    for idx, row in df_sku.iterrows():
        inventario -= row['Piezas']
        df_sku.at[idx, 'Inventario'] = inventario
        if inventario < 0 and primera_fecha_negativa is None:
            primera_fecha_negativa = row['Fecha']

    print(f"Primera fecha en la que el inventario se vuelve negativo: {primera_fecha_negativa}")
    print(df_sku)

else:
    print("No se pudo cargar el archivo CSV.")
