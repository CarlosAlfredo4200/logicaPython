# estudiantes = [
    
#     {
#         'nombre': 'Juan',
#         'edad': 32
#     },
    
#     {
#          'nombre': 'Carlos',
#         'edad': 43
#     }
# ]


# print(estudiantes)

print(' ')

# ¿Como hacer para agregar una nueva llave aun diccionario? append a un diccionario
# ¿A una lista de diccionario se puede recorrer? si ¿Como?

# ------- Agregar al diccionario o modificar ------------
# carros = {}

# carros["Nombre"]="Toyota"
# carros["Valor"]= 200000
# carros["Color"]="Red"

 
# print(carros)
# # ------- Eliminar al diccionario al eliminar la clave se elimina el valor ------------

    # del(carros["Color"])
# print(carros)

#----------------- Agenda ---------------

# agenda = { 
#           'Carlos':{"edad":43,
#                     "Estatura":1.80
#                     }, 
#           'Juan':[17,1.70],
#           'Joel':[12,1.60] 
#           }

# print(agenda)
# print(agenda['Carlos'])

#-----------------------------------------------

equipo = {10:"Paulo dybala", 11:"Douglas Costa", 7:"CR7"}
# print(equipo[10])# esta forma solo si existe
# print(equipo.get(11, 'No existe en el diccionario')) #Si no encuentra la clave

# #Busqueda directa
# print(10 in equipo) #retorna true o false

# #Mostrar solo las claves
# print(equipo.keys())

# #Mostrar solo values
# print(equipo.values())

# #Mostrar todo
# print(equipo.items()) #Recorrerlo en tuplas

# #Mostrar el tamaño
# print(len(equipo))

#limpiar diccionario
#print(equipo.clear())

#-----------------Recorrer Diccionarios -----------------------

for item in equipo:
    print(item, ':', equipo[item])