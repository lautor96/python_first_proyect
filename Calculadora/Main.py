def message_a_menu():
    print("BIENVENIDO A CALCULATOR\n")
    print("Aplicacion desarrollada para la resolucion de operaciones entre dos numeros, como: Suma, resta, multiplicacion y division")
    print("Para hacer uso de la calculadora, por favor escoja una opcion del siguiente MENU\n")
    print("MENU")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division\n")

def request_user_option():
    print("Ingrese una opcion del menu")
    return int(input())

def numbers_operation():
    print ("\nAhora por favor ingrese los numeros que quiere operar entre si\n")

def add_numbers(n_first, n_second):
    print ("\nAccedio a: SUMA\n")
    print("El resultado de la SUMA es " + str(n_first + n_second))

def sub_numbers(n_first, n_second):
    print ("\nAccedio a: RESTA\n")
    print("El resultado de la RESTA es " + str(n_first - n_second))

def product_numbers(n_first, n_second):
    print ("\nAccedio a: MULTIPLICAION\n")
    print("El resultado de la MULTIPLICACION es " + str(n_first * n_second))

def div_numbers(n_first, n_second):
    print ("\nAccedio a: DIVISION\n")
    print("El resultado de la DIVISION es " + str(n_first / n_second))

message_a_menu()
option = request_user_option()
numbers_operation()

number_1= float(input("Ingrese el primer numero"))
number_2= float(input("Ingrese el segundo numero"))

if (option == 1):
    add_numbers(number_1, number_2)
elif (option == 2):
    sub_numbers(number_1, number_2)
elif (option == 3):
    product_numbers(number_1, number_2)
elif (option == 4):
    print ("\nAccedio a: DIVISION")
    if (number_1 == 0):
        print("ERROR, el resultado es indefinido" )
    elif (number_2 == 0):
        print("ERROR, el resultado es indefinido" )
    else:
        div_numbers(number_1, number_2)
else:
    print ("\nERROR en la opcion del MENU\nFIN")



