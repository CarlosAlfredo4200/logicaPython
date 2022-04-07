
class Heroe:
    
    def __init__(self, name, poder, height):
            
        self.nombre = name
        self.poder = poder
        self.estatura = height
        self.tipoHeroe = None
        self.cantidadVida = None
      
    def saludar(self):
        print('Hola!!!')

# Utilizar la clase instancia

batman = Heroe('Bruce Wayne', 'Millonario', 45)

superMan = Heroe('Clar Kent', 'Volar', 1.95)

print(batman.nombre, batman.estatura)
print(superMan.nombre, superMan.poder, superMan.estatura)

batman.saludar()
 


#Acceder a un método
