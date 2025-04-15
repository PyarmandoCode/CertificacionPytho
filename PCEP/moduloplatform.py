"""
Modulo Platform
-Este modulo sirve para obtener informacion sobre el sistema operativo , arquitectura de la mquina  , version de python

"""
import platform

#Nombre del sistema operativo
print("Sistema Operativo",platform.system())
#Version del Sistema Operativo
print("Version del Sistema Operativo",platform.version())
#Tipo de Maquina
print("Tipo de Maquina",platform.machine())
#Procesador (Por Ejemplo , 'Intel65 Family 6 Model')
print("Procesador",platform.processor())
#Nombre completo del sistema  (mas detalladro que system() y version())
print("Plataforma completa",platform.platform())
#Version de Python
print("Version de Python",platform.python_version_tuple())