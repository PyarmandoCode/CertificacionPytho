import platform

def obtener_info_sistema():
    info = {
     "Sistema Operativo" : platform.system(),
     "Version del Sistema":platform.version(),
     "Tipo de máquina": platform.machine(),
     "Procesador": platform.processor(),
     "Plataforma Completa" : platform.platform(),
     "Implementacion de python" :platform.python_implementation(),
     "Version de python" :".".join(platform.python_version_tuple())
    }
    return info

def mostrar_info(info):
    print("\n Informacion del sistema\n" + "="*40)
    for clave,valor in info.items():
        print(f"{clave:25}: {valor}")
    print("="*40)    

def guardar_info(info,archivo="reporte_sistema.txt"):
    with open(archivo,"w",encoding="utf-8") as f:
        f.write("📊 Informacion del Sistema\n") 
        f.write("="*40+"\n")
        for clave,valor in info.items():
            f.write(f"{clave:25}: {valor}\n")
        f.write("="*40+"\n")    
    print(f"\n Informacion guardada en :{archivo}")    

def menu():
    while True:
        print("\n Menú:")
        print("1.Mostrar Informacion del Sistema")
        print("2.Guardar la Informacion en el Archivo")
        print("3.Salir")
        opcion = input("Elige una opción (1/2/3):")
        if opcion=="1":
            info=obtener_info_sistema()
            mostrar_info(info)
        elif opcion =="2":
            info=obtener_info_sistema()
            guardar_info(info)    
        elif opcion=="3":
            print("Hasta Luego!")    
            break
        else:
            print("Opcioin Invalida Intente de Nuevo")

menu()            