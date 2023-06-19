class Producto:
    def __init__(self, titulo):
        self.titulo = titulo

class Pelicula(Producto):
    def __init__(self, titulo, actor_principal, director, año):
        super().__init__(titulo)
        self.actor_principal = actor_principal
        self.director = director
        self.año = año
        self.costo_renta = 0
        self.costo_venta = 0

class Serie(Producto):
    def __init__(self, titulo, actor_principal, director, temporadas):
        super().__init__(titulo)
        self.actor_principal = actor_principal
        self.director = director
        self.temporadas = temporadas
        self.costo_renta = 0
        self.costo_venta = 0

class Documental(Producto):
    def __init__(self, titulo, director, tema, año):
        super().__init__(titulo)
        self.director = director
        self.tema = tema
        self.año = año
        self.costo_renta = 0
        self.costo_venta = 0

class EventoDeportivo(Producto):
    def __init__(self, titulo, deporte, fecha, hora, lugar):
        super().__init__(titulo)
        self.deporte = deporte
        self.fecha = fecha
        self.hora = hora
        self.lugar = lugar
        self.costo_renta = 0
        self.costo_venta = 0
