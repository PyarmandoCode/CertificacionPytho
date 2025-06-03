#Sistema Bancario
class CuentaBancaria:
    def __init__(self,titular,saldo_inicial=0):
        self.titular=titular
        self.__saldo=saldo_inicial #Atributo Privado

    def __str__(self):
        return f"{self.titular} y su saldo actual {self.__saldo}"
    
    def depositar(self,cantidad):
        if cantidad>0:
            self.__saldo +=cantidad #acumulador
            print(f"{self.titular}: Deposito de {cantidad}. Nuevo saldo:{self.__saldo}")
        else:
            print("Cantidad Invalida para depositar")      

    def retirar(self,cantidad):
        if cantidad<=0:
            print("Cantidad invalida para retirar")          
        elif cantidad>self.__saldo:
            print("Fondos Insuficientes")    
        else:
            self.__saldo -=cantidad
            print(f"{self.titular}: Retiro la {cantidad}. Nuevo Saldo: {self.__saldo}")    
    #interacciion entre objetos        
    #opera sobre otra instancoa de la misma clase
    def transferir(self,destino,cantidad):
        if not isinstance(destino,CuentaBancaria):
            print("Destino es Invalido")        
            return
        if cantidad>self.__saldo:
            print("Fondos insuficientes para transferir")
        else:
            self.__saldo-=cantidad
            destino.__saldo +=cantidad
            print(f"Transferidos {cantidad} de {self.titular}  a {destino.titular}")    
    def mostrar_saldo(self):
        return(f"{self.titular} tiene un saldo de {self.__saldo}")         
        


#Crear Cuentas
cuenta_ana=CuentaBancaria("Ana",1000)    
cuenta_luis=CuentaBancaria("Luis",500)
cuenta_ana.depositar(200)
cuenta_luis.depositar(300)
cuenta_ana.transferir(cuenta_luis,400)
print(cuenta_luis.mostrar_saldo())
#cuenta_ana.depositar(800)
#cuenta_ana.retirar(400)

#print(cuenta_ana.__dict__)
#print(cuenta_luis.__dict__)
#print(cuenta_ana)
#print(cuenta_luis)