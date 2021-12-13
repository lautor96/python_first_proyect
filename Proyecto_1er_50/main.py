#Aplicacion login - ELECTIVA EN PROGRAMACION
#Laura Alejandra Torres Ochoa
#Codigo:201421760

import verific

user = "laura@gmail.com"
password = "Program55?"

def message_a_menu():
    print("BIENVENIDO A CALCULATOR\n")
    print("Por favor")

message_a_menu()

user_1= raw_input("Ingrese su correo: ")#obtener la entrada del usuario como una string
password_1= raw_input("Ingrese su clave: ")

if (user_1 == user) & (password_1 == password):
    verific.compare_users(user_1, user)
    verific.compare_password(password_1, password)
    print ("LOGIN EXITOSO")
elif (user_1 != user) | (password_1 != password):
    verific.ver_mail(user_1)
    verific.compare_users(user_1, user)
    verific.compare_password(password_1, password)
    print ("ERROR LOGIN")
else:
    print ("...")
