# 1. Construir un programa para ir de compras a un supermercado que permita la construcción del siguiente menú:

# Digitar 1 para recibir código, nombre y precio de un producto
# Digitar 2 para mostrar los productos
# Digitar 3 para buscar y editar producto por código
# Digitar 4 para buscar y eliminar producto por código 

 


class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        
           
    def __str__(self):
          return f"Código: {self.codigo} Nombre: {self.nombre} Precio: {self.precio}"
  
     

    def getNombre(self):
          return self.nombre
    
    def getCodigo(self):
          return self.codigo
    
    def getPrecio(self):
          return self.precio
      
    #--- Metodos para actualizar ---
  
    def setNombre(self, newNombre):
        self.nombre = newNombre

    def setCodigo(self, newCodigo):
        self.codigo = newCodigo
    
    def setPrecio(self, newPrecio):
        self.precio = newPrecio
    
     
      
      
def agregar():
    
    codigo = int(input('Ingrese el código del producto: '))
    nombre = input('Ingrese nombre del producto: ')
    precio =int( input('Ingrese el precio del producto: '))
     
    
    nuevoProducto = Producto(codigo, nombre, precio)
    listaProductos.append(nuevoProducto)

def listar():
    print('')
    print('Lista de productos')
    
    for index in range(0,len(listaProductos)):
         print(f'{index } : {listaProductos[index]}')
         
        

def editar():     
    print('')
    listar()
    seleccion = int(input('Ingrese el código que desea actualiza: '))
    
    codigo =int( input('Ingrese nuevo código :')) 
    listaProductos[seleccion].setCodigo(codigo)
    
    nombre = input('Ingrese nuevo nombre :')   
    listaProductos[seleccion].setNombre(nombre)
    
    precio =int(input('Ingrese nuevo precio :'))   
    listaProductos[seleccion].setPrecio(precio)
    
    print('Se actualizo correctamente...')
         
         
         
def eliminar():
    listar()
    seleccion = int(input('Ingrese el dato que desea eliminar: '))
    
    print(f"Seguro que desea eliminar a :{listaProductos[seleccion].getNombre()}")
    elimiar = input('y para elimiar/ n para ignorar: ')
    
    if(elimiar =='y'):
        listaProductos.remove(listaProductos[seleccion])
    else:
        return
     
 
    
listaProductos =[]
 
 
producto1 = Producto(414,'Papa',10000)
producto2 = Producto(415,'Cafe',12000)
producto3 = Producto(416,'Maiz',15000)

listaProductos.append(producto1)
listaProductos.append(producto2)
listaProductos.append(producto3)



opcion = -1
while(opcion != 0):
    
    print('')
    
    print('Digitar 1 para recibir código, nombre y precio de un producto')
    print('Digitar 2 para mostrar los productos')
    print('Digitar 3 para buscar y editar producto por código')
    print('Digitar 4 para buscar y eliminar producto por código')
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
        
    elif(opcion == 3):
        editar()
    
    elif(opcion == 4):
        eliminar()
    else:
        print('')
        print('Opcion incorrecta')