# Crea una funciòn que reciba una lista con valores nùmericosy devuelva el valor maximo y minimo ingresados.

def maxmin():
    print('')
    
    numeros = []
    numIngresado = ''
    
    numIngresado = input('Ingrese el numero o fin para terminar:');
    while(numIngresado != 'fin'):
        
        nuevoNumero = numIngresado * 1
        numeros.append(nuevoNumero)
        numIngresado = input('Ingrese el numero :');
         
    else:
        
        maximo = max(numeros)
        manimo = min(numeros)
 
        print('')
        print(numeros)
        print(f'El número maximo ingresado fue : {maximo}')
        print(f'El número manimo ingresado fue : {manimo}')
        print('')
                                                                                
maxmin()