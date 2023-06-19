[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/LCXMIOgt)
# Proyecto
PROFESOR:Abel García Nájera

ALUMNOS:

RAMÍREZ AGUILERA JESÚS EMMANUEL 2223068873
RODRÍGUEZ BECERRIL ANTONIO 2213026390

UEA: PROGRAMACIÓN ESTRUCTURADA CB01C
CARRERA: INGENIERÍA EN COMPUTACIÓN

OBJETIVO: Aplicar todos los conocimientos adquiridos durante la UEA.
**************************************************************************
 
Introducción:
El objetivo principal de esta actualización es proporcionar a los usuarios una plataforma actualizada y fácil de usar, donde puedan acceder a una amplia variedad de películas, series, documentales y eventos deportivos en vivo. El nuevo sistema deberá permitir a los usuarios explorar el catálogo, obtener información detallada de cada producto, alquilar o comprar, y disfrutar de una experiencia de lectura detallada. Para esto se establecen los requisitos clave y se propone la creación de un nuevo modelo de alquiler y ventas. Se ha implementado un algoritmo en Python que resuelve de manera correcta las tareas asignadas, lo que permite una gestión eficiente del inventario. Además, se explorarán diferentes métodos y mejores prácticas para mejorar la capacidad de respuesta y la facilidad de uso de la plataforma.

Comentarios de la Implementación:
El código muestra una implementación de clases en Python para un catálogo de productos que puede agregar, buscar, eliminar y mostrar diferentes tipos de productos. Los productos son de cuatro tipos: Película, Serie, Documental y EventoDeportivo. Cada tipo de producto tiene diferentes atributos, los cuales son inicializados en el constructor.

La clase Catalogo es la clase principal que administra todos los productos. Contiene los métodos para agregar, buscar, eliminar y mostrar productos, además de cargar y guardar el catálogo en un archivo. También contiene los métodos que muestran diferentes tipos de productos y todo el catálogo.

Los métodos de mostrar catálogo, buscar y eliminar reciben un argumento adicional que indica el tipo de producto a mostrar, buscar o eliminar. Los métodos de mostrar productos eliminan la necesidad de repetir código.

La función principal es un bucle infinito que muestra el menú principal al usuario y llama a los métodos correspondientes para cada elección del usuario. La función main() se ejecuta al final del archivo para iniciar el programa.

La clase "Producto" define un objeto con una propiedad "título".
Las clases "Película", "Serie", "Documental" y "EventoDeportivo" heredan de "Producto" y definen objetos con propiedades relevantes para cada tipo de producto.
La clase "Catalogo" define un objeto que puede agregar, buscar, eliminar y mostrar productos, así como cargar o guardar el catálogo desde o hacia un archivo.
En la función "mostrar_menu_principal" se imprime un menú con opciones para realizar acciones en el catálogo.
En la función "mostrar_menu_agregar_producto" se imprime un menú con opciones para agregar un producto de un tipo específico al catálogo.
En la función "mostrar_menu_mostrar_catalogo" se imprime un menú con opciones para mostrar productos de un tipo específico o del catálogo completo.
En la función "main" se utiliza un ciclo para recibir y procesar

Documentación: 

La clase Producto es la clase base de la cual heredan todas las demás clases. En este caso, su único atributo es "titulo", que es común a todos los productos.

Las clases Película, Serie y Documental heredan de la clase Producto y añaden atributos específicos para cada tipo de producto, como "actor_principal", "director", "año" y "temporadas".

La clase EventoDeportivo también hereda de la clase Producto, pero en este caso los atributos son diferentes, como "deporte", "fecha", "hora" y "lugar".

En todas las clases, el método "init" se encarga de inicializar los atributos de cada objeto. En las clases hijas, se llama al método "init" de la clase padre usando "super().init(titulo)" para inicializar el atributo "titulo".

Cada objeto creado a partir de estas clases tiene dos atributos adicionales: "costo_renta" y "costo_venta", los cuales se inicializan en 0. Estos atributos podrían ser actualizados posteriormente con métodos específicos para cada tipo de producto

Diagrama de bloques:  
El diagrama de bloques que se esta presentando, muestra de manera mas dinamica la manera en  la que los modulos se dividen y el orden en el que se ejecuta cada uno, van desde la ejecución de el archivo main hasta el modulo encargado de la eliminaciaon de cualquier producto, dicho diagrama se encuentra adjunto en el apartado "DIAGRAMA DE BLOQUE" 
