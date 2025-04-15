import platform

def mostrar_info_sistema():
    print("="*40)
    print("📊 Informacion del sistema detectado")
    print("="*40)
    print(f"🖥️ Sistema Operativo : {platform.system()}")
    print(f"🧬 Version del Sistema : {platform.version()}")
    print(f"🖥️ Tipo de máquina : {platform.machine()}")
    print(f"🧠 Procesador : {platform.processor()}")
    print(f"🧾 Plataforma Completa : {platform.platform()}")
    print(f"🐍 Implementacion de python : {platform.python_implementation()}")
    print(f"🔢 Version de python : {'.'.join(platform.python_version_tuple())}")
    print("="*40)


mostrar_info_sistema()

    