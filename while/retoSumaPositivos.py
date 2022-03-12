# Construir un programa que reciba números enteros y los sume mientras estos sean posotivos, 
# si se digita un número negativo el programa debe terminar.

numeroIngresado = 0
resultado = 0

numeroIngresado = int(input('Ingresa el número :'))
while(numeroIngresado > 0 ):
     resultado += numeroIngresado
     numeroIngresado = int(input('Ingresa el número :'))
else:
    print(f'El resultado de la suma es :{resultado}')









 