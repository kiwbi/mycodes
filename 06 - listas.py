lenguajes = ['Python', 'Kotlin', 'Java', 'JavaScript']
print(lenguajes)

#Los arrays (lists) comienzan en la posicion 0
print(lenguajes[0]) #Python

#Ordenar los elementos alfabeticamente: Java, JavaScript, Kotlin, Python
lenguajes.sort()
print(lenguajes)

#Acceder a un elemento dentro de un texto
#Para mezclar un String con una Variable, debe comenzar con f'
aprendiendo = f'Estoy aprendiendo {lenguajes[3]}'
print(aprendiendo)

#Modificando valores de un arreglo (list)
lenguajes[2] = 'PHP' #Se modifica la posicion dos de la lista
print(lenguajes)

#Agregar elementos a un arreglo (list)
lenguajes.append('Ruby') #append agrega un elemento a la lista
print(lenguajes)

#Forma UNO de eliminar de un arreglo (list)
del lenguajes[1] #Se elimina el elemento UNO de la lista
print(lenguajes)

#Forma DOS de eliminar de un arreglo (list)
lenguajes.pop() #pop elimina el ultimo elemento de la lista
print(lenguajes)

#Eliminar con pop una posicion en especial
lenguajes.pop(0) #Se elimina el elemento cero de la lista
print(lenguajes)

#Eliminar por nombre
lenguajes.remove('PHP')
print(lenguajes)