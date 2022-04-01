# Crea una función que reciba una lista con valores númericos y devuelva el valor maximo y minimo ingresados.

def maxmin():
    print('')
    
    numeros = []
    numIngresado = ''
    
    numIngresado = input('Ingrese el numero o fin para terminar:').strip();
    while(numIngresado != 'fin'):
        
        nuevoNumero = float(numIngresado)
        numeros.append(nuevoNumero)
        numIngresado = input('Ingrese el numero o fin para terminar:')
        print('')
    else:
        
        numeros.sort()
        maximo = max(numeros)
        minimo = min(numeros)
 
        print('')
        print(numeros)
        print(f'El número maximo ingresado fue : {maximo}')
        print(f'El número minimo ingresado fue : {minimo}')
        print('')
                                                                                
maxmin()