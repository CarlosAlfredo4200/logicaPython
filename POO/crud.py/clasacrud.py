class Persona:
  def __init__(self, nombre, apellido, telefono, correo):
      self.nombre  = nombre
      self.apellido = apellido
      self.telefono = telefono
      self.correo = correo
    
  def __str__(self):
      return f"Nombre: {self.nombre} Apellido: {self.apellido} Telefono: {self.telefono} correo:{self.correo}"
  
  def getNombre(self):
      return self.nombre
  def getApellido(self):
      return self.apellido
  
  #--- Metodos para actualizar ---
  
  def setNombre(self, newNombre):
      self.nombre = newNombre
      
  def setApellido(self, newApellido):
      self.apellido = newApellido
  
  def setTelefono(self, newTelefono):
      self.telefono = newTelefono
  
  def setCorreo(self, newCorreo):
      self.correo = newCorreo
      
#----------------- Funciones --------------------------------
def create():
    nombre = input('Ingrese nombre :')   
    apellido = input('Ingrese apellido :')   
    telefono =int(input('Ingrese telefono :'))   
    correo = input('Ingrese correo :')   
    nuevaPersona = Persona(nombre, apellido, telefono, correo)
    listaPersonas.append(nuevaPersona)
     
     
def update():
    print('')
    read()
    seleccion = int(input('Ingrese el dato que desea actualiza: '))
    nombre = input('Ingrese nuevo nombre :')   
    listaPersonas[seleccion].setNombre(nombre)
    
    apellido = input('Ingrese nuevo apellido :')   
    listaPersonas[seleccion].setApellido(apellido)
    
    telefono =int(input('Ingrese nuevo telefono :'))   
    listaPersonas[seleccion].setTelefono(telefono)
    
    correo = input('Ingrese nuevo correo :')  
    listaPersonas[seleccion].setCorreo(correo)
    
    print('Se actualizo correctamente...')
     
    
    
def read():
    print('')
    print('Listado de Personas:')
    # for item in listaPersonas:
    #     print(item)
    
    for index in range(0,len(listaPersonas)):
         print(f'{index } : {listaPersonas[index]}')
         
         
def delete():
    read()
    seleccion = int(input('Ingrese el dato que desea eliminar: '))
    
    print(f"Seguro que desea eliminar a :{listaPersonas[seleccion].getNombre()} {listaPersonas[seleccion].getApellido()}")
    elimiar = input('y para elimiar/ n para ignorar: ')
    
    if(elimiar =='y'):
        listaPersonas.remove(listaPersonas[seleccion])
    else:
        return
     
    
    
#-----------------------------------------------------------

#------------------- Inicio el programa ---------------
listaPersonas = []
persona1 = Persona('Carlos','Montoya', 4421063, 'alfredomontoyacorreo2@gmail.com')
persona2 = Persona('Andrea','Montoya', 4421063, 'surleyab@gmail.com')
listaPersonas.append(persona1)
listaPersonas.append(persona2)
opcion = ''

while(opcion != 'x'):
    print('-- Agenda --')
    print('1 Para agregar persona')
    print('2 Para editar persona')
    print('3 Para listar persona')
    print('4 Para eliminar persona')
    print('x Para salir')
    print('')
    opcion = input('Ingrese la opcion deseada: ')
     
    
    print('')
    if(opcion == 'x'):
        print('Saliendo...')
    
    elif(opcion == 'a'):
        create()
    
    elif(opcion == 'e'):
        update()
    
    elif(opcion == 'l'):
        read()
        
    elif(opcion == 'd'):
        delete()   
    else:
        print('Opcion incorrecta')
    
     