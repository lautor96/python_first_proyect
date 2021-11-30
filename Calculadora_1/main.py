
print("BIENVENIDO A CALCULATOR\n")
print("Aplicacion desarrollada para la resolucion de operaciones entre dos numeros, como: Suma, resta, multiplicacion y division")
print("Para hacer uso de la calculadora, por favor escoja una opcion del siguiente MENU\n")
print("Ingrese una opcion del menu")
option=int(input("MENU\n 1. Suma [1]\n 2. Resta [2]\n 3. Multiplicacion [3]\n 4. Division [4]\n"))


print ("\nAhora por favor ingrese los numeros que quiere operar entre si\n")
number_1= float(input("Ingrese el primer numero"))
number_2= float(input("Ingrese el segundo numero"))

if (option == 1):
    print ("\nAccedio a: SUMA\n")
    suma = number_1 + number_2
    print("El resultado de la SUMA es:% .2f"%  suma)
elif (option == 2):
    print ("\nAccedio a: RESTA\n")
    resta = number_1 - number_2
    print("El resultado de la RESTA es: % .2f"%  resta)
elif (option == 3):
    print ("\nAccedio a: MULTIPLICAION\n")
    multiplicacion = number_1 * number_2
    print("El resultado de la RESTA es:% .2f"% multiplicacion)
elif (option == 4):
    print ("\nAccedio a: DIVISION")
    if (number_1 == 0):
        print("ERROR, el resultado es indefinido" )
    elif (number_2 == 0):
        print("ERROR, el resultado es indefinido" )
    else:
        division = number_1 / number_2
        print("El resultado de la DIVISION es:% .2f" % division)
else:
    print ("\nERROR en la opcion del MENU\nFIN")