#Codificar un programa que permita recibir el :
# nombre, edad, país y tiempo(minutos)) de la ultima prueba de crono individual de varios ciclistas del tour de Francia, 
# al final el software estará en la capacidad de indicar cual fue el ciclista con el mejor tiempo y mostrar todos sus datos




class Carrera:
    def __init__(self, nombre, edad, pais, tiempo):
        self.nombre = nombre
        self.edad = edad
        self.pais = pais
        self.tiempo = tiempo
    
    def __str__(self):
          return f"Nombre: {self.nombre} edad: {self.edad} pais: {self.pais} tiempo:{self.tiempo}"
  
    def getTiempo(self):
          return self.tiempo

    def getNombre(self):
          return self.nombre
    
    def getEdad(self):
          return self.edad
    
    def getPais(self):
          return self.pais
      
      
def agregar():
    
    nombre = input('Ingrese nombre del corredor: ')
    edad = int(input('Ingrese la edad corredor: '))
    pais = input('Ingrese el pais del corredor: ')
    tiempo = int(input('Ingrese el tiempo corredor: '))
    
    nuevoCorredor = Carrera( nombre, edad, pais,tiempo  )
    listaCarreras.append(nuevoCorredor)

def listar():
    print('')
    print('Lista de corredores')
    
    for index in range(0,len(listaCarreras)):
         print(f'{index } : {listaCarreras[index]}')
         
        
    for index in range(0,len(listaCarreras)):
        
        listaTiempos.append(listaCarreras[index].getTiempo())
         
         
     
    minimo = min(listaTiempos)
    print('')
    for index in range(0,len(listaCarreras)):
        if(listaCarreras[index].getTiempo() == minimo):
         print('El corredor que logro el menor tiempo fue: ')
         print(' ')
         print('\t Nombre:',listaCarreras[index].getNombre())
         print('\t Edad:',listaCarreras[index].getEdad())
         print('\t Pais:',listaCarreras[index].getPais())
         print('\t Tiempo:',listaCarreras[index].getTiempo())
         
         
listaCarreras = []
listaTiempos = []
 
corredor1 = Carrera('Carlos', 43,'Colombia',4)
corredor2 = Carrera('Andrea', 42,'Medellin',3)
corredor3 = Carrera('Andrea', 41,'Medellin',2)

listaCarreras.append(corredor1)
listaCarreras.append(corredor2)
listaCarreras.append(corredor3)
opcion = -1
while(opcion != 0):
    print('')
    print('1 Para ingresar corredor')
    print('2 Para ver los resultados')
    print('0 Para salir')
    print('')
    opcion = int(input('Ingresa opcion deseada:'))
    if(opcion == 0):
        print('')
        print('Saliendo...')
    
    elif(opcion == 1):
        agregar()
    
    elif(opcion == 2):
        listar()
        
    else:
        print('')
        print('Opcion incorrecta')