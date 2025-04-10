
#Funcion random me permite generar numeros aleatorios
#-random.random() .- Devuelve un numero aleatorio en el rango [0.0,1.0]
import random
valor= random.random()
print(f"El Numero aleatorio entre 0 y 1 es {valor}")


#-random.randint().- Devuelve un numero aleatorio entre a y b (ambos incluidos)

import random
numero= random.randint(1,10)
print(f"El Numero Generado entre 1 y 10 es {numero}")

#-random.randrange(start,stop,step).-Devuelve un numero de secuencia como range() pero aleatoriamente

import random
numero= random.randrange(0,20,2)
print(f"Numero aleatorio entre 0 y 10:{numero}")

#-random.uniform(a,b) .- Devuelve un numero flotante aleatorio entre a y b

import random
numero=random.uniform(1.5,5.5)
print(f"Numero Flotante entre 1.5 y 5.5 {numero}")

#-random.choice(lista) .-Selecciona un elemento aleatorio de una secuencia (como una lista)

import random
colores= ["rojo","verde","azul","negro","gris"] #list
color=random.choice(colores)
print(f"Color Elegido {color}")

#-random.choices(poblacion,k=n) .-Devuelve una lista con n elementos aleatorios con reemplazo

import random
nombres=["Ana","Luis","Pedro","Lucia"]
seleccionados=random.choices(nombres,k=3)
print(f"Nombres Aleatorios {seleccionados}")

#-random.sample(poblacion,k=n).- Devuelve n elementos son repetirse(sin reemplazo)

import random
letras= ["A","B","C","D"]
seleccion=random.sample(letras,k=2)
print(f"Seleccion sin repetir {seleccion}")

#-random.shuffle(lista).-Mezcla los elementos en el lugar(in-place)

import random
cartas=["as","rey","reyna","joker"]
random.shuffle(cartas)
print(f"Cartas mezcladas ,{cartas}")

#-random.seed(valor) .-Esteblece un semilla inicial para el generador de numeros aleatorios.

import random
random.seed(42) #semilla fija
print("Primer Valor", random.randint(1,100))
print("Segundo Valor",random.randint(1,100))










