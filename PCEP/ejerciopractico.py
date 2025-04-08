"""
Un dia de compras de Laura
-Fue al Supermercado
-Redecorando su casa
-Ayudado a su primo con su tarea de matematica
"""
#Precio Redondeado al pagar en caja(ceil)
#Precio mas Bajo para una oferta(floor)
#Cortar decimales del presupuesto(trunc)
#Decoracion con flores(factorial)
#Medir la distancia entre dos puntos de la pared(hypot)
#Calcular eñ tamaño de una baldosa cuadrada(sqrt)

import math
print("---Soluciones para el dia de compras de Laura---")
#1.-Redondear Hacia arriba
compra=23.45
print(f"1.Total redondeado a pagar: {math.ceil(compra)}")
#2.-Redondear Hacia abajo
precio_producto=49.55
print(f"2.Precio redondeado para oferta:{math.floor(precio_producto)}")
#3.-Truncar un presupuesto
presupeusto=150.75
print(f"3.Presupuesto sin centavos: {math.trunc(presupeusto)}")
#4.-Arreglo de flores
flores=5
print(f"4.Formas de ordenar 5 flores: {math.factorial(flores)}")
#5.-Distancia de la repisa
horizontal=1.2
vertical=0.8
print(f"5.Longitud de la repisa: {math.hypot(horizontal,vertical):.2f}metros")
#5.- Tamaño de lado de la baldosa
area=2.25
print(f"6.Lado de la Baodosa cuadrada: {math.sqrt(area):.2f}metros")


