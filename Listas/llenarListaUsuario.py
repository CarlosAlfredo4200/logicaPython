# Construir un programa que reciba el tamaño de una lista 
# y la llene con números entregados por el usuario


lista = []

tamañoLista = int(input('Ingrese el tamaño deseado de la lista :'))

for k in range(tamañoLista):
     
     numeroIngresado = int(input('Ingresa el número :'))
     lista.append(numeroIngresado)
else:
    print(f'La lista obtenida es :{lista}')
        

# ------------------------ Version 2 ----------------------



 