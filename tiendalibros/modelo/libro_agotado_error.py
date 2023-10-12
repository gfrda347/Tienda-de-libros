from tiendalibros.modelo.libro_error import LibroError

class LibroAgotadoError(LibroError):
    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn
        mensaje = f"El libro con título '{titulo}' e ISBN '{isbn}' está agotado."
        super().__init__(mensaje)

    def __str__(self):
        return self.mensaje
