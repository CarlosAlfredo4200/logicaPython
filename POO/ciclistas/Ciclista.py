#Codificar un programa que permita recibir el :
# nombre, edad, país y tiempo(minutos)) de la ultima prueba de crono individual de varios ciclistas del tour de Francia, 
# al final el software estará en la capacidad de indicar cual fue el ciclista con el mejor tiempo y mostrar todos sus datos


class Ciclista:
    def __init__(self):
        self.__nombre = None
        self.__edad = None
        self.__pais = None
        self.__tiempo = None
        
    #DECORADOR DE CLASE: palabras reservadas encima de una funcion @ propety=GET
#Metodos get para leer el valor un atributo

    listaCiclistas =[]

    def ingresar(self):
        newCiclista=dict(nombre=self.__nombre, edad=self.__edad, pais=self.__pais, tiempo= self.__tiempo)
        listaCiclistas.append(newCiclista)
        
    print(listaCiclistas)
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def edad(self):
        return self.__edad
    
    @property
    def pais(self):
        return self.__pais
    
    @property
    def tiempo(self):
        return self.__tiempo
    
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
            
    @pais.setter 
    def pais(self, pais):
        self.__pais = pais
        
     
         
    @tiempo.setter 
    def tiempo(self, tiempo):
        if(tiempo < 0):
            print('No puedes tener tiempo negativo!!!')
        else:
            self.__tiempo = tiempo   