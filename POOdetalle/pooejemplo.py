class EquipoEspañol:
    def __init__(self,nombre,ciudad,fundacion):
        self.nombre=nombre
        self.ciudad=ciudad
        self.fundacion=fundacion
        self.titulos = [] #Lista para guardar titulos ganados

    #Metodo paramostrar informacion del equipo
    def mostar_info(self):
        print(f"Equipo: {self.nombre}")    
        print(f"Ciudad: {self.ciudad}")    
        print(f"Año de Fundacion: {self.fundacion}")    
        print(f"Titulos: {', '.join(self.titulos) if self.titulos else 'Ninguno'}") 
        print("-"*40)   

    def agregar_titulo(self,titulo):
        self.titulos.append(titulo)    
        print(f"🏆{titulo} agregado a {self.nombre}")
    def total_titulos(self):
        return len(self.titulos)    


#Crear objetos (equipos)
barcelona= EquipoEspañol("FC BARCELONA","BARCELONA",1899)        
madrid= EquipoEspañol("REAL MADRID","MADRID",1902)  
barcelona.agregar_titulo("La Liga 2023")      
madrid.agregar_titulo("Champions League 2023")
barcelona.agregar_titulo("Copa del Rey 2022")

#usar metodos
barcelona.mostar_info()
madrid.mostar_info()

#total de titulos
print(f"{barcelona.nombre} tiene {barcelona.total_titulos()} titulos")
print(f"{madrid.nombre} tiene {madrid.total_titulos()} titulos")