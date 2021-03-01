class Restaurant: #Con Mayuscula incial

    def __init__(self, nombre, categoria, precio):
       self.nombre = nombre #atributo
       self.categoria = categoria
       self.precio = precio
        
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}')

#Instanciar o Llamar a la clase
restaurant = Restaurant('Pizzeria Mexico', 'Comida Picante', '50')
restaurant.mostrar_informacion()

restaurant2 = Restaurant('Hamburguesas Cacho', 'Comida Popular', '40')
restaurant2.mostrar_informacion()