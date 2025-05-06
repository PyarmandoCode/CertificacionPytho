class Calculadora:
    def sumar(self,a,b):
        return a + b
    def restar(self,a,b):
        return a - b
    def multiplicar(self,a,b):
        return a * b
    def division(self,a,b):
        return a / b
    
calc =Calculadora()   
#diccionario que asociar cada operacion con el metodo correspondiente
operaciones = {
    "+":calc.sumar,
    "-":calc.restar,
    "*":calc.multiplicar,
    "/":calc.division
}

#Bucle interactivo
while True:
    try:
        entrada=input("Ingrese la Operacion o q para salir:")
        if entrada.lower()=="q":
            print("Gracias por usar la calculadora")
            break
        #separa los componentes
        partes= entrada.split()
        if len(partes)!=3: 
            print("Formato Incorrecto")
            continue
        a,op,b=partes
        a,b=float(a),float(b)
        #Ejecutar operaciones si es valida
        if op in operaciones:
            resultado=operaciones[op](a,b)
            print(f"El Resultado es {resultado}")
        else:
            print("Operacion Invalida")   
    except ValueError:
        print("Por Favor ingrese numeros validos")         
    except Exception as e:
        print(f"Error: {e}")    


