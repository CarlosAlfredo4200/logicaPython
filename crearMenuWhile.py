num = 1
print('------------')
print('----Menu----')
print('------------')

print('0 salir')
print('1 sqrt')
print('0 saludar')



while(num != 0):
    num = int(input('Ingresa el número :'))
    
    if( num == 1):
        print('Digito 1')
    elif (num == 2 ):
        print('Digito 2')
    else:
        print('Digita una opcion valida')
        
else:
    print('Fin del while')
         