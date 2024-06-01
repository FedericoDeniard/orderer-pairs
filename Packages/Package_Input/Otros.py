import os
from os import system

def clear_screen():
    if os.name == "nt":
        system("cls")
    else:
        system("clear")

def pause(message = "Presione una tecla para continuar...\n"):
    if os.name == "nt":
        system("pause")
    else:
        input(message)