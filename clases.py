from math import pi as pi
import turtle

"""
Escribir una clase en python llamada circulo que contenga un radio, con un metodo que devuelva el area
y otro que devuelva el perimetro del circulo.
Si se instancia la clase con radio <=0 mostrar una excepcion indicando un error amigable al usuario e
impidiendo la instanciacion.
Si printeamos el objeto creado debe mostrarse una representacion amigable.
El objeto debe tener su atribut radio modificable, si se le interesa setear un valor <=0 mostrar un
error y no permitir modificacion.
Permitir la multiplicacion del circulo: Circulo * n debe devolver un nuevo objeto con el radio multiplicado por n.
No permitir la multiplicacion por numeros <=0
"""


class Circulo():
    radio = int(input())
    if radio>0:
        pass
    else:
        print("Los radios no pueden ser nulos o negativos\nIntentemos con valores mayores a cero")
        
    def area(self):
        return(pi * self.radio**2)
    
    def perimetro(self):
        return(2 * pi * self.radio)
        
    def crea_circulo(self):
        t_cir = turtle.Turtle()
        t_cir.circle(self.radio)
        
        
circulo1 = Circulo()
print(f"El valor del area es: {circulo1.area()}.")
print(f"El valor del perimetro es : {circulo1.perimetro()}.")
print(circulo1.crea_circulo())

