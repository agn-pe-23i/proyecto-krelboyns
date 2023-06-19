[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/LCXMIOgt)
# Proyecto

PROFESOR:  ABEL GARCÍA NÁJERA
ALUMNOS: 
- RAMIREZ AGUILERA JESÚS EMMANUEL 2223068873
 -RODRIGUEZ BECERRIL ANTONIO 2213026390
UEA: PROGRAMACIÓN ESTRUCTURADA CB01C
CARRERA: INGENIERÍA EN COMPUTACIÓN
**************************************************


OBJETIVO: Aplicar todos los conocimientos adquiridos durante la UEA.

INTRODUCCION: 
El objetivo principal de esta actualización es proporcionar a los usuarios una plataforma actualizada y fácil de usar, donde puedan acceder a una amplia variedad de películas, series, documentales y eventos deportivos en vivo. El nuevo sistema deberá permitir a los usuarios explorar el catálogo, obtener información detallada de cada producto, alquilar o comprar, y disfrutar de una experiencia de lectura detallada.Para esto se ponen  los requisitos clave y se propone la creación de un nuevo modelo de alquiler y ventas. Se ha implementado un algoritmo en Python que resuelve de manera correcta las tareas asignadas, lo que permite una gestión eficiente del inventario. Además, se explorarán diferentes métodos y mejores prácticas para mejorar la capacidad de respuesta y la facilidad de uso de la plataforma.

COMENTARIOS DDE LA IMPLEMENTACION Y DISEÑO: 

El código muestra una implementación de clases en Python para un catálogo de productos que puede agregar, buscar, eliminar y mostrar diferentes tipos de productos. Los productos son de cuatro tipos: Película, Serie, Documental y EventoDeportivo. Cada tipo de producto tiene diferentes atributos, que son inicializados en el constructor. 
La clase Catalogo es la clase principal que administra todos los productos. Contiene los métodos para agregar, buscar, eliminar y mostrar productos, además de cargar y guardar el catálogo en un archivo. También contiene los métodos que muestran diferentes tipos de productos y todo el catálogo.
Los métodos de mostrar catálogo, buscar y eliminar reciben un argumento adicional que indica el tipo de producto a mostrar, buscar o eliminar. Los métodos de mostrar productos eliminan la necesidad de repetir código.
La función principal es un bucle infinito que muestra el menú principal al usuario y llama a los métodos correspondientes para cada elección del usuario. La función main() se ejecuta al final del archivo para iniciar el programa.
- La clase "Producto" define un objeto con una propiedad "titulo".
- Las clases "Pelicula", "Serie", "Documental" y "EventoDeportivo" heredan de "Producto" y definen objetos con propiedades relevantes para cada tipo de producto.
- La clase "Catalogo" define un objeto que puede agregar, buscar, eliminar y mostrar productos, así como cargar o guardar el catálogo desde o hacia un archivo.
- En la función "mostrar_menu_principal" se imprime un menú con opciones para realizar acciones en el catálogo.
- En la función "mostrar_menu_agregar_producto" se imprime un menú con opciones para agregar un producto de un tipo específico al catálogo.
- En la función "mostrar_menu_mostrar_catalogo" se imprime un menú con opciones para mostrar productos de un tipo específico o del catálogo completo.
- En la función "main" se utiliza un ciclo para recibir y procesar las opciones del usuario y llamar a las funciones correspondientes del catálogo.

En este código se definen varias clases que representan diferentes tipos de productos, como películas, series, documentales y eventos deportivos en vivo. Cada clase tiene atributos específicos que la distinguen de las demás, como el actor principal y el director en el caso de las películas, o el tema y el año en el caso de los documentales. Además, cada clase hereda de la clase base Producto, que tiene un solo atributo común a todas las clases: el título del producto.

Es importante destacar que en las definiciones de las clases se utiliza el método _init_ para inicializar los atributos de cada objeto. Sin embargo, se ha cometido un error de sintaxis al escribirlo como init (con un solo guion bajo), lo cual hace que no se llame correctamente al método y los atributos no se inicialicen correctamente. Para corregir esto, debería cambiar init por _init_ (con dos guiones bajos).

DOCUMENTACIÓN: 
En este apartado se estara expliccando de maner ageneral en que consisite cada modulo que integrael código; 

