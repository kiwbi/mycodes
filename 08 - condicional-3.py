#Operadores and y or
#And --> lee que se cumplan todas als condiciones
#or --> lee que se cumpla al menos una de las condiciones declaradas
usuario_logueado = True
usuario_admin = True
if usuario_logueado or usuario_admin: 
    print('Administrador')
elif usuario_logueado:
    print('Acceso al sistema')
else: 
    print('Debes iniciar sesion')