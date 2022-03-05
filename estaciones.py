# Calcular la estación según un mes proporcionado por consola


mes = input('Digita el mes de consulta:').lower()


if (mes == 'enero' or mes == 'febrero'):
    print(f'La estacion es Invierno entrando a verano')
elif (mes == 'marzo'):
    print('La estacion  es Invierno')

elif (mes == 'abril' or mes == 'mayo'):
    print('La estacion  es verano')
elif (mes == 'junio'):
    print('La estacion es verano entrando al otoño')

elif (mes == 'julio' or mes == 'agosto'):
    print('La estacion  es otoño')
elif (mes == 'septiembre'):
    print('La estacion es otoño entrando a la primavera')

elif (mes == 'octubre' or mes == 'novienbre'):
    print('La estacion  es primavera')
elif (mes == 'diciembre'):
    print('La estacion es primavera entrando al invierno')
