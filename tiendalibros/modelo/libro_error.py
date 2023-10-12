from tiendalibros.modelo.libro import Libro
from tiendalibros.modelo.libro_error import LibroError

class LibroError(Exception):
    pass

class LibroExistenteError(LibroError):
    def __init__(self, titulo, isbn):
        super().__init__()
        self.titulo = titulo
        self.isbn = isbn

    def __str__(self):
        return f"El libro con título '{self.titulo}' y ISBN: {self.isbn} ya existe en el catálogo."

try:
    raise LibroExistenteError("Título del Libro", "ISBN12345")
except LibroExistenteError as e:
    print(e)  

class LibroError(Exception):
    pass

class ExistenciasInsuficientesError(LibroError):
    def __init__(self, mensaje, cantidad_a_comprar):
        super().__init__(mensaje)
        self.cantidad_a_comprar = cantidad_a_comprar

try:
    raise ExistenciasInsuficientesError("No hay suficientes existencias para la compra", 5)
except ExistenciasInsuficientesError as e:
    print(f"Error: {e}, Cantidad a comprar: {e.cantidad_a_comprar}")

