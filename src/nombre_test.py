from nombre import *
#ejercicio1
fichero = "data/frecuencias_nombres.csv"
resultado = leer_frecuencias_nombres(fichero)
for e in resultado[:3]:
    print(e)
for e in resultado[-3:]:
    print(f"Mostrando los 3 últimos: {e}  ")