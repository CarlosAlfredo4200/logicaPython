#Los diccionarios en Python nos permitirán crear un conjunto 
# de datos de diferentes tipos almacenados en una sola variable:

persona = {
    'nombre': 'Carlos',
    'edad': 43,
    'estado':True
    
}

# print(persona['nombre'])
# print(persona.get('estado'))

print('')

# ---------Recorrer diccionario----------

for key, value in persona.items():
    print(f'{key} : {value}')
    
    
for value in persona.values():
    print(value)
     
