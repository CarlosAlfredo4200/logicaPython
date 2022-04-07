# Las Tuplas en PYTHON son estructuras de datos similares a las LISTAS, se diferencias en que estas son 
# INMUTABLES, es decir no puedo agregar o eliminar elementos de una tupla después de definirla:


# #Creando tuplas.

# estudiantes = ('Carlos', 'Juan Carlos')

# for estudiante in estudiantes:
#     print(estudiante)
 
 
# #convertir tupla a lista

# lista = list(estudiantes)
# lista.append('Maria')

# print(lista)
# #---------------------------------
# newtupla = tuple(lista)
# print(newtupla)
 
# #-------------------------

# Convertir la tupla=(50,45,20,30,40,87) en una lista que solo contenga números >40 


tuplaNumeros =  (50,45,20,30,40,87)

listaNumeros = []

for k in tuplaNumeros:
    if(k > 40):
          listaNumeros.append(k)
      
    nuevaDupla = tuple(listaNumeros)
print(nuevaDupla)
    
#---------------------------------------------
# Convertir la tupla=(50,45,20,30,40,87) en una lista que solo contenga números  PARES

# tupla=(50,45,20,30,40,87) 

# nuevaTuplaNumeros = []

# for item in tupla:
#      if(item % 2 == 0):
#          nuevaTuplaNumeros.append(item)

# print(nuevaTuplaNumeros)

