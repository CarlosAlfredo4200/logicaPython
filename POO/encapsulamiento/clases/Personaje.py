#Si estoy dentro de la clase puedo protected _name = atributo protegido

#private __name

#Encapsular construir metodos publicos y atributos privados
# get saca el valor de latribulo (Visualizar)
# set ingresa el valor de latribulo (asignando valor a atributo)

class Personaje:
    def __init__(self):# self + parametros
        #Definir atributos y el atr self
        self.__nombre = None
        self.__edad = None


#DECORADOR DE CLASE: palabras reservadas encima de una funcion @ propety=GET
#Metodos get para leer el valor un atributo

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def edad(self):
        return self.__edad
    
    #Metodos set para ingresar el valor un atributo . No retornan nada
    #SIEMPRE VALIDAR EN SET
    
    @nombre.setter 
    def nombre(self, nombre):
        self.__nombre = nombre
         
    @edad.setter 
    def edad(self, edad):
        if(edad < 0):
            print('No puedes tener edades negativas!!!')
        else:
            self.__edad = edad
         
    
    


        