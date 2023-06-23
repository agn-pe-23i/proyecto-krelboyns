# Importamos el modulo de catalogo para que alas opciones ingresadas puedan ser usadas en este modulo
import catalogo
# Hacemos una funcion para cargar catalago en el archivo de texto
def cargar_catalogo():
    nombre_archivo = input("Ingrese el nombre del archivo del catalogo que desea cargar: ")
    try:
        with open(nombre_archivo, "r") as archivo:
            catalogo.catalogo_productos = eval(archivo.read())
        print("El catálogo se ha cargado.")
# en caso de que el archivo no pueda ser encontrado se mandara un mensaje de error o que el archivo no pudo ser encontrado
    except FileNotFoundError:
        print("catalogo no existe.")
    except:
        print("Ocurrió un error.")
# Hacemos una funcion para que guarde el catalogo y lo ponga en un archivo .txt
def guardar_catalogo():
    nombre_archivo = input("Ingrese el nombre del archivo: ")
    try:
        with open(nombre_archivo, "w") as archivo:
            archivo.write(str(catalogo.catalogo))
        print("Se ha guardado correctamente.")
# en caso de que el catalogo no pueda ser guardado con exitow se tiene
    except:
        print("Ocurrió un error.")