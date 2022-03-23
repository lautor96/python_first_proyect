class Person:
    nombre = ''
    apellido = ''
    apodo = ''
    telefono = 0
    correo = ''

    def __init__(self, nombre, apellido, apodo, telefono, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.apodo = apodo
        self.telefono = telefono
        self.correo = correo

    def dar_nombre(self):
        return self.nombre

    def dar_apellido(self):
        return self.apellido

    def dar_apodo(self):
        return self.apodo

    def dar_telefono(self):
        return self.telefono

    def dar_correo(self):
        return self.correo

    def agregar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def agregar_apellido(self, nuevo_apellido):
        return self.nuevo_apellido

    def agregar_apodo(self, nuevo_apodo):
        return self.nuevo_apodo

    def agregar_telefono(self, nuevo_telefono):
        return self.nuevo_telefono

    def agregar_correo(self, nuevo_correo):
        return self.nuevo_correo

    def exportar(self):
        return {"nombre": self.nombre, "apellido": self.apellido, "apodo": self.apodo, "telefono": self.telefono,"correo": self.correo}