from tiendalibros.modelo.libro_error import LibroError

class LibroExistenteError(LibroError):
    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn
        mensaje = f"El libro con título '{titulo}' y ISBN '{isbn}' ya existe en el catálogo"
        super().__init__(mensaje)

    def __str__(self):
        return self.mensaje
