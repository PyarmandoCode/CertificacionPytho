"""
- ord (c) convierte un caracter en un valor unicode
- chr (n) convierte un numero unicode en su caracter correspondiente


#print(ord('A')) #65
#print(ord('a')) #97
#print(ord('@')) #64
#print(ord('ñ')) #241

print(chr(65))
print(chr(97))
print(chr(64))
print(chr(241))

"""

"""
indexing, slicing, immutability
"""
#indexing
texto="Python"
#print(texto[0]) #P
#print(texto[-1]) #n
#slicing
#print(texto[0:4]) #Pyt

#immutability
#texto[0]="J"
nuevo = "J" + texto[1:]
#print(nuevo)

"""
iterating through strings, concatenating, multiplying, comparing
(against strings and numbers)
for letra in "Hola":
    print(letra)

nombre="Juan"    
apellido = "Perez"
edad = 29
completo = nombre + " " + apellido + " " + str(edad)
completo1 = nombre,apellido
completo2= f"{nombre} {apellido} {edad}"
print(completo)
print("Hola " * 13)

print("abc" =="abc") #True
print("abc" >"Abc") #True
print("5" < "10") #False
print(int("5")<10) #True
"""
# operators: in, not in
#El operador in comprueba si un string esta dentro de otro
frase="Los lenguajes Python y Java son poderosos"
print("Python" in frase) #True
print("Java" in frase) #False
print("java" not in frase) #True