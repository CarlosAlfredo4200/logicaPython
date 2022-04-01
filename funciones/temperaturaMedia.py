# // En el valle de aburra afronta altas temperaturas año tras año.
# // crear una funcion que calcule latemperatua media de la tierra desde la toma de
# // 20 registros diarios de temperatura

#--- Crear funciòn -----
def mediaTemperatura():

    #---- Variables -------
    ingreso = 0
    medidasTermicas = []
    contador = 0
    sumaIngresados = 0

    while(contador < 5):
        print('')

        ingreso = float(input('Ingresa el dato: '))
        medidasTermicas.append(ingreso)
        contador = contador + 1
        sumaIngresados += ingreso

    else:

        #---- Ordenar de menor a mayos ----

        medidasTermicas.sort()
        maximo = max(medidasTermicas)
        minimo = min(medidasTermicas)

        temperaturaMedia = minimo + maximo

        mediaDia = temperaturaMedia / 2
        mediaGeneral = sumaIngresados / contador

        print('')
        print('Temperatura media Dia: '+format(mediaDia, ".2f"))
        print('Temperatura media general: ' + format(mediaGeneral, ".2f"))
        print('')

mediaTemperatura()
