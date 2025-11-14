import csv
from collections import namedtuple

FrecuenciaNombre = namedtuple('FrecuenciaNombre', 'año,nombre,frecuencia,genero')

def leer_frecuencias_nombres(fichero):
    with open(fichero, encoding ="utf-8") as f:
        lector = csv.reader(f)
        next(lector)
        lista = []
        for año, nombre, frecuencia, genero in lector:
            año = int(año)
            frecuencia = int(frecuencia)
            tupla = FrecuenciaNombre(año, nombre, frecuencia, genero)
            lista.append(tupla)
    return lista
