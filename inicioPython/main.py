#Comentario   versionamiento NTV001 se crea main.py para codificar condicionales
 
nivelDeAgua = int(input('Digita la cantidad de agua de HidroItuango :'))
print(f'El nivel del agua es {nivelDeAgua}')

if(nivelDeAgua < 200 ):
    print('Niveles bajos')
elif(nivelDeAgua >= 200 and nivelDeAgua < 450 ):
    print('Niveles optimos')
else :
    print('Niveles altos')
        
 