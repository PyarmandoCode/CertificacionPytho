"""
Una Excepcion es un error que ocurre durante la ejecuccion de un programa y que interrumpe el flujo normal .amenos que sea manejado adecuadamente

Excepcion             Descripcion
==========================================================
ZeroDivisionError	División entre cero
ValueError	        Valor incorrecto para una operación
TypeError	        Tipo de dato incorrecto
IndexError	        Índice fuera de rango en listas
KeyError	        Clave inexistente en un diccionario
AssertionError	    Falla en una afirmación assert
============================================================

try:
    print("Inicio")
    x= 10 / 0 #Esto lanzara una excepcion : ZeroDivisionError
except ZeroDivisionError:
    print("No Puedes dividir entre cero")    
    print("Fin")
"""

"""
1.>except, except

try:
    print("Inicio")
    x= 10 / 0 #Esto lanzara una excepcion : ZeroDivisionError
except ZeroDivisionError:
    print("No Puedes dividir entre cero")    
    print("Fin")

except generico (no recomendado)
  
try:
    x = int("Hola")
except:
    print("Ocurrio un errror (Tipo desconocido)")    

"""

"""
try:
    x= 5 / 5
except:
    print("Error")    
else:
    print(f"No Hubo un error Resultado {x}")    
"""

"""
Multiples excepciones

try:
    x= int("abc")
except (ValueError,TypeError):
    print("Valor o tipo incorrecto")
"""
"""
Jerarquia de Excepciones

BaseException
 └── Exception
      ├── ArithmeticError
      │    └── ZeroDivisionError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      └── ValueError
"""

"""
try:
    lst=[1,2]
    print(lst[3])
except IndexError:
    print("Indice fuera de rango")    
"""    

"""
Ejemplo con raise

def dividir(a,b):
    if b==0:
        raise ValueError("No se puede dividir entre cero")
    return a / b


try:
    raise TypeError("Error de Tipo")
except TypeError as e:
    print(f"Capturando {e}")
    raise #Relanza la excepcion

"""

"""
assert
"""

x = -5
assert x>0, "x debe ser mayor a cero"
