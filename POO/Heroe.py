
class Heroe:
    
    def __init__(self, name, poder, height):
            
        self._nombre = name
        self._poder = poder
        self._estatura = height
        self.tipoHeroe = None
        self.cantidadVida = None
      
    def saludar(self):
        print('Hola!!!')

# Utilizar la clase instancia

batman = Heroe('Bruce Wayne', 'Millonario', 45)

superMan = Heroe('Clar Kent', 'Volar', 1.95)

#print(batman.nombre, batman.estatura)
print(superMan._nombre, superMan._poder, superMan._estatura)

batman.saludar()
 


#Acceder a un método
