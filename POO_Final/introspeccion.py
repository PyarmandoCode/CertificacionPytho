class Animal:
    pass

class Perro(Animal):
    def ladrar(self):
        print("Guau!")

#Creamos una instancia
mi_perro=Perro()

#Introspeccion con hasattr()
#hasattr es una funcion incorporada de python que se usa para verificar si un 
#objeto tiene un atributo especifico(propiedad,metodo o variable)
#devuelve true si el atributo existe y false si no
#print("¿Tiene 'ladrar'?:",hasattr(mi_perro,'ladrar')) #true es un metodo del objeto
#print("¿Tiene '__name__'?:",hasattr(mi_perro,'__name__'))#false no esta en el objeto esa clase

#Analizando la clase
#print("Nombre de la clase:",Perro.__name__) #Perro
#print("Modulo donde esta definida",Perro.__module__) #__main__
#print("Clase base (herencia)",Perro.__bases__) #(class '__main__Animal)

#Herencia Simple y uso de isinstance()
class Animal:
    def hablar(self):
        return "Algun Sonido"
    

class Perro(Animal):
    def hablar(self):
        return "Guau"
    
   

class Gato(Animal):
    def hablar(self):
        return "Miau" 
    
#Uso de isinstance
firulais = Perro()
#print(isinstance(firulais,Perro)) #True
#print(isinstance(firulais,Animal)) #True



#polimorfismo
def hazlo_hablar(animal):
    print(animal.hablar()) #Poliformismo misma funcion , comportamiento distinto

#hazlo_hablar(Perro())
#hazlo_hablar(Gato())

#Sobreescritura de metodos (overriding) 
class Perro(Animal):
    def __str__(self):
        return "Soy un perro que dice:"+self.hablar()

#print(str(Perro()))    

#Operadores IS y NOT IS

a=Perro()
b=a
c=Perro()
print(a is b) #true (mismo objeto en memoria)
print(a is not c)#true /aunque sean del mismo tipo, no son del mismo objeto
    
        