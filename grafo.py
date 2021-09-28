from lista import Lista


class Grafo(object):

    def __init__(self, dirigido=True):
        self.dirigido = dirigido
        self.inicio = Lista()

    def insertar_vertice(self, dato, otro=None): #! agregar otro
        self.inicio.insertar({'info': dato, 'visitado': False, 'aristas': Lista()}, 'info')


    def insertar_arista(self, peso, origen, destino):
        ver_origen = self.inicio.busqueda(origen, 'info')
        ver_destino = self.inicio.busqueda(destino, 'info')
        if(ver_origen != -1 and ver_destino != -1):
            self.inicio.obtener_elemento(ver_origen)['aristas'].insertar({'peso': peso, 'destino': destino}, 'destino')
            if(not self.dirigido): #! chequear relaicon nodo a si mismo
                self.inicio.obtener_elemento(ver_destino)['aristas'].insertar({'peso': peso, 'destino': origen}, 'destino')
        else:
            print('los vertices origen o destino no estan en el grafo....')


grafo = Grafo(dirigido=False)
grafo.insertar_vertice('A')
grafo.insertar_vertice('C')
grafo.insertar_vertice('B')
print(grafo.inicio.tamanio())

grafo.insertar_arista(12, 'A', 'C')
grafo.insertar_arista(1, 'A', 'B')
grafo.insertar_arista(1, 'A', 'F')
# grafo.insertar_arista(100, 'B', 'B')

grafo.inicio.obtener_elemento(0)['aristas'].barrido()
print()
grafo.inicio.obtener_elemento(1)['aristas'].barrido()

# grafo.inicio.barrido()


