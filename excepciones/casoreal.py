def leer_nombre():
    try:
        with open("nombres.txt","r") as archivo:
            lineas= archivo.readlines()
            if not lineas:
                raise ValueError("El Archivo esta Vacio")
            
            for nombre in lineas:
                nombre=nombre.strip()
                if not nombre.isalpha(): #Valida que sea letras
                    raise ValueError(f"Datos no valido {nombre}")
                print(nombre.upper())
    except FileNotFoundError:
        print("El Archivo no existe")           
    except ValueError as e:
        print(f"Error de contenido {e}")     
    except Exception as e:
        print(f"Error inesperado {e}")    
    else:
        print("Lectura completada correctamente")    


leer_nombre()        