# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 13:11:40 2024

@author: dano_
"""
import json

import requests

# API Key de NY Times
API_KEY = 'ZshS04fwd6atH6SEcZ67Nfy8aigRXhwh'

# Función para obtener las listas de Best Sellers disponibles
def obtener_listas():
    url = f'https://api.nytimes.com/svc/books/v3/lists/names.json?api-key={API_KEY}'
    response = requests.get(url)
    data = response.json()
    listas = {lista['list_name']: lista['display_name'] for lista in data['results']}
    return listas

# Función para obtener los Best Sellers de una lista y fecha específica
def obtener_best_sellers(lista, fecha=None):
    if fecha:
        url = f'https://api.nytimes.com/svc/books/v3/lists/{fecha}/{lista}.json?api-key={API_KEY}'
    else:
        url = f'https://api.nytimes.com/svc/books/v3/lists/current/{lista}.json?api-key={API_KEY}'
    
    response = requests.get(url)
    data = response.json()
    best_sellers = data['results']['books']
    return best_sellers

# Función para filtrar libros por precio y rango de edad
def filtrar_libros(libros, precio_max=None, rango_edad=None):
    libros_filtrados = []
    for libro in libros:
        if precio_max and float(libro['price']) > precio_max:
            continue
        if rango_edad and rango_edad not in libro['age_group']:
            continue
        libros_filtrados.append(libro)
    return libros_filtrados

# Interfaz de usuario
def main():
    listas = obtener_listas()
    
    # Pedir al usuario que seleccione una lista
    print("Listas de Best Sellers disponibles:")
    for i, (key, value) in enumerate(listas.items()):
        print(f"{i+1}. {value} ({key})")
    
    lista_idx = int(input("Seleccione el número de la lista que desea consultar: ")) - 1
    lista_seleccionada = list(listas.keys())[lista_idx]
    
    # Pedir al usuario que seleccione la fecha
    fecha = input("Ingrese la fecha en formato AAAA-MM-DD de el titulo de su interés (dejar vacío para la lista actual): ")
    
    # Obtener los Best Sellers
    best_sellers = obtener_best_sellers(lista_seleccionada, fecha)
    
    # Pedir al usuario que seleccione el precio máximo
    precio_max = input("Ingrese el precio máximo del libro (dejar vacío para omitir): ")
    precio_max = float(precio_max) if precio_max else None
    
    # Pedir al usuario que seleccione el rango de edad
    rango_edad = input("Ingrese el rango de edad del libro (dejar vacío para omitir): ")
    
    # Filtrar libros
    libros_filtrados = filtrar_libros(best_sellers, precio_max, rango_edad)
    
    # Mostrar resultados
    if libros_filtrados:
        print("\nLibros encontrados:")
        for libro in libros_filtrados:
            print(f"Título: {libro['title']}, Autor: {libro['author']}, Precio: ${libro['price']}, Rango de edad: {libro['age_group']}")
    else:
        print("No se encontraron libros que cumplan con los criterios especificados.")

if __name__ == "__main__":
    main()

