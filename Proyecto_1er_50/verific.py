def compare_users(n_users, m_users):
    if len(n_users) is 0:
        print ("\nUsuario no debe estar vacio\n")
    elif n_users != m_users:
        print("\nUsuario incorrecto\n")
    elif n_users == m_users:
        print("\nUsuario correcto\n")
    else:
        print ("...")
def ver_mail(r_user):
    if r_user.count('@') == 0:
        print ("No es un email")
    elif r_user.count('@') <=1:
        print("OK")
def compare_password(n_password, m_password):
    if len(n_password) is 0:
        print ("Clave no debe estar vacio\n")
    elif len(n_password) < 8:
        print ("Clave debe tener minimo 8 caracteres\n")
    elif n_password != m_password:
        print("Clave incorrecta\n")
    elif n_password == m_password:
        print("Clave correcta\n")
    else:
        print ("...")