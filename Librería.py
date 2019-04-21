class Libreria:

    def __init__(self):
        self.libros = {}

    def crear(self, Titulo, libro):
        if Titulo not in self.libros:
            self.libros.update({Titulo: libro})
            print("¡Se ha añadido un nuevo libro!")
            print("El libro añadido es:", Titulo, "del autor:", libro.autor)

    def modificar(self, Titulo, libro):
        for dict_key, dict_value in self.libros.items():
            if dict_key is Titulo:
                if libro.especialidad is not dict_value.especialidad:
                    print("La especialidad del libro no puede cambiar, se conservará la existente.")
                    libro.especialidad = dict_value.especialidad
                self.libros.update({dict_key: libro})
                print("El libro", Titulo, "se modifico de la siguiente manera:")
                print("Titulo:", Titulo, ", autor:", libro.autor, ", especialidad:", libro.especialidad, ", N° ventas:",
                      libro.ventas, ", nota de la crítica:", libro.nota, ", comentarios:", libro.comentarios)

        self.crear(Titulo, libro)

    def compra_segura(self, autor):
        may = 0
        libroslist = []
        for dict_key, dict_value in self.libros.items():
            if dict_value.autor is autor:
                if dict_value.nota > may:
                    may = dict_value.nota

        for dict_key, dict_value in self.libros.items():
            if dict_value.autor is autor and dict_value.nota is may:
                libroslist.append(dict_key)

        if len(libroslist) > 1:
            print("Los libros con la mayor nota de crítica del autor", autor, " son:")
        else:
            print("El libro con la mayor nota de crítica del autor", autor, " es:")

        for key in libroslist:
            print("Libro:", key, ", especialidad:", self.libros[key].especialidad, ", N° ventas:",
                  self.libros[key].ventas, ", nota de la crítica:", self.libros[key].nota, ", comentarios:",
                  self.libros[key].comentarios)

    def listado(self, especialidad):
        listado = []
        for dict_key, dict_value in self.libros.items():
            if dict_value.especialidad is especialidad:
                listado.append(dict_key)

        for j in range(2, len(listado) - 1, 2):
            for i in range(len(listado) - 1):
                if self.libros[listado[i]].ventas < self.libros[listado[i+1]].ventas:
                    act = listado[i]
                    listado[i] = listado[i+1]
                    listado[i+1] = act

        print("Los libros de la especialidad", especialidad, " en orden de ventas son:")
        for key in listado:
            print("Libro:", key, ", autor:", self.libros[key].autor, ", N° ventas:", self.libros[key].ventas,
                  ", nota de la crítica:", self.libros[key].nota, ", comentarios:",
                  self.libros[key].comentarios)

    def mostrar(self):
        print("Los libros agregados son: ")
        for dict_key, dict_value in self.libros.items():
            print("Titulo:", dict_key, ", autor:", dict_value.autor, ", especialidad:", dict_value.especialidad,
                  ", N° ventas:", dict_value.ventas, ", nota de la crítica:", dict_value.nota, ", comentarios:",
                  dict_value.comentarios)
