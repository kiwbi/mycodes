class Restaurant: #Con Mayuscula incial

    def __init__(self, nombre, categoria, precio):
       self.nombre = nombre #atributo
       self.categoria = categoria
       self.__precio = precio #Default: Public, PROTECTED, PRIVATE con doble guion bajo
        
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.__precio}')

    #Getters - GET = este método obtiene un valor
    def get_precio(self):
        return self.__precio

    #Setters - SET = éste método agrega un valor o lo modifica
    def set_precio(self, precio):
        self.__precio = precio

#Crear una clase hijo de Restaurante
class Hotel(Restaurant):
        def __init__(self, nombre, categoria, precio):
            super().__init__(nombre, categoria, precio)

hotel = Hotel('Hotel POO', '5 Estrellas', 200)
hotel.mostrar_informacion()