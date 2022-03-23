from ..models.person import Person


class View:
    def seleccionar_opcion_menu(self):
        print("1. Agregar contacto")
        print("2. Listar contacto")
        print("3. Buscar contacto")
        print("4. Adicionar telefono a contacto")
        print("5. Salir")
        return int(input("Ingrese la opcion    "))

    def formulario_contacto(self):
        nombre = int(input("Ingrese nombre "))
        apellido = str(input("Ingrese apellido"))
        apodo = int(input("Ingrese apodo"))
        telefono = int(input("Ingrese telefono "))
        correo = int(input("Ingrese correo"))
        return Person(nombre, apellido, apodo, telefono, correo)

    def contacto_creado_correctamente(self, name):
        print("Contacto #{name}, creado correctamente")

    def nombre_del_archivo(self):
        return str(input("Ingrese nombre del archivo"))

    def mensaje_correcto(self):
        print("---")
        print("Accion realizada correctamente :D")
        print("---")

    def mensaje_incorrecto(self, message):
        print("---")
        print("La accion no se pudo realizar D:")
        print(message)
        print("---")
