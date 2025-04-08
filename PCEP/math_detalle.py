import math
#print(dir(math))
"""
Funciones del modulo math
-ceil() .- Redondea hacia arriba al entero mas cercano
numero=4.3
resultado=math.ceil(numero)
print(f"math.ceil({numero}) = {resultado}") # 5
-floor().- Redondea hacia abajo al entero mas cercano 
numero = 4.7
resultado=math.floor(numero)
print(f'math.floor({numero})={resultado}') #4
-trunc().-Eliminar la parte decimal (trunca)
numero= -4.8
resultado=math.trunc(numero)
print(f"math.truc({numero})= {resultado}") # -4
-factorial().-Calcular el factorial de un numerom positivo
numero=5
resultado=math.factorial(numero)
print(f"math.factorial({numero}) = {resultado}")
-hypot()
cateto1 = 3
cateto2 = 4
resultado = math.hypot(cateto1,cateto2)
print(f"math.hypot({cateto1} , {cateto2}) = {resultado}") # 5.0
-sqrt()
numero = 16
resultado = math.sqrt(numero)
print(f"math.sqrt({numero}) = {resultado}") 
"""
#factorial es el producto de todos los numeros enteros positicos desde 1 hasta n
# n!=n x (n -1)  x (n -2) x ..x 3x2x1)
#3!=3*2*1 =6
#5!=5*4*3*2*1=120
#1!=1
def factorial(n):
    """Usando un bucle iterativa"""
    resultado=1
    for i in range(1,n+1):
        resultado *=i
    return resultado    

#numero=1
#print(f"El Factorial de {numero} es {factorial(numero)}")

def factorial2(n):
    """Hallar el Factorial ustilizando recursividad"""
    if n==0 or n==1:
        return 1
    else:
        return n* factorial2(n-1)

#numero=5
#print(f"El Factorial de {numero} es {factorial2(numero)} ")    

"""
hipotenusa = es el lado mas largo de un trianuglo rectangulo y se calcula usando el teorema de pitagoras
 hipotenusa2 = cateto21 + cateto22
"""


def calcular_hipotenusa(cateto1,cateto2):
    return math.sqrt(cateto1**2+cateto2**2)

c1=3
c2=4
hipotenusa=calcular_hipotenusa(c1,c2)
#print(f"La Hipotenusa es : {hipotenusa}")


