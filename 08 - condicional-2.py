#Ejemplo Elif
ocupacion = 'Jubilado'

if ocupacion == 'Estudiante':
    print('Tienes el 50% de descuento')
elif ocupacion == 'Jubilado':
    print('Tienes 75% de descuento')
elif ocupacion == 'Desempleado':
    print('Tienes un 10% de descuento')
else:
    print('Debes pagar el 100%')