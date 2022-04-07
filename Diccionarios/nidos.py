# ¿Una lista de diccionario se puede recorrer? si ¿Como?
# ------------Lista [] de diccionarios {} ------------

persona1 = {
    'nombre': 'Carlos',
    'edad': 43,
    'estado': True
}
persona2 = {
    'nombre': 'Andrea',
    'edad': 42,
    'estado': False
}
persona3 = {
    'nombre': 'Juan',
    'edad': 17,
    'estado': True
}

# Forma 1
lista = [persona1, persona2, persona3]


# for k in lista:
#    print( k)

# --------------------------------

inventario = []
inventario.append(
    {
        'nombre': 'Carlos',
        'edad': 43,
        'estado': True
    }
)

inventario.append(
    {
        'nombre': 'Andrea',
        'edad': 42,
        'estado': False
    }
)

inventario.append(
    {
        'nombre': 'Juan',
        'edad': 17,
        'estado': True
    }
)



for k in inventario:
     
    print(' ')
    print('\t Nombre:', k['nombre'])
    print('\t Edad:', k['edad'])
    print('\t Estado:', k['estado'])
    
#------Buscar dato especifico--------
print(' ')
buscar = input('¿A quien buscas? :')
for item in inventario:
    if buscar == item['nombre']:
        print(' ')
        print('\t Nombre:', item['nombre'])
        print('\t Edad:', item['edad'])
        print('\t Estado:', item['estado'])
 
    
    
 