from libro import Libro
from carro_compra import CarroCompras
from excepciones import LibroAgotadoError, ExistenciasInsuficientesError, LibroExistenteError

class TiendaLibros:
    def __init__(self):
        self.catalogo = {}
        self.carrito = CarroCompras()

    def adicionar_libro_a_catálogo(self, isbn, titulo, precio, existencias):
        if isbn in self.catalogo:
            raise LibroExistenteError(titulo, isbn)
        else:
            libro = Libro(titulo, "", precio)
            libro.isbn = isbn
            libro.existencias = existencias
            self.catalogo[isbn] = libro
            return libro

    def agregar_libro_a_carrito(self, libro, cantidad):
        if libro.isbn not in self.catalogo:
            raise ValueError("El libro no está en el catálogo.")

        existencias = self.catalogo[libro.isbn].existencias

        if existencias == 0:
            raise LibroAgotadoError(libro.titulo, libro.isbn)

        if cantidad > existencias:
            raise ExistenciasInsuficientesError(libro.titulo, libro.isbn, cantidad, existencias)

        self.carrito.agregar_item(libro, cantidad)
    def retirar_item_de_carrito(self, isbn):
        self.carrito.quitar_item(isbn)
