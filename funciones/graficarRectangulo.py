# Escriba un programa que pida la base y la altura de un rectángulo y permita calcular: Area, perimetro y grafucar el rectàngulo.

def graficarRectangulo ():
    
    print('')
    base = float(input('Ingrese el valor de la base: '))
    altura = float(input('Ingrese el valor de la Altura: '))
     #-- Variables --
     
    print('')
    puntos = ''
    area = 0
    perimetro = 0

    # ---- Calcular ---
    area = base * altura
    perimetro = 2 * (base + altura)

    print(f'El area del reactàngulo es: ${format(area, ".2f")}')
    print(f'El perimetro del reactàngulo es: ${format(perimetro, ".2f")}')
    print('')

    # -- Graficar --
    
    for item in range(0, int(base), 1):
        puntos += '*'+ ' '
        
    for item in range(0, int(altura), 1):
        print(puntos)
         
    print('')
         


graficarRectangulo()


