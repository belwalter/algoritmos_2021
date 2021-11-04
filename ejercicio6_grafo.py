from grafo import Grafo

dioses = Grafo(dirigido=False)

dioses.insertar_vertice('Urano')
dioses.insertar_vertice('Cronos')
dioses.insertar_vertice('Rea')
dioses.insertar_vertice('Zeus')
dioses.insertar_vertice('Hades')
dioses.insertar_vertice('Demeter')
dioses.insertar_vertice('Atenea')
dioses.insertar_vertice('Apollo')
dioses.insertar_vertice('Persefone')

dioses.insertar_arista(1, 'Urano', 'Cronos', data={'relacion': ['padre', 'hijo']})

dioses.insertar_arista(1, 'Cronos', 'Zeus', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1, 'Cronos', 'Hades', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1, 'Cronos', 'Demeter', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1, 'Cronos', 'Rea', data={'relacion': ['pareja']})
dioses.insertar_arista(1, 'Cronos', 'Rea', data={'relacion': ['hermano']})

dioses.insertar_arista(1, 'Zeus', 'Hades', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Zeus', 'Atenea', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1, 'Zeus', 'Apollo', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1, 'Zeus', 'Persefone', data={'relacion': ['padre', 'hijo']})

dioses.insertar_arista(1, 'Demeter', 'Persefone', data={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1, 'Apollo', 'Persefone', data={'relacion': ['hermano']})
# origen = dioses.buscar_vertice('Persefone')
print('apmlitud')
dioses.barrido_amplitud(0)
print('fin')


print(dioses.es_adyacente('Zeus', 'Urano'))

dioses.adyacentes('Zeus')

def ancestro(vertice_nombre):
    origen = dioses.buscar_vertice(vertice_nombre)
    if(origen != -1):
        dios = dioses.inicio.obtener_elemento(origen)
        for i in range(dios['aristas'].tamanio()):
            nombre_dios = dios['aristas'].obtener_elemento(i)['destino']
            dios_aux = dios['aristas'].obtener_elemento(i)['data']
            if(len(dios_aux['relacion']) > 1):
                if(dios_aux['relacion'][1] == 'padre' or dios_aux['relacion'][1] == 'madre'):
                    print(nombre_dios, dios_aux['relacion'])
                    ancestro(nombre_dios)

def directo(ver_origen, ver_destino):
    print('tiene relacion directa:')
    pos = dioses.buscar_arista(ver_origen, ver_destino)
    print(pos)
    if(pos != 1):
        pos_aux = dioses.buscar_vertice('Zeus')
        print(dioses.inicio.obtener_elemento(pos_aux)['aristas'].obtener_elemento(pos))


directo('Zeus', 'Apollo')
# ancestro('Persefone')

# for i in range(dioses.inicio.tamanio()):
#     dios = dioses.inicio.obtener_elemento(i)
#     print('aristas', dios['info'])
#     for j in range(dios['aristas'].tamanio()):
#         print(dios['aristas'].obtener_elemento(j))

#     print()

# origen = dioses.buscar_vertice('Cronos')
# dios = dioses.inicio.obtener_elemento(origen)
# print('aristas', dios['info'])
# for j in range(dios['aristas'].tamanio()):
#     arista = dios['aristas'].obtener_elemento(j)
#     if(len(arista['data']['relacion']) == 2):
#         if(arista['data']['relacion'][1] == 'hijo'):
#             print(arista)
# print()
# origen = dioses.buscar_vertice('Cronos')
# dios = dioses.inicio.obtener_elemento(origen)
# print('aristas', dios['info'])
# for j in range(dios['aristas'].tamanio()):
#     arista = dios['aristas'].obtener_elemento(j)
#     if(len(arista['data']['relacion']) == 2):
#         if(arista['data']['relacion'][1] == 'padre'):
#             print(arista)

# print()
# origen = dioses.buscar_vertice('Cronos')
# dios = dioses.inicio.obtener_elemento(origen)
# print('aristas', dios['info'])
# for j in range(dios['aristas'].tamanio()):
#     arista = dios['aristas'].obtener_elemento(j)
#     if(arista['data']['relacion'][0] == 'hermano'):
#         print(arista)

# print()
# origen = dioses.buscar_vertice('Cronos')
# dios = dioses.inicio.obtener_elemento(origen)
# print('aristas', dios['info'])
# for j in range(dios['aristas'].tamanio()):
#     arista = dios['aristas'].obtener_elemento(j)
#     if(arista['destino'] == 'Zeus'):
#         print(arista)


# vertice_origen = dioses.buscar_vertice('Urano')
# vertice_destino = dioses.buscar_vertice('Atenea')

# camino = dioses.dijkstra(vertice_origen, vertice_destino)

# destino = 'Atenea'
# costo = None
# while(not camino.pila_vacia()):
#     dato = camino.desapilar()
#     if(dato[1][0] == destino):
#         if(costo is None):
#             costo = dato[0]
#         print(dato[1][0])
#         destino = dato[1][1]
# print('el costo total del camino es:', costo)
