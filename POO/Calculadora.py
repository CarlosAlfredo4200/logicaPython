class Calculadora:
    
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
        
    def sumar(self):
       suma = self.numero1 + self.numero2
       return suma

    def restar(self):
        resta = self.numero1 - self.numero2
        return resta

    def multiplicar(self):
        multiplicacion = self.numero1 * self.numero2
        return multiplicacion
    
    def dividir(self):
        division = self.numero1 / self.numero2
        return division
    
    
  
 
     