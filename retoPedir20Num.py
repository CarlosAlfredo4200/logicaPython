
# Pedir 20 números y contar cuantos de los ingresados son negativos 

print('Hallar la cantidad de números negativos')
print('')
positivos = 0
ingreso = 0
negativos = 0
repeticion = 0

while(repeticion < 5):
    ingreso = int(input('Ingresa el número :'))
    repeticion += 1   
    if(ingreso > 0 ):
        positivos += 1
    else :
        negativos += 1
        
else:
    print(f'N° de positivos : {positivos} y N° de  negativos fueron : {negativos}')
    

