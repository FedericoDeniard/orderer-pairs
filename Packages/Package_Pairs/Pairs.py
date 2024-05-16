from Packages.Package_Input.Input import *
from os import system

def get_set():
    A = []
    while True:
        print(A)
        number = input("Ingrese un valor para el cojunto\n(aprete enter para omitir)\n")
        if not validate_number(number):
            break
        A.append(number)
        system("cls")
    
    return A

def multiply_sets(A: list,B: list) -> list:
    C = []
    for a in A:
        for b in B:
            result = [a,b]
            C.append(result)
    return C

def relationship(A: list,B: list) -> list:
    C = []

    print("Escribe el operador relacional")
    relational_operator = input("x '> / < / >= / <= / = / !=' y\n")
    while relational_operator not in [">","<",">=","<=","=","!="]:
        relational_operator = input("x '> / < / >= / <= / = / !=' y\n")

    print("Agregar un operador a Y\n(aprete enter para omitir)")
    operador_y = input("'+ / - / * / % / ^'\n")
    while operador_y not in ["","+","-","*","%","^"] :
        operador_y = input("'+ / - / * / % / ^'\n")
    if operador_y != "":
        modificador_y = get_int(f"Agregue un valor para z:\n 'x {relational_operator} y{operador_y}z'\n")

    for a in A:
        a = int(a)
        for b in B:
            b = int(b)
            match relational_operator:
                case ">":
                    match operador_y:
                        case "+":
                            system("pause")
                            if a > (b+modificador_y):
                                C.append([a,b])
                        case "-":
                            if a > (b-modificador_y):
                                C.append([a,b])
                        case "*":
                            if a > (b*modificador_y):
                                C.append([a,b])
                        case "%":
                            if a > (b/modificador_y):
                                C.append([a,b])
                        case "^":
                            if a > (b**modificador_y):
                                C.append([a,b])
                        case _:
                            if a > b:
                                C.append([a,b])
                case "<":
                    match operador_y:
                        case "+":
                            if a < (b+modificador_y):
                                C.append([a,b])
                        case "-":
                            if a < (b-modificador_y):
                                C.append([a,b])
                        case "*":
                            if a < (b*modificador_y):
                                C.append([a,b])
                        case "%":
                            if a < (b/modificador_y):
                                C.append([a,b])
                        case "^":
                            if a < (b**modificador_y):
                                C.append([a,b])
                        case _:
                            if a < b:
                                C.append([a,b])
                case ">=":
                    match operador_y:
                        case "+":
                            if a >= (b+modificador_y):
                                C.append([a,b])
                        case "-":
                            if a >= (b-modificador_y):
                                C.append([a,b])
                        case "*":
                            if a >= (b*modificador_y):
                                C.append([a,b])
                        case "%":
                            if a >= (b/modificador_y):
                                C.append([a,b])
                        case "^":
                            if a >= (b**modificador_y):
                                C.append([a,b])
                        case _:
                            if a >= b:
                                C.append([a,b])
                case "<=":
                    match operador_y:
                        case "+":
                            if a <= (b+modificador_y):
                                C.append([a,b])
                        case "-":
                            if a <= (b-modificador_y):
                                C.append([a,b])
                        case "*":
                            if a <= (b*modificador_y):
                                C.append([a,b])
                        case "%":
                            if a <= (b/modificador_y):
                                C.append([a,b])
                        case "^":
                            if a <= (b**modificador_y):
                                C.append([a,b])
                        case _:
                            if a <= b:
                                C.append([a,b])
                case "=":
                    match operador_y:
                        case "+":
                            if a == (b+modificador_y):
                                C.append([a,b])
                        case "-":
                            if a == (b-modificador_y):
                                C.append([a,b])
                        case "*":
                            if a == (b*modificador_y):
                                C.append([a,b])
                        case "%":
                            if a == (b/modificador_y):
                                C.append([a,b])
                        case "^":
                            if a == (b**modificador_y):
                                C.append([a,b])
                        case _:
                            if a == b:
                                C.append([a,b])
                case "!=":
                    match operador_y:
                        case "+":
                            if a != (b+modificador_y):
                                C.append([a,b])
                        case "-":
                            if a != (b-modificador_y):
                                C.append([a,b])
                        case "*":
                            if a != (b*modificador_y):
                                C.append([a,b])
                        case "%":
                            if a != (b/modificador_y):
                                C.append([a,b])
                        case "^":
                            if a != (b**modificador_y):
                                C.append([a,b])
                        case _:
                            if a != b:
                                C.append([a,b])
    return C