#Iniciar un diccionario vacio
jugador = {}
print(jugador)

#Se une un jugador
jugador['nombre'] = 'Ariel'
jugador['puntaje'] = 0
print(jugador)

#Incrementod e puntaje
jugador['puntaje'] = 100
print(jugador)

#Accdeder a un valor
print(jugador.get('consola')) #Imprimira 'none' dado que el valor es inexistente
print(jugador.get('consola', 'No existe el valor consola')) #agregar mensaje

#Iterar en el diccionario
for llave, Valor in jugador.items():
    print(Valor)

#Eliminar jugador y puntaje
del jugador ['nombre']
del jugador ['puntaje']
print(jugador)