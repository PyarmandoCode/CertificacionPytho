#Clase
class Muñeco:
    #Constructor
    def __init__(self,sexo,edad,caracteristica,dirigido):
        self.sexo=sexo
        self.edad=edad
        self.caracteristica=caracteristica
        self.dirigido=dirigido
#Objetos
dracula=Muñeco(sexo="Masculino",edad=400,caracteristica="Chupa Sangre",dirigido="adultos")   
barbie=Muñeco(sexo="Femenino",edad=17,caracteristica="Bailarina",dirigido="Niñas")

print(dracula.caracteristica)
print(f"{barbie.caracteristica} {barbie.dirigido}")
print(dracula.__dict__)