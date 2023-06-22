[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/LCXMIOgt)
# Proyecto
PROFESOR:Abel García Nájera

ALUMNOS:

RAMÍREZ AGUILERA JESÚS EMMANUEL 2223068873

RODRÍGUEZ BECERRIL ANTONIO 2213026390

UEA: PROGRAMACIÓN ESTRUCTURADA CB01C
CARRERA: INGENIERÍA EN COMPUTACIÓN

**************************************************************************
                                                              INTRODUCCIÓN:

 
En la actualidad, los servicios de streaming se han vuelto muy populares como una opción para que las personas disfruten de una amplia variedad de contenido, como películas, series, documentales y eventos deportivos en vivo, directamente desde sus hogares. Con el objetivo de mantenerse actualizados y proporcionar una experiencia de usuario mejorada, los servicios de streaming necesitan actualizar sus sistemas de alquiler y venta de contenido.

Para lograrlo, es esencial contar con un catálogo completo y actualizado que contenga información detallada sobre las películas, series, documentales y eventos deportivos en vivo disponibles en el servicio. Además, se requiere un sistema que permita interactuar eficientemente con este catálogo.

En este escenario, se emplearán los conocimientos adquiridos en el curso de programación estructurada para desarrollar un código que cumpla con las necesidades mencionadas. A través del diseño de un programa adecuado, se espera crear un sistema que facilite la correcta y completa manipulación del catálogo de productos, permitiendo a los usuarios acceder y gestionar de manera eficiente el alquiler y la venta de contenido.

El código implementará los principios de programación estructurada, prestando atención a la organización y estructura del código, utilizando funciones y estructuras de control para llevar a cabo operaciones específicas, y brindando una interacción intuitiva con el usuario a través de menús que guíen las acciones a realizar en el catálogo de productos.


                                                              DOCUMENTACIÓN:
                                                              

El módulo con el nombre de catálogo implementa un programa para administrar un catálogo de productos en un servicio de streaming.
Se define una lista vacía llamada "catalogo" que se utilizará para almacenar los datos de los productos.
Se definen varias funciones para agregar diferentes tipos de productos al catálogo: películas, series, documentales y eventos deportivos en vivo. Cada función solicita al usuario que ingrese los detalles del producto correspondiente (como título, actor principal, director, etc.) y luego agrega un diccionario con esos detalles al catálogo.
La función "menu_agregar()" muestra un menú al usuario para seleccionar el tipo de producto que desea agregar. Dependiendo de la opción seleccionada, se llama a la función correspondiente para agregar ese tipo de producto.
La función "buscar_producto()" permite al usuario buscar productos en el catálogo utilizando una palabra clave. Se recorre el catálogo y se compara la palabra clave con los títulos de los productos. Se muestran los productos coincidentes encontrados.
La función "eliminar_producto()" permite al usuario eliminar un producto del catálogo. Se solicita al usuario que ingrese el título del producto a eliminar y se busca en el catálogo. Si se encuentra, se elimina del catálogo; de lo contrario, se muestra un mensaje de error.
La función "mostrar_catalogo()" muestra un menú al usuario para visualizar el catálogo de productos. Dependiendo de la opción seleccionada, se llaman a funciones específicas para mostrar las películas, series, documentales, eventos deportivos o todo el catálogo.
Las funciones de visualización (mostrar_peliculas(), mostrar_series(), mostrar_documentales(), mostrar_eventos_deportivos() y mostrar_todo()) recorren el catálogo y muestran los productos correspondientes.
La función "print_producto()" se utiliza para imprimir los detalles de un producto en un formato legible.
Agregar, buscar, eliminar y mostrar productos en un catálogo de un servicio de streaming. Proporciona una interfaz simple para interactuar con el catálogo y administrar los productos de manera eficiente.

Para el módulo de archivo contiene dos funciones: cargar_catalogo() y guardar_catalogo(), que se utilizan para cargar y guardar un catálogo de productos en un archivo de texto.

La función cargar_catalogo():

Solicita al usuario que ingrese el nombre del archivo del catálogo que desea cargar.
Intenta abrir el archivo en modo lectura ("r").
Si el archivo existe, lee su contenido y utiliza la función eval() para evaluarlo como código Python.
El resultado de la evaluación se asigna a la variable catalogo.catalogo_productos, que aparentemente es una variable definida en el módulo catalogo. Esto implica que el archivo de catálogo contiene una representación válida de un diccionario o una lista en Python.
Si el archivo no existe, se captura la excepción FileNotFoundError y se muestra un mensaje de error.
Si ocurre cualquier otro tipo de excepción, se muestra un mensaje genérico de error.
La función guardar_catalogo():

Solicita al usuario que ingrese el nombre del archivo en el que desea guardar el catálogo.
Intenta abrir el archivo en modo escritura ("w").
Si el archivo se abre correctamente, se escribe una representación en forma de cadena del contenido de catalogo.catalogo en el archivo. Se asume que catalogo.catalogo es una variable que contiene el catálogo de productos definido en el módulo catalogo.
Si ocurre algún error durante el proceso de guardado, se muestra un mensaje genérico de error.
En resumen, estas funciones permiten cargar un catálogo de productos desde un archivo y asignarlo a una variable en el módulo catalogo, así como guardar el contenido de esa variable en un archivo de texto. La forma en que se almacena y se accede al catálogo de productos en el módulo completo no se muestra en el código proporcionado, por lo que es necesario revisar otras partes del programa para comprender completamente cómo se utiliza esta funcionalidad.

El módulo main es el módulo principal donde se importan las funciones especificadas en los módulos anteriores.
Importa los módulos "catalogo" y "archivo_catalogo". Estos módulos contienen funciones relacionadas con la manipulación y gestión del catálogo de productos.

Define la función "menu_principal()" que muestra un menú de opciones al usuario y solicita que seleccione una opción. Las opciones incluyen agregar un producto, buscar un producto, eliminar un producto, mostrar el catálogo, cargar un catálogo, guardar un catálogo y salir. La función devuelve la opción seleccionada.

Define la función "ejecutar_opcion(opcion)" que recibe la opción seleccionada por el usuario y ejecuta la función correspondiente según la opción seleccionada. Por ejemplo, si la opción es "1", se llama a la función "catalogo.menu_agregar()" para agregar un producto al catálogo. Si la opción es "2", se llama a la función "catalogo.buscar_producto()" para buscar un producto, y así sucesivamente. Si la opción es "7", se muestra un mensaje de despedida.

Define la función "main()" que se encarga de ejecutar el programa principal. Utiliza un bucle "while True" para solicitar continuamente la opción al usuario y ejecutarla. Si la opción es "7", se rompe el bucle y el programa finaliza.

La línea "if name == "main":" se utiliza para verificar si el script se está ejecutando como el programa principal. Esto permite que el código dentro de este bloque solo se ejecute cuando el archivo se ejecuta directamente, no cuando se importa como un módulo. En este caso, se llama a la función "main()" para iniciar el programa.

PARA EL USO DEL PROGRAMA PRINCIPAL
se requiere descargar la carpeta contenida en el repositorio de GitHub con el nombre "proyecto". Una vez esté descargada, se tendrá que abrir con la aplicación de PyCharm. Una vez ya esté abierta, se tiene que descargar el catálogo, el cual es un archivo con formato de texto, es decir, .txt.

                                             COMENTARIOS DE IMPLEMENTACION Y DISEÑO: 

                                             
El código está constituido por 3 módulos. El código del módulo de catálogo fue diseñado para permitir al usuario agregar nuevos productos, buscar productos por palabra clave, eliminar productos y mostrar el catálogo completo o productos específicos.
El catálogo se almacena en una lista llamada "catalogo", donde cada producto se representa como un diccionario con diferentes atributos dependiendo del tipo de producto (película, serie, documental o evento deportivo en vivo).
El programa presenta un menú con opciones para realizar diferentes acciones. Al seleccionar la opción correspondiente, se llaman a las funciones adecuadas para llevar a cabo la operación deseada. Por ejemplo, al seleccionar la opción de agregar producto, se muestra otro menú para elegir el tipo de producto y luego se llama a la función correspondiente para solicitar los detalles del producto y agregarlo al catálogo.
La función de búsqueda permite al usuario ingresar una palabra clave y busca en el catálogo los productos cuyos títulos contienen esa palabra clave. Los resultados coincidentes se muestran en pantalla.

La función de eliminación solicita al usuario que ingrese el título del producto que desea eliminar. Si el producto se encuentra en el catálogo, se elimina de la lista. En caso contrario, se muestra un mensaje de error.
La función de visualización muestra diferentes categorías de productos o todo el catálogo, dependiendo de la opción seleccionada por el usuario. Recorre el catálogo y muestra los detalles de los productos correspondientes.
En general, este código proporciona una estructura básica y funcionalidades principales para administrar un catálogo de productos en un servicio de streaming, pero se pueden agregar más funcionalidades y mejoras según sea necesario.

Para el módulo de archivo se usó un diseño donde se define la función "cargar_catalogo()" que se encarga de cargar un catálogo desde un archivo de texto. Esta función solicita al usuario que ingrese el nombre del archivo del catálogo que desea cargar.

Dentro de la función "cargar_catalogo()", se utiliza un bloque "try-except" para manejar posibles excepciones durante el proceso de carga del catálogo. Se abre el archivo especificado en modo lectura ("r") y, si el archivo existe, se lee su contenido utilizando el método "read()".
Luego, se utiliza la función "eval()" para evaluar el contenido leído como código Python. Se asume que el contenido del archivo representa una estructura de datos válida en Python, como un diccionario o una lista.
El resultado de la evaluación se asigna a la variable "catalogo.catalogo_productos", que aparentemente es una variable definida en el módulo "catalogo". Esto implica que el archivo de catálogo contiene una representación válida de los productos del catálogo.

Si el archivo no existe, se captura la excepción "FileNotFoundError" y se muestra un mensaje de error indicando que el catálogo no existe. Si ocurre cualquier otro tipo de excepción durante el proceso de carga, se captura y se muestra un mensaje genérico de error.

Además, el código también define la función "guardar_catalogo()" que se encarga de guardar el catálogo en un archivo de texto. Esta función solicita al usuario que ingrese el nombre del archivo en el que se desea guardar el catálogo.
Dentro de la función "guardar_catalogo()", se utiliza un bloque "try-except" para manejar posibles excepciones durante el proceso de guardado. Se abre el archivo especificado en modo escritura ("w") y, si el archivo se abre correctamente, se escribe una representación en forma de cadena del contenido de "catalogo.catalogo" en el archivo.

Se asume que "catalogo.catalogo" es una variable que contiene el catálogo de productos definido en el módulo "catalogo".
Si ocurre algún error durante el proceso de guardado, se captura la excepción y se muestra un mensaje genérico de error.

                                                   DIAGRAMA DE ESTRUCTURA: 

[Presentación1.pdf](https://github.com/agn-pe-23i/proyecto-krelboyns/files/11840458/Presentacion1.pdf)

El diagrama de estructura muestra cómo del módulo principal se desprenden otros dos módulos en los cuales estarán definidas las funciones principales para el funcionamiento del módulo principal.
Los dos módulos son "archivo_catalogo", donde se desprenden las funciones de almacenamiento del catálogo, y "catalogo", que almacena todas las funciones principales de edición del catálogo, como agregar producto, eliminar producto, etc.

