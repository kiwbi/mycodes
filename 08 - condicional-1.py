#Revisar si una condicion es mayor a
balance = 500
if balance > 0:
    print('Usted puede abonar')
else:
    print('Usted no posee saldo')

#likes
likes = 200
if likes >= 200:
    print('Excelente! 200 Likes')
else: 
    print('Ups! aún te falta para los 200!')

#If con texto
lenguaje = 'Python'
if  lenguaje == 'Python':
    print('Excelente decision!')

#Evaluar un Boolean
usuario_autenticado = True

if usuario_autenticado: #No es encesario agregar el operador: == True:
    print('Usuario correctamente verificado')
else:
    print('Debes iniciar sesion!')

#Evaluar un elemento de una lista
lenguajes = ['Python', 'Kotlin', 'Java', 'JavaScript']
if 'PHP' in lenguajes:
    print('PHP si existe')
else:
    print('PHP no está en la lista')

#If anidados
usuario_autenticado = True
usuario_admin = False

if usuario_autenticado:
    if usuario_admin:
        print('ACCESO TOTAL')
    else:
        print('Acceso al sistema')
else:
    print('Debes iniciar sesion!')