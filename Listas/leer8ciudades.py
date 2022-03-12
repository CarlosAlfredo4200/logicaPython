# Leer 8 ciudades colombianas, guardarlas en una lista 
# y mostrar en orden inverso los datos ingresados



listaCiudades = [];
for k in range(0, 3 , 1):
    ciudadIngresada = input('Ingrese la ciudad :')
    listaCiudades.append(ciudadIngresada)

listaCiudades.reverse()
print(listaCiudades)
    
    
    