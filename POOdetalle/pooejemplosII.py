class Empleado:
    aumento_salario = 1.05 #Variable de clase (comun para todos)

    def __init__(self,nombre,apellido,salario):
        self._nombre = nombre #convencion no accedes directamente
        self.__apellido=apellido #name mangling
        self.salario = salario

    def mostrar_apellido(self):
        return self.__apellido


emp=Empleado("Laura","Lopez",1200)
#print(emp.mostrar_nombre())
print(emp._Empleado__apellido) #name mangling

#empleado1 = Empleado("Carlos",5000)
#empleado2= Empleado("Ana",6000)

#print(empleado1.nombre)
#print(empleado2.nombre)

#print(Empleado.aumento_salario) #Desde la clase
#print(empleado1.aumento_salario) #desde la interface

#Modificando la variable de clase desde  la clase
#Empleado.aumento_salario = 1.10
#print(empleado1.aumento_salario) #Afecta a todos si no se sobreescribe

#Sobrescribiendo en una instancia
#empleado1.aumento_salario=1.20
#print(empleado1.aumento_salario) #solo para la instancia empleado1
#print(empleado2.aumento_salario)

#Usando __dict__ : propiedades del objeto y la clase

#print(empleado1.__dict__) #Mostrar variables propias de la instancia
#print(Empleado.__dict__) #Mostrar atributos y metodos de la clase

#_variable:protegida(convencion)

