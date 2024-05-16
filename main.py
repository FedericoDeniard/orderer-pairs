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
                result = multiply_sets(A,B)
                print(result)
                relation = relationship(A,B)
                print(relation)
            case 2:
                result = multiply_sets(B,A)
                print(result)
                relation = relationship(B,A)
                print(relation)
                
            case 3:
                result = multiply_sets(A,A)
                print(result)
                relation = relationship(A,A)
                print(relation)
            case 4:
                result = multiply_sets(B,B)
                print(result)
                relation = relationship(B,B)
                print(relation)
            case 5:
                print("Conjunto A:")
                A = get_set()
                print("Conjunto B:")
                B = get_set()
            case 6:
                run = False
        system("pause")
main()
