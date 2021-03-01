import pandas
import requests
import statistics

#OBTENER EL PROMEDIO DE COMPRA/VENTA DE USD CON LA API
r = requests.get("https://api.recursospython.com/dollar") #Realiza un request a la API y guardar los datos en la variable R
cotizacion = statistics.mean(r.json().values()) #El Means hace un promedio de los valores de compra y venta que viajan en el json y se guarda enla variable cotizacion
print(cotizacion) #Imprime la cotizacion

#Crear una funcion que convierta UDS a $
def dolar_a_pesos(precio_en_usd):
    return precio_en_usd * cotizacion

# 1- Leer Excel
excel = pandas.read_excel("productos.xlsx") #Si el escel esta en otra carpeta debemos colocar la ruta
# 2- Convertir USD a $ y escribir en la columna PRECIO $
excel["PRECIO $"] = excel["PRECIO USD"].apply(dolar_a_pesos)
excel.to_excel("productos.xlsx", index=False) #El index es para que Pandas no cree una columna extra