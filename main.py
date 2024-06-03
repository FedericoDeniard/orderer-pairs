from Packages.Package_Pairs.Pairs import *
from os import system
from os import name

def main():
    print("Conjunto A:")
    A = get_set()
    print("Conjunto B:")
    B = get_set()
    run = True

    while run:
        system("clear")
        print(f"A={A}\nB={B}")
        option = get_int(message="Seleccione una opcion\n1. AxB\n2. BxA\n3. AxA\n4. BxB\n5. Cambiar valores\n6. Salir\n",min=1,max=6)
        match option:
            case 1:
                result = multiply_sets(A, B)
                print(f"AxB: {result}")
                relation = relationship(A, B)
                system("clear")
                print(f"AxB: {result}")
                print(f"R: {relation}")
                matrix = relationship_matrix(A, B, result, relation)
                formatted_matrix = show_array(matrix)
                print(f"Mr: \n{formatted_matrix}")
                domain = get_domain(result)
                set_range = get_range(result)
                print(f"El dominio es: {domain}")
                print(f"La imagen es: {set_range}")
                properties = relation_properties(A, B,relation)
                print(properties)
            case 2:
                result = multiply_sets(B, A)
                print(f"BxA: {result}")
                relation = relationship(B, A)
                system("clear")
                print(f"BxA: {result}")
                print(f"R: {relation}")
                matrix = relationship_matrix(B, A, result, relation)
                formatted_matrix = show_array(matrix)
                print(f"Mr: \n{formatted_matrix}")
                domain = get_domain(result)
                set_range = get_range(result)
                print(f"El dominio es: {domain}")
                print(f"La imagen es: {set_range}")
                properties = relation_properties(B, A,relation)
                print(properties)
            case 3:
                result = multiply_sets(A, A)
                print(f"AxA: {result}")
                relation = relationship(A, A)
                system("clear")
                print(f"AxA: {result}")
                print(f"R: {relation}")
                matrix = relationship_matrix(A, A, result, relation)
                formatted_matrix = show_array(matrix)
                print(f"Mr: \n{formatted_matrix}")
                domain = get_domain(result)
                set_range = get_range(result)
                print(f"El dominio es: {domain}")
                print(f"La imagen es: {set_range}")
                properties = relation_properties(A, B,relation)
                print(properties)
            case 4:
                result = multiply_sets(B, B)
                print(f"BxB: {result}")
                relation = relationship(B, B)
                system("clear")
                print(f"BxB: {result}")
                print(f"R: {relation}")
                matrix = relationship_matrix(B, B, result, relation)
                formatted_matrix = show_array(matrix)
                print(f"Mr: \n{formatted_matrix}")
                domain = get_domain(result)
                set_range = get_range(result)
                print(f"El dominio es: {domain}")
                print(f"La imagen es: {set_range}")
                properties = relation_properties(B,A,relation)
                print(properties)
            case 5:
                print("Conjunto A:")
                A = get_set()
                print("Conjunto B:")
                B = get_set()

            case 6:
                run = False
        input("Presione una tecla para continuar...")
main()

if __name__ == '__main__':
    main()