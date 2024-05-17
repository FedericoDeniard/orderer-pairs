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

    while True:
        equation = input("Escriba la ecuación (la multiplicación es *): \n")
        safe_dict = {}
        x = 1
        y = 1
        safe_dict['x'] = x
        safe_dict['y'] = y
        try:
            eval(equation)
            break
        except SyntaxError:
            print("Error: La ecuación es invalida. Por favor, intentelo nuevamente.")

    for a in A:
        for b in B:
            x = int(a)
            y = int(b)
            safe_dict['x'] = x
            safe_dict['y'] = y
            if eval(equation, {"__builtins__": None}, safe_dict):
                C.append([a, b])

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

def get_domain(C: list) -> set:
    domain = {pair[0] for pair in C}
    return domain

def get_range(C: list) -> set:
    range = {pair[1] for pair in C}
    return range