from Empleado import Empleado


class Compania:

    def __init__(self):
        self.empleados = {}

    def Ingresar(self, num, nombre, numSS):
        empleado = Empleado(nombre, numSS)
        if num not in self.empleados:
            self.empleados.update({num: empleado})

    def Buscar(self, dato):
        for dict_key, dict_value in self.empleados.items():
            if dato is dict_key or dato is dict_value.nombre or dato is dict_value.numSS:
                print("Empleado:", dict_key, ", nombre:", dict_value.nombre, ", número de seguro social:"
                      , dict_value.numSS)
