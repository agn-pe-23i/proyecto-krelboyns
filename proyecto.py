}- proyecto
  |- main.py
  |- catalog.py
  |- menu.py
# main.py
from menu import show_main_menu

def main():
    show_main_menu()

if _name_ == '_main_':
    main()
# catalogo.py
class Producto:
    def _init_(self, titulo):
        self.titulo = titulo

class Pelicula(Producto):
    def _init_(self, titulo, actor, director, año, costo_alquiler, costo_venta):
        super()._init_(titulo)
        self.actor = actor
        self.director = director
        self.año = año
        self.costo_alquiler = costo_alquiler
        self.costo_venta = costo_venta

    # Agrega otros métodos necesarios para las películas

class Serie(Producto):
    def _init_(self, titulo, actor, director, temporadas, costo_alquiler, costo_venta):
        super()._init_(titulo)
        self.actor = actor
        self.director = director
        self.temporadas = temporadas
        self.costo_alquiler = costo_alquiler
        self.costo_venta = costo_venta

    # Agrega otros métodos necesarios para las series

class Documental(Producto):
    def _init_(self, titulo, director, tema, año, costo_alquiler, costo_venta):
        super()._init_(titulo)
        self.director = director
        self.tema = tema
        self.año = año
        self.costo_alquiler = costo_alquiler
        self.costo_venta = costo_venta

    # Agrega otros métodos necesarios para los documentales

class EventoDeportivoEnVivo(Producto):
    def _init_(self, titulo, deporte, fecha, hora, lugar, costo_venta):
        super()._init_(titulo)
        self.deporte = deporte
        self.fecha = fecha
        self.hora = hora
        self.lugar = lugar
        self.costo_venta = costo_venta

    # Agrega otros métodos necesarios para los eventos deportivos en vivo

# Agrega otros métodos o clases necesarios para el manejo del catálogo
# menu.py
from catalogo import Pelicula, Serie, Documental, EventoDeportivoEnVivo

def mostrar_menu_principal():
    while True:
        print("Menú principal")
        print("1. Agregar un producto")
        print("2. Buscar producto")
        print("3. Eliminar un producto")
        print("4. Mostrar el catálogo")
        print("5. Cargar catálogo")
