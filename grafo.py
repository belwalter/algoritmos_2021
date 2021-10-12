from lista import Lista


class Grafo(object):

    def __init__(self, dirigido=True):
        self.dirigido = dirigido
        self.inicio = Lista()

    def insertar_vertice(self, dato, criterio='info', otro=None):  # ! agregar otro
        self.inicio.insertar({'info': dato, 'visitado': False, 'aristas': Lista()}, criterio)


    def insertar_arista(self, peso, origen, destino, criterio='destino', otro=None):  # ! agregar otro
        ver_origen = self.inicio.busqueda(origen, 'info')
        ver_destino = self.inicio.busqueda(destino, 'info')
        if(ver_origen != -1 and ver_destino != -1):
            self.inicio.obtener_elemento(ver_origen)['aristas'].insertar({'peso': peso, 'destino': destino}, criterio)
            if(not self.dirigido and origen != destino):
                self.inicio.obtener_elemento(ver_destino)['aristas'].insertar({'peso': peso, 'destino': origen}, criterio)
        else:
            print('los vertices origen o destino no estan en el grafo....', origen, destino)

    def grafo_vacio(self):
        return self.inicio.lista_vacia()

    def tamanio(self):
        return self.inicio.tamanio()
    
    def buscar_vertice(self, clave, criterio='info'):
        return self.inicio.busqueda(clave, criterio=criterio)

    def buscar_arista(self, origen, destino, criterio='destino'):
        ver_origen = self.inicio.busqueda(origen, 'info')
        if(ver_origen != -1):
            return self.inicio.obtener_elemento(ver_origen)['aristas'].busqueda(destino, criterio)
        else:
            return ver_origen

    def barrido_vertices(self):
        self.inicio.barrido()

    def es_adyacente(self, origen, destino):
        ver_origen = self.inicio.busqueda(origen, 'info')
        if(ver_origen != -1):
            destino = self.buscar_arista(origen, destino)
            if(destino != -1):
                return True
            else:
                return False
        else:
            return False

    def adyacentes(self, origen):
        ver_origen = self.inicio.busqueda(origen, 'info')
        if(ver_origen != -1):
            self.inicio.obtener_elemento(ver_origen)['aristas'].barrido()

    def eliminar_vertice(self, clave):
        aux = self.inicio.eliminar(clave, criterio='info')
        for posicion in range(self.tamanio()):
            origen = self.inicio.obtener_elemento(posicion)['info']
            self.eliminar_arista(origen, clave)
        return aux


    def eliminar_arista(self, origen, destino):
        ver_origen = self.inicio.busqueda(origen, 'info')
        if(ver_origen != -1):
            self.inicio.obtener_elemento(ver_origen)['aristas'].eliminar(destino, 'destino')
            if(not self.dirigido):
                ver_destino = self.inicio.busqueda(destino, 'info')
                if(ver_destino != -1):
                    self.inicio.obtener_elemento(ver_destino)['aristas'].eliminar(origen, 'destino')

    def barrido_profundidad(self, ver_origen):
        """Barrido en profundidad del grafo."""
        while(ver_origen < self.inicio.tamanio()):
            vertice = grafo.inicio.obtener_elemento(ver_origen)
            if(not vertice['visitado']):
                vertice['visitado'] = True
                print(vertice['info'])
                aristas = 0
                while(aristas < vertice['aristas'].tamanio()):
                    arista = vertice['aristas'].obtener_elemento(aristas)
                    pos_vertice = self.buscar_vertice(arista['destino'])
                    nuevo_vertice = grafo.inicio.obtener_elemento(pos_vertice)
                    if(not nuevo_vertice['visitado']):
                        self.barrido_profundidad(pos_vertice)
                    aristas += 1
            ver_origen += 1


# def barrido_amplitud(grafo, vertice):
#     """Barrido en amplitud del grafo."""
#     cola = Cola()
#     while(vertice is not None):
#         if(not vertice.visitado):
#             vertice.visitado = True
#             arribo(cola, vertice)
#             while(not cola_vacia(cola)):
#                 nodo = atencion(cola)
#                 print(nodo.info)
#                 adyacentes = nodo.adyacentes.inicio
#                 while(adyacentes is not None):
#                     adyacente = buscar_vertice(grafo, adyacentes.destino)
#                     if(not adyacente.visitado):
#                         adyacente.visitado = True
#                         arribo(cola, adyacente)
#                     adyacentes = adyacentes.sig
#         vertice = vertice.sig

grafo = Grafo()
print(grafo.grafo_vacio())
grafo.insertar_vertice('A')
grafo.insertar_vertice('C')
grafo.insertar_vertice('B')
grafo.insertar_vertice('F')

grafo.insertar_arista(12, 'A', 'A')
grafo.insertar_arista(1, 'A', 'B')
grafo.insertar_arista(3, 'C', 'B')
grafo.insertar_arista(1, 'A', 'F')
grafo.insertar_arista(1, 'F', 'B')
vertice_origen = grafo.buscar_vertice('A')
grafo.barrido_profundidad(vertice_origen)
# grafo.insertar_arista(100, 'B', 'B')

# grafo.inicio.obtener_elemento(0)['aristas'].barrido()
# print()
# grafo.inicio.obtener_elemento(1)['aristas'].barrido()

# grafo.barrido_vertices()

# print(grafo.es_adyacente('A', 'F'))
# print(grafo.es_adyacente('A', 'C'))
# # print(grafo.eliminar_vertice('B'))
# print()
# grafo.barrido_vertices()
# print()
# grafo.eliminar_arista('A', 'B')
# grafo.adyacentes('A')
# print()
# grafo.adyacentes('F')
# print()
# grafo.adyacentes('B')

# print(grafo.buscar_vertice('F'))
# print(grafo.buscar_vertice('B'))

# print(grafo.buscar_arista('B','A'))
# print(grafo.buscar_arista('A','A'))
