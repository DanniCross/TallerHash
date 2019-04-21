from Compania import Compania
from Libro import Libro
from Librería import Libreria


def main():
    # 1
    compania = Compania()
    compania.Ingresar(123, "Felipe", 2928)
    compania.Ingresar(345, "Jose", 2625)
    compania.Ingresar(567, "Gomez", 2324)
    compania.Buscar("Felipe")
    compania.Buscar(2625)
    compania.Buscar(567)
    # 2
    libreria = Libreria()
    libro = Libro("Paula Hawkins", 50, 5, "Novela", "comentario1")
    libreria.crear("Libro escrito en el agua", libro)
    libro = Libro("Alejandro Sequera", 20, 3, "Reflexión", "comentario2")
    libreria.crear("Mi viaje sin ti", libro)
    libro = Libro("Antoine de Saint", 100, 10, "Infantil", "comentario3")
    libreria.crear("El principito", libro)
    libro = Libro("Antoine de Saint", 70, 10, "Infantil", "comentario4")
    libreria.crear("Tierra de hombres", libro)
    libro = Libro("Antoine de Saint", 30, 5, "Infantil", "comentario5")
    libreria.crear("Vuelo nocturno", libro)
    print()
    libro = Libro("Alejandro Sequera", 50, 10, "Este no cambia", "Este si cambia")
    libreria.modificar("Mi viaje sin ti", libro)
    libro = Libro("Yo", 100, 50, "Alguno", "si")
    libreria.modificar("Mi título", libro)
    print("Los libros agregados junto con el modificado son:")
    libreria.mostrar()
    print()
    libreria.compra_segura("Antoine de Saint")
    print()
    libreria.listado("Infantil")


main()
