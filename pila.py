
class Pila(object):
    
    def __init__(self):
        self.__elementos = []

    def apilar(self, dato):
        self.__elementos.append(dato)





pila = Pila()
pila.apilar(5)
pila.apilar(7)
pila.apilar(9)
pila.apilar(3)



print(pila.__elementos)
