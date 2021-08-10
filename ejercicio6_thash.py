
from random import randint, choice
from lista import Lista

tabla_legion = [None] * 10
tabla_numero = [None] * 200

lista_legion = ['FL', 'TF', 'TK', 'CT', 'FN', 'FO']


def hash_legion(clave, tamanio_tabla):
    h = 0
    for caracter in clave:
        h = h * 33 + ord(caracter)
    return h % tamanio_tabla

def hash_numero(clave, tamanio_tabla):
    clave = clave % 1000
    return clave % tamanio_tabla


for i in range(2000):
    legion = choice(lista_legion)
    numero = randint(1000, 9999)
    stormtrooper = {'legion': legion, 'codigo': numero}
    pos_legion = hash_legion(legion, len(tabla_legion))
    pos_numero = hash_numero(numero, len(tabla_numero))
    if(tabla_legion[pos_legion] is None):
        tabla_legion[pos_legion] = Lista()
    tabla_legion[pos_legion].insertar(stormtrooper, 'codigo')
    if(tabla_numero[pos_numero] is None):
        tabla_numero[pos_numero] = Lista()
    tabla_numero[pos_numero].insertar(stormtrooper, 'legion')


stormtrooper = {'legion': 'FN', 'codigo': 2187}
pos_legion = hash_legion('FN', len(tabla_legion))
tabla_legion[pos_legion].insertar(stormtrooper, 'codigo')

stormtrooper = {'legion': 'FN', 'codigo': 2781}
pos_numero = hash_numero(2781, len(tabla_numero))
tabla_numero[pos_numero].insertar(stormtrooper, 'legion')

pos_legion = hash_legion(stormtrooper['legion'], len(tabla_legion))
if(tabla_legion[pos_legion]):
    pos = tabla_legion[pos_legion].busqueda(2187, 'codigo')
    if(pos > -1):
        print(tabla_legion[pos_legion].obtener_elemento(pos), pos)
        tabla_legion[pos_legion].eliminar(2187, 'codigo')

print()
pos_numero = hash_numero(1781, len(tabla_numero))
tabla_numero[pos_numero].barrido_stormtrooper(781)
print()
pos_numero = hash_numero(1537, len(tabla_numero))
tabla_numero[pos_numero].barrido_stormtrooper(537)

# for index, cant_colision in enumerate(tabla_numero):
#     print(index, cant_colision)
# for index, stormtrooper in enumerate(tabla_numero):
#     if(stormtrooper):
#         print(index, stormtrooper.tamanio())
#     else:
#         print(index, 0)
