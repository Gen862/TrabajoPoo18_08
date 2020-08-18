'''Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea
saber cuanto deberá pagar finalmente por su compra.
Inicio
Leer tc
d = tc * 0.15
tp = tc - d
Imprimir tp
Fin'''
print("Bienvenido, por tu compra obtendras un descuento del 15%")
class Shop():
    def __init__(self):
        self.ope= tc=int(input("Porfavor digita el valor de tu compra "))
        self.ope= d = tc * 0.15
        self.ope= tp = tc - d
bag = Shop()
print("\n El total a pagar es de: ", bag.ope)


