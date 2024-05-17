from Packages.Package_Pairs.Pairs import *
from os import system

def main():
    print("Conjunto A:")
    A = get_set()
    print("Conjunto B:")
    B = get_set()
    run = True

    while run:
        system("cls")
        print(f"A={A}\nB={B}")
        option = get_int(message="Seleccione una opcion\n1. AxB\n2. BxA\n3. AxA\n4. BxB\n5. Cambiar valores\n6. Salir\n",min=1,max=6)
        match option:
            case 1:
                result = multiply_sets(A, B)
                print(f"AxB: {result}")
                relation = relationship(A, B)
                system("cls")
                print(f"AxB: {result}")
                print(f"R: {relation}")
                matrix = relationship_matrix(A, B, result, relation)
                formatted_matrix = show_array(matrix)
                print(f"Mr: \n{formatted_matrix}")

            case 2:
                result = multiply_sets(B, A)
                print(f"BxA: {result}")
                relation = relationship(B, A)
                system("cls")
                print(f"BxA: {result}")
                print(f"R: {relation}")
                matrix = relationship_matrix(B, A, result, relation)
                formatted_matrix = show_array(matrix)
                print(f"Mr: \n{formatted_matrix}")

            case 3:
                result = multiply_sets(A, A)
                print(f"AxA: {result}")
                relation = relationship(A, A)
                system("cls")
                print(f"AxA: {result}")
                print(f"R: {relation}")
                matrix = relationship_matrix(A, A, result, relation)
                formatted_matrix = show_array(matrix)
                print(f"Mr: \n{formatted_matrix}")

            case 4:
                result = multiply_sets(B, B)
                print(f"BxB: {result}")
                relation = relationship(B, B)
                system("cls")
                print(f"BxB: {result}")
                print(f"R: {relation}")
                matrix = relationship_matrix(B, B, result, relation)
                formatted_matrix = show_array(matrix)
                print(f"Mr: \n{formatted_matrix}")

            case 5:
                print("Conjunto A:")
                A = get_set()
                print("Conjunto B:")
                B = get_set()

            case 6:
                run = False
        system("pause")
main()