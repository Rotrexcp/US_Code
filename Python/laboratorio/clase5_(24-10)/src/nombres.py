from typing import NamedTuple
from datetime import date
import csv

'''reciclar para el 4 el 2, para el 5 y 6 el 3'''

FrecuenciaNombre = NamedTuple("FrecuenciaNombre", [("año",date),("nombre",str),("frecuencia",int),("genero",str)])


def leer_frecuencias_nombres(nombres_csv:str)->list[FrecuenciaNombre]:
    with open(nombres_csv, encoding="utf-8") as f:
        lista_nombres=[]
        lector=csv.reader(f)
        next(lector)
    
        for año,nombre,frecuencia,genero in lector:
            año=int(año)
            nombre=str(nombre)
            frecuencia=int(frecuencia)
            genero=str(genero)

            r=FrecuenciaNombre(año,nombre,frecuencia,genero)

            lista_nombres.append(r)

    return lista_nombres


def filtrar_por_genero(lista_fichero:list[FrecuenciaNombre], genero:str)->list[FrecuenciaNombre]:
    lista_por_genero=[]

    for registro in lista_fichero:
        if genero == registro.genero:
            tupla = (registro.año, registro.nombre, registro.frecuencia)
            lista_por_genero.append(tupla)

    return lista_por_genero


def calcular_nombres(lista_fichero: list[FrecuenciaNombre], genero: str) -> set[str]:
    conjunto_nombres = set()

    # Reutilizamos la función filtrar_por_genero para obtener las tuplas
    filtro = filtrar_por_genero(lista_fichero, genero)

    # Extraer los nombres de las tuplas (año, nombre, frecuencia)
    for tupla in filtro:
        año, nombre, frecuencia = tupla  # Descomponer la tupla explícitamente      or: _,nombre,_
        conjunto_nombres.add(nombre)     # Solo trabajamos con el nombre

    return conjunto_nombres

'''conjunto_nombres = set()

# Reutilizamos la función filtrar_por_genero para obtener las tuplas
filtro = filtrar_por_genero(lista_fichero, genero)

# Extraer los nombres de las tuplas (año, nombre, frecuencia)
for _, nombre, _ in filtro:
    conjunto_nombres.add(nombre)

return conjunto_nombres'''


def calcular_top_nombres_de_año(lista_fichero: list[FrecuenciaNombre], año:int, num_limite:int, genero:str)->list[str, int]:
    lista_top_nombres=[]