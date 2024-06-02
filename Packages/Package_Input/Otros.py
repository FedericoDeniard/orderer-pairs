import platform
from os import system

def clear_screen():
    os_name = platform.system()
    if os_name == "Windows":
        clear_screen()
    else:
        system("clear")

def pause(message = "Presione una tecla para continuar...\n"):
    if platform.system == "nt":
        system("pause")
    else:
        input(message)