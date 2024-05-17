from Packages.Package_Input.Input import *
from os import system

def get_set():
    A = []
    while True:
        print(A)
        number = input("Ingrese un valor para el cojunto\n(aprete enter para omitir)\n")
        if not validate_number(number):
            break
        number = int(number)
        if number not in A:
            A.append(number)
        else:
            print(f"{number} ya se encuentra en el conjunto")
            system("pause")
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

def relationship_matrix(A: list, B:list, AxB: list, C: list) -> list:
    """Makes a matrix to check values from 2 sets

    Args:
        A (list): First set. It's used to build the matrix's rows
        B (list): Second set. It's used to build the matrix's colums
        AxB (list): Product between A and B
        C (list): Relationship between A and B

    Returns:
        list: A matrix with A values as rows and B values as colums. Matrix[i][j] has 0 or 1 value if the relationship is false or true.
    """
    D = [[0] * len(B) for _ in range(len(A))]
    row = 0
    column = 0
    j = 0

    loop = True
    while loop:
        for i in range(len(AxB)):
            if column == len(B):
                column = 0
                row += 1
            if AxB[i] == C[j]:
                D[row][column] = 1
                j += 1
            column +=1
            if j == len(C) or i == len(AxB):
                loop = False
                break
    return D

def show_array(array: list):
    """ Recieves an array and prints a formatted version of it.

    Args:
        array (list): The array you want to print.

    """
    message = "[ "
    for i in range(len(array)):
        for j in range(len(array[i])):
            message += f"{array[i][j]} "
        if i == len(array) - 1:
            message += "]"
        else:
            message += "\n  "
    return message