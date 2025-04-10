# Lista de estudiantes participantes
estudiantes = ['Andrea', 'Carlos', 'Lucía', 'Miguel', 'Sofía', 'Diego']

import random
#Seleccionar al ganador aleatoria
random.seed(2025)
#ganador = random.choice(estudiantes)
premios = random.sample(estudiantes,k=3)
print(f"El Ganador del premio es  {premios}")

"""
-Juegos (dados,ruleta,carta)
-Simulacion de clientes llegando a una tienda
-Generacion de contraseñas seguras
-Pregunras aleatorias en un quiz
"""