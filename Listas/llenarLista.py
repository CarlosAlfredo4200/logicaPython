# Construir un programa que reciba el tamaño de una lista  
# y la llene con múltiplos de 7



tamañoLista = int(input('el tamaño deseado de la lista :'))

lista = []

for k in range(0, tamañoLista, 1):
    lista.append(k * 7)

print(lista)
