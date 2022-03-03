# Calcular la etapa de la vida, según la edad

edad = int(input('Ingresa la edad :'))


 
if (edad <= 14 ):
    print('Eres un niño aun!!!')
    
elif (edad == 15 or edad <= 28):
    print('Eres un Joven!!!')
    
elif (edad == 29 or edad <= 60):
    print('Eres un adulto!!!')
    
else :
    print('Eres un adulto mayor!!!')