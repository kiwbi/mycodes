#Creando un diccionario simple
cancion = {
    'artista': 'Metallica', #Llave y Valor
    'cancion': 'Enter Sandman',
    'lanzamiento': '1992,',
    'likes': 3000
}

print(cancion['artista']) #Imprime el valor Metallica de la llave Artista
print(cancion) #Imprime diccionario completo

#Mezclar con un string
artista = cancion['artista']
print(f'Estoy escuchando {artista}')

print(cancion)

#Agregar nuevos valores
cancion['playlist'] = 'Heavy metal' #agregar llave y valor nuevos. // Si no existe lo agrega
print(cancion)


#Reemplazar valor existente
cancion['cancion'] = 'Seek & Destroy' #Reemplazar valor de una llave // Si existe lo remeplaza
print(cancion)

#Eliminar  valores
del cancion['lanzamiento']
print(cancion)