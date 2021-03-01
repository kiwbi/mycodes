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

#Instanciar o Llamar a la clase
restaurant = Restaurant('Pizzeria Mexico', 'Comida Picante', '50')
#restaurant._precio=80 #No sera posible modificar el monto con PRIVATE __ (Se necesita un metodo Get/Set)
restaurant.mostrar_informacion()
restaurant.set_precio(80)
precio = restaurant.get_precio()
print(precio)

restaurant2 = Restaurant('Hamburguesas Cacho', 'Comida Popular', '20')
restaurant2.mostrar_informacion()
restaurant2.set_precio(40)
restaurant2.get_precio()