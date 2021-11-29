print ("BIENVENIDO A CALCULATOR\nAplicacion desarrollada para la resolucion de "
       "operaciones entre dos numeros, como: Suma, resta, multiplicacion y division.\n"
       "Para hacer uso de la calculadora, por favor escoja una opcion del siguiente MENU")


opcion=int(input("MENU\n "
                 "1. Suma [1]\n"
                 "2. Resta [2]\n"
                 "3. Multiplicacion [3]\n"
                 "4. Division [4]\n"))

print ("\nAhora por favor ingrese los numeros que quiere operar entre si\n")
numero_1= float(input("Ingrese el primer numero"))
numero_2= float(input("Ingrese el segundo numero"))

if (opcion == 1):
    print ("\nAccedio a: SUMA")
    suma=float(numero_1+numero_2)
    print ("El resultado de la SUMA, es:% .2f"% suma)
elif (opcion == 2):
    print ("\nAccedio a: RESTA")
    resta = float(numero_1 - numero_2)
    print ("El resultado de la RESTA, es:% .2f" % resta)
elif (opcion == 3):
    print ("\nAccedio a: MULTIPLICACION")
    multiplicacion = float(numero_1 * numero_2)
    print ("El resultado de la MULTIPLICACION, es:% .2f" % multiplicacion)
elif (opcion == 4):
    print ("\nAccedio a: DIVISION")
    division = float(numero_1 / numero_2)
    print ("El resultado de la DIVISION, es:% .2f" % division)
else:
    print ("\nERROR en la opcion del MENU\nFIN")



