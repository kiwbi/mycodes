import os #Importar libreria OS que cuenta con funciones para manejra archivos

CARPETA = 'Contactos/' #la mayuscula la define como una constante, no se debe modificar el valor
EXTENSION = '.txt' #Extension de archivos

#Contactos
class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

def app():

    #Revisar si la carpeta existe o no
    crear_directorio()

    #Mostrar menu de opciones
    mostrar_menu()

    #Preguntar al usuario la accion a realizar
    preguntar=True
    while preguntar:
        opcion = input('Seleccione una opcion: \r\n')
        opcion = int(opcion)

        #Ejecutar las opciones
        if opcion == 1:
            agregar_contacto()
            preguntar=False
        elif opcion == 2:
            editar_contacto()
            preguntar=False
        elif opcion == 3:
            mostrar_contactos()
            preguntar=False
        elif opcion == 4:
            buscar_contacto()
            preguntar=False
        elif opcion == 5:
            eliminar_contacto()
            preguntar=False
        else:
            print('Opcion no válida, intente de nuevo')

def mostrar_menu():

def agregar_contacto():

def existe_contacto(nombre):

def editar_contacto():

def mostrar_contactos():

def buscar_contacto():

def eliminar_contacto():
    nombre = input('Seleccione el contacto que desea eliminar: \r\n')

    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('\r\nEliminado correctamente')
    except IOError:
        print('El archivo no existe')
        print('IOError')


    nombre = input('Seleccione el contacto que desea buscar: \r\n')

    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('\r\n Informacion del Contacto \r\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')  
    except IOError:
        print('El archivo no existe')
        print('IOError')

    #Reiniciar la app
    app()


    archivos = os.listdir(CARPETA)
    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]
    for archivo in archivos_txt:
        with open (CARPETA + archivo) as contacto:
            for linea in contacto:
                #Imprime los contenidos
                print(linea.rstrip())
            #Imprime un separador entre contactos
            print('\r\n')


    print('Escribe el nombre del contacto a editar')
    nombre_anterior = input('Nombre del contacto que desea editar: \r\n')

    #Revisar si el archivo ya existe antes de editarlo
    existe = existe_contacto(nombre_anterior)

    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:

            #Resto de los campos
            nombre_contacto =  input('Agrega el Nuevo Nombre: \r\n')
            telefono_contcto = input('Agrega el Nuevo Teléfono: \r\n')
            categoria_contacto = input('Agrega la Nueva Categoria : \r\n')

            #Instanciar
            contacto = Contacto(nombre_contacto, telefono_contcto, categoria_contacto)

            #Escribir en el archivo
            archivo.write('Nombre:' + contacto.nombre + '\r\n') #NombreDelObjetoInstanciado.Atributo
            archivo.write('Telefono:' + contacto.telefono + '\r\n') #NombreDelObjetoInstanciado.Atributo
            archivo.write('Categoria:' + contacto.categoria + '\r\n') #NombreDelObjetoInstanciado.Atributo

            #Renombrar el archivo
            os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)

            #Mostrar mensaje de exito
            print('\r\n Contacto editado Correctamente \r\n')

    else:
        print('Ese contacto no existe')

    #Reiniciar la aplicacion
    app()


    print('Escribe los datos para agregar el nuevo Contacto')
    nombre_contacto =  input('Nombre del Contacto: \r\n')

    #Revisar si el archivo ya existe
    existe = existe_contacto(nombre_contacto)


    if not existe:
        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:

            #Resto de los campos
            telefono_contcto = input('Agregar Teléfono: \r\n')
            categoria_contacto = input('Categoria Contacto: \r\n')

            #Instanciar la clase
            contacto = Contacto(nombre_contacto, telefono_contcto, categoria_contacto)

            #Escribir en el archivo
            archivo.write('Nombre:' + contacto.nombre + '\r\n') #NombreDelObjetoInstanciado.Atributo
            archivo.write('Telefono:' + contacto.telefono + '\r\n') #NombreDelObjetoInstanciado.Atributo
            archivo.write('Categoria:' + contacto.categoria + '\r\n') #NombreDelObjetoInstanciado.Atributo

            #Mostrar un mensaje de éxito
            print('\r\n Contacto creado Correctamente \r\n')
    else:
        print('Ese Contacto ya existe')
    
    #Reiniciar la App   
    app()


    print('Selecciones del menú lo que desea hacer:')
    print('1) Agregar Nuevo Contacto')
    print('2) Editar Contacto')
    print('3) Ver Contactos')
    print('4) Buscar Contactos')
    print('5) Eliminar Contactos')


    if not os.path.exists(CARPETA):
        #Si la carpeta no existe, crearla
        os.makedirs(CARPETA)
    

    return os.path.isfile(CARPETA + nombre + EXTENSION)