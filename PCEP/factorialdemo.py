"""
n! = n × (n-1) × (n-2) × ... × 1
Por ejemplo, 5! = 5 × 4 × 3 × 2 × 1 = 120
"""
import math
#Ingrese el Numero
num = int(input("Que Numero deseas Factorizar?"))
def factorial_for(n):
    resultado=1
    for i in range(1,n+1):
        resultado  *=i
    return resultado

def factorial_math(n):
    return math.factorial(n)

#Mostrar los resultados
print("\n  Factorial Usando for",factorial_for(num))
print("\n  Factorial Usando match",factorial_math(num))