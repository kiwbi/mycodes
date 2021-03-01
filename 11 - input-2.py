pregunta = 'Agrega un numero y te dire siu es par o impar \r\n'
pregunta += 'Escribe "cerrar" para salir de la app \r\n'
preguntar = True

while preguntar:

    #Mezclando con operadores

    numero = input (pregunta)

    if numero == 'cerrar':
        preguntar = False
    else: 
        numero = int(numero)

        if numero % 2 == 0:
            print(f'el número {numero} es par')
        else:
            print(f'el número {numero} no es impar')