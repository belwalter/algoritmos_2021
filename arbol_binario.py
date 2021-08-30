

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

    def busqueda(self, clave):
        pos = None
        if(self.info is not None):
            if(self.info == clave):
                pos = self
            elif(clave < self.info and self.izq is not None):
                pos = self.izq.busqueda(clave)
            elif(self.der is not None):
                pos = self.der.busqueda(clave)
        return pos

    def remplazar(self):
        """Determina el nodo que remplazará al que se elimina."""
        aux = None
        if(self.der is None):
            aux = self.info
            if(self.izq is not None):
                self.info = self.izq.info
                self.der = self.izq.der
                self.izq = self.izq.izq
            else:
                self.info = None
        else:
            aux = self.der.remplazar()
        return aux

    def eliminar_nodo(self, clave):
        """Elimina un elemento del árbol y lo devuelve si lo encuentra."""
        x = None
        if(self.info is not None):
            if(clave < self.info):
                if(self.izq is not None):
                    x = self.izq.eliminar_nodo(clave)
            elif(clave > self.info):
                if(self.der is not None):
                    x = self.der.eliminar_nodo(clave)
            else:
                x = self.info
                if(self.der is None and self.izq is None):
                    self.info = None
                elif(self.izq is None):
                    self.info = self.der.info
                    self.izq = self.der.izq
                    self.der = self.der.der
                elif(self.der is None):
                    self.info = self.izq.info
                    self.der = self.izq.der
                    self.izq = self.izq.izq
                else:
                    aux = self.izq.remplazar()
                    self.info = aux
                    # raiz.info, raiz.nrr = aux.info, aux.nrr
        return x
    
    def contar_ocurrencias(self, buscado):
        cantidad = 0
        if(self.info is not None):
            if(self.info == buscado):
                cantidad += 1
            if(self.izq is not None):
                cantidad += self.izq.contar_ocurrencias(buscado)
            if(self.der is not None):
                cantidad += self.der.contar_ocurrencias(buscado)
        return cantidad
    
    def contar_pares_impares(self):
        pares, impares = 0, 0
        if(self.info is not None):
            if(self.info % 2 == 0):
                pares += 1
            else:
                impares += 1
            if(self.izq is not None):
                par, impar = self.izq.contar_pares_impares()
                pares += par
                impares += impar
            if(self.der is not None):
                par, impar = self.der.contar_pares_impares()
                pares += par
                impares += impar
        return pares, impares


    #! BARRIDO POR NIVEL


# arbol = Arbol()
# arbol.insertar_nodo('F')
# arbol.insertar_nodo('B')
# arbol.insertar_nodo('E')
# arbol.insertar_nodo('C')
# arbol.insertar_nodo('K')
# arbol.insertar_nodo('R')
# arbol.insertar_nodo('H')
# arbol.insertar_nodo('J')
# arbol.insertar_nodo('A')

# # print(arbol.izq.info, arbol.izq.izq, arbol.izq.der)
# # print(arbol.arbol_vacio())
# # arbol.preorden()

# # x = arbol.eliminar_nodo('F')
# pos = arbol.busqueda('K')
# if pos:
#     print('elemento encontrado', pos.info)

# print()
# print('barrido')
# arbol.inorden()