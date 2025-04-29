import sys
import mi_paquete
from mi_paquete.utilidades import contar_palabras

print(mi_paquete.suma(10,5))
print(contar_palabras("Hola mundo desde Python"))

#Imprimir el nombre del archivo
print(f"Este archivo se llama :{__name__}")
print(sys.path)

"""
nested packages
-Son carpetas con __init__.py hace que los paquetes sean validos
-Si no tienes __init__.py PYTHON NO  lo trata como paquete
 como un Arbol de directorio de Windows(Directory Trees)
"""