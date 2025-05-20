"""
-Una clase es un molde o plantilla que define como seran los objetos.
En ella se agrupan propiedades(atributos) y comportaminetos (metodos)
-Objeto es Una Instancia real de una clase. Puedes tener muchos objetos de una misma clase
-Propiedad (Atributo) son  las variables que pertenecen a un objeto . Se definene e el metodo __init__
-Metodos(method) Es una funcion dentro de una clase. Representa un comportamiento del objeto
-Encapsulamiento  Es ocultar los detalles internos del objeto y proteger los datos.Se logra usando atributos privados(__nombre) y metodos de acceso (getters/setters)
-Herencia Permite que una clase(subclase) herede laspropiedades y metodos de otra clase (superclase)
-Superclase Es la clase base de la cual heredan otras clase.
-Subclase Es la clase que hereda de otra.

"""

class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre #propiedad
        self.edad=edad #propiedad
    def saludar(self):
        print(f"Hola Soy {self.nombre} y tengo {self.edad} años")    
    

persona1 = Persona("Juan",30)
persona2 = Persona("Maria",28)
#print(persona1.nombre)
#print(persona2.edad)
#print(persona1.__dict__)
#persona1.saludar()


class CuentaBancaria:
    def __init__(self,saldo):
        self.__saldo=saldo #atributo privado

    def obtener_saldo(self):
        return self.__saldo

    def depositar(self,cantidad):
        if cantidad>0:
            self.__saldo +=cantidad


cuenta = CuentaBancaria(1000)
cuenta.depositar(500)
#print(cuenta.obtener_saldo())

class Animal:
    def __init__(self,nombre):
        self.nombre=nombre
    def hablar(self):
        print("Hace un Sonido")    

class Perro(Animal): #Hereda de Animal o la superclase o la clase padre
    def hablar(self):
        print("Guau!!")


perro= Perro("Firulais")    
perro.hablar()
    