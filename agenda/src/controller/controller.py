import json
from ..models.person import Person
from ..view.view import View

class Controller:
    def __init__(self):
        self.valor_seleccionado = 0
        self.vista = View()
        self.contactos = []

    def acciones(self):
        while self.valor_seleccionado != 5:
            self.valor_seleccionado = self.vista.seleccionar_opcion_menu()
            if self.valor_seleccionado == 1:
                self.agregar_contacto()
            if self.valor_seleccionado == 2:
                self.listar_contacto()
            if self.valor_seleccionado == 3:
                self.buscar_contacto()
            if self.valor_seleccionado == 4:
                self.agregar_numero()


    def agregar_contacto(self):
        contacto = self.vista.formulario_contacto()
        self.contactos.append(contacto)
        self.vista.contacto_creado_correctamente(contacto.nombre)

    def listar_contacto(self):
        for contacto in self.contactos:
            print(contacto.exportar())

    def agregar_numero(self):
        nombre_del_archivo = self.vista.nombre_del_archivo()
        lista_para_exportar = []
        for contacto in self.contactos:
            lista_para_exportar.append(contacto.exportar())

        with open(f"data/{nombre_del_archivo}.json", "w") as fp:
            json.dump(lista_para_exportar, fp)

        self.vista.mensaje_correcto()

    def buscar_contacto(self):
        nombre_del_archivo = self.vista.nombre_del_archivo()
        lista_para_exportar = []
        for contacto in self.contactos:
            lista_para_exportar.append(contacto.exportar())

        with open(f"data/{nombre_del_archivo}.json", "r") as fp:
            json.dump(lista_para_exportar, fp)

        self.vista.mensaje_correcto()

    def salir(self):
        pass
