# Codificar un programa que presente un menu de 4 opciones
# y reciba un numero natural para realizar las siguientes opciones

import math
num = 1
opcion = 0
print('Menu de opciones a ejecutar: ')
print('')
 

print('1 Encuentre si el numero es multiplo de 2')
print('2 Encuentre la raiz cuadrada del número')
print('3 suamr 100 al número ingresado')
print('4 Elevar la la 12 potencia el número ingresado')
print('0 terminar')
print('')



while(num != 0):
    num = int(input('Ingresa el número :'))
    opcion = int(input('Ingresa la opcion :'))
    
    if(opcion == 1):
            if( num % 2 == 0 ):
                 print(f'El número {num} si es multiplo de 2')
                 print('')
            else:
                print(f'El número {num} no es multiplo de 2')
                print('')
                
                
    elif(opcion == 2):
            print(f'La raiz cuadrada de {num } es {math.sqrt(num)}')
            print('')
            
    elif(opcion == 3):
            suma = num + 100
            print(f'La suma de  {num } + 100 es : {suma}')
            print('')
            
    elif(opcion == 4):
            potencia = num ** 6
            print(f'La potencia  12 de {num } es : {potencia}')
            print('')
            
            
            
            
 
    
        
else:
    print('Fin del while')
         