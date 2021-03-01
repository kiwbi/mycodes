nombre = input('¿Cuál es tu nombre?: \r\n') #\r\n --> Salto de linea
print(f'Hola {nombre}')

#Leer datos que seran numeros
edad = input ('¿Cuál es tu edad?: \r\n')

#Convertir edad (string) a int
edad = int(edad)

if edad >=18:
    print('Ya puedes votar')
else:
    print('Aun no puedes votar')

#Mezclando con operadores

numero = input ('Agrega un número y te diré si es para o impar \r\n')
numero = int(numero)

if numero % 2 == 0:
    print(f'el número {numero} es par')
else:
    print(f'el número {numero} no es impar')