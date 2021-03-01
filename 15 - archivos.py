def app():
    #crear archivo
    archivo = open('archivo.txt', 'w') #w es archivo de escritura, y si no existe lo creará.
    
    #Generar numeros en archivo
    for i in range(0,20):
        archivo.write('esta es la linea' + str(i) + "\r\n")
    
    #Cerrar archivo
    archivo.close()

app()