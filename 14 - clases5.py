class Restaurant: #Con Mayuscula incial

    def __init__(self, nombre, categoria, precio):
       self.nombre = nombre #atributo
       self.categoria = categoria
       self.precio = precio #Default: Public, PROTECTED, PRIVATE con doble guion bajo
        
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}')

    #Getters - GET = este método obtiene un valor
    def get_precio(self):
        return self.precio

    #Setters - SET = éste método agrega un valor o lo modifica
    def set_precio(self, precio):
        self.precio = precio

#Crear una clase hijo de Restaurante
class Hotel(Restaurant):
        def __init__(self, nombre, categoria, precio, valetparking):
            super().__init__(nombre, categoria, precio)
            self.valetparking = valetparking

        #Reescribir un metodo (debe llamarse igual)
        def mostrar_informacion(self):
            print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}, Valetparking: {self.valetparking}')
                
        #Agregar un metodo que solo exista en hotel
        def get_valetparking(self):
            return self.valetparking

hotel = Hotel('Hotel POO', '5 Estrellas', 200, 'Si')
hotel.mostrar_informacion()
valetparking = hotel.get_valetparking()
print(valetparking)