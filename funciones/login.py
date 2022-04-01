# Crear una subrutina llamada login, que reciba un nombre y contraseña del usuario y devuelva verdadero si en nombre de usuario es "admin" y la contraseña "adm123". Además recibe el número de intentos que se ha intentado hacer login y no se ha podido hacer login. 


def login():
    print('')
    contador = 0
    name = input('Ingrese el nombre de usuario : ')
    password = input('Ingrese la contraseña : ')
    
    while(name != 'admin' and password != 'admin123'):
        contador += 1
        name = input('Ingrese el nombre de usuario : ')
        password = input('Ingrese la contraseña : ')
        print('Lo siento no eres el administrador de la cuenta')
        print('')
    else:
        print('')
        print(f'Bienvenido {name}!!!')
        print(f'El número de intentos errados fue : {contador}')
        print('')
     
     
 
login()