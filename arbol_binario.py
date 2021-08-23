


class Arbol(object):

    def __init__(self, info=None):
        self.info = info
        self.der = None
        self.izq = None

    def arbol_vacio(self):
        return self.info is None

    def insertar_nodo(self, dato):
        if(self.info is None):
            self.info = dato
        elif(dato < self.info):
            if(self.izq is None):
                self.izq = Arbol(dato)
            else:
                self.izq.insertar_nodo(dato)
        else:
            if(self.der is None):
                self.der = Arbol(dato)
            else:
                self.der.insertar_nodo(dato)

    def inorden(self):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.inorden()
            print(self.info)
            if(self.der is not None):
                self.der.inorden()

    def postorden(self):
        if(self.info is not None):
            if(self.der is not None):
                self.der.postorden()
            print(self.info)
            if(self.izq is not None):
                self.izq.postorden()

    def preorden(self):
        if(self.info is not None):
            print(self.info)
            if(self.izq is not None):
                self.izq.preorden()
            if(self.der is not None):
                self.der.preorden()


arbol = Arbol()
arbol.insertar_nodo(7)
arbol.insertar_nodo(10)
arbol.insertar_nodo(1)
arbol.insertar_nodo(15)
arbol.insertar_nodo(5)
# print(arbol.izq.info, arbol.izq.izq, arbol.izq.der)
# print(arbol.arbol_vacio())
arbol.preorden()