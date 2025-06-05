#       A
#      / \
#     B   C
#      \ /
#       D

#Usar MRO(Orden de resolucion de metodos)

class A:
    def saludar(self):
        return "Hola desde A"

class B(A):
    def saludar(self):
        return "Hola desde B"
class C(A):
    def saludar(self):
        return "Hola desde C"    

class D(B,C):
    pass

d=D()

print(d.saludar())

print(D.__mro__)

class Persona:
    def __init__(self,nombre="Armando",edad=37):
        self.nombre=nombre
        self.edad=edad

#Creas el objeto(invocar al constructor)
p1=Persona()
#Acceder a los atributos
print(p1.nombre)
print(p1.edad)
