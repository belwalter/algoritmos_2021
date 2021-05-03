

from pila import Pila
from random import randint

# pila_datos = Pila()
# # pila_aux = Pila()

# for i in range(0, 100):
#     num = randint(1, 100)
#     print(num)
#     pila_datos.apilar(num)

# cantidad = 0
# contar = int(input('ingrese el numero que desea contar '))

# while(not pila_datos.pila_vacia()):
#     x = pila_datos.desapilar()
#     if(x == contar):
#         cantidad += 1

# print('cantidad de ocurrencias', cantidad)

# pila_letras = Pila()
# pila_aux = Pila()
# pila_inversa = Pila()

# palabra = input('ingrese una palabra ')

# for letra in palabra:
#     pila_letras.apilar(letra)

# while(not pila_letras.pila_vacia()):
#     x = pila_letras.desapilar()
#     # print(x)
#     pila_aux.apilar(x)
#     pila_inversa.apilar(x)

# while(not pila_aux.pila_vacia()):
#     x = pila_aux.desapilar()
#     pila_letras.apilar(x)

# #print(pila_letras.tamanio(), pila_aux.tamanio(), pila_inversa.tamanio())


# while(not pila_letras.pila_vacia() and pila_letras.elemento_cima() == pila_inversa.elemento_cima()):
#     print('pila letras', pila_letras.desapilar())
#     print('pila inversa', pila_inversa.desapilar())


# if(pila_letras.pila_vacia()):
#     print('la palabra es palindromo')
# else:
#     print('no es un palindromo')


# pila_dioses = Pila()
# pila_aux = Pila()

# pila_dioses.apilar('Zeus')
# pila_dioses.apilar('Helios')
# pila_dioses.apilar('Poseidon')
# pila_dioses.apilar('Ares')
# pila_dioses.apilar('Hermes')

# posicion_insertar = 1

# if(pila_dioses.tamanio() >= posicion_insertar):
#     pos = 0
#     while(not pila_dioses.pila_vacia() and pos < posicion_insertar):
#         pos += 1
#         pila_aux.apilar(pila_dioses.desapilar())

#     pila_dioses.apilar('Atenea')
    
#     while(not pila_aux.pila_vacia()):
#         pila_dioses.apilar(pila_aux.desapilar())
    
#     while(not pila_dioses.pila_vacia()):
#         print(pila_dioses.desapilar())
# else:
#     print('la pila no tiene la cantidad de elementos necesarios')

# pila_datos = Pila()
# pila_aux = Pila()

# numeros = [0, 3, 1, 7, 2, 10]

# for i in range(0, 6):
#     numero = numeros[i]

#     if(pila_datos.pila_vacia()):
#         pila_datos.apilar(numero)
#     else:
#         if(numero >= pila_datos.elemento_cima()):
#             pila_datos.apilar(numero)
#         else:
#             while(not pila_datos.pila_vacia() and pila_datos.elemento_cima() > numero):
#                 pila_aux.apilar(pila_datos.desapilar())
            
#             pila_datos.apilar(numero)

#             while(not pila_aux.pila_vacia()):
#                 pila_datos.apilar(pila_aux.desapilar())

# while(not pila_datos.pila_vacia()):
#     print(pila_datos.desapilar())

class Traje(object):
    # modelo, pelicula, estado = '', '', ''

    def __init__(self, modelo, pelicula, estado):
        self.modelo = modelo
        self.pelicula = pelicula
        self.estado = estado

    def __str__(self):
        return self.modelo+' - '+self.pelicula+' - '+self.estado

# pila = Pila()
# pila_aux = Pila()

# traje = Traje('Mark III', 'Avengers I', 'Dañado')
# pila.apilar(traje)
# traje = Traje('Mark I', 'Iron Man I', 'Destruido')
# pila.apilar(traje)
# traje = Traje('Mark XLIV', 'Capitan America: Civil War', 'Dañado')
# pila.apilar(traje)
# traje = Traje('Mark III', 'Iron Man I', 'Impecable')
# pila.apilar(traje)
# traje = Traje('Mark XXV', 'Avengers II', 'Dañado')
# pila.apilar(traje)

# control_traje = False

# while(not pila.pila_vacia()):
#     x = pila.desapilar()
#     # punto a
#     if(x.modelo == 'Mark XLIV'):
#         print('el moelo Mark XLIV fue utilizado en', x.pelicula)
#     #punto b
#     if(x.estado == 'Dañado'):
#         print('el modelo', x.modelo, 'resulto dañado')
#     #punto c
#     if(x.estado == 'Destruido'):
#         print('el modelo', x.modelo, 'resulto destruido')
#     else:
#         pila_aux.apilar(x)
#     if(x.pelicula == 'Capitan America: Civil War' or x.pelicula == 'Spiderman'):
#         print(x.modelo, 'es utilizado en las peliculas indicadas')

# while(not pila_aux.pila_vacia()):
#     pila.apilar(pila_aux.desapilar())

# # if(not control_traje):
# #     traje = Traje('Mark LXXXV', 'Avengers II', 'Dañado')
# #     pila.apilar(traje)

# while(not pila.pila_vacia()):
#     print(pila.desapilar())


pila_vocales = Pila()
pila_consonantes = Pila()
pila_simbolos = Pila()

parrafo = """Dada una pila de objetos de una oficina de los que se dispone de su nombre y peso (por ejemplo monitor 1 kg, teclado 0.25 kg, silla 7 kg, etc.), ordenar dicha pila de acuerdo a su peso –del
objeto más liviano al más pesado–. Solo pueden utilizar pilas auxiliares como estructuras extras, no se pueden utilizar métodos de ordenamiento"""

vocales = ['a', 'e', 'i', 'o', 'u']


for caracter in parrafo:
    if(caracter.lower() in vocales):
        pila_vocales.apilar(caracter)
    elif(ord(caracter.lower())>97 and ord(caracter.lower())<=122):
        pila_consonantes.apilar(caracter)
    else:
        pila_simbolos.apilar(caracter)

#! punto a
print('cantidad de vocales', pila_vocales.tamanio())
print('cantidad de consonantes', pila_consonantes.tamanio())
print('cantidad de simbolos', pila_simbolos.tamanio())

#! punto e
print('cantidad de vocales y simbolos son iguales ?', pila_vocales.tamanio()==pila_simbolos.tamanio())

#! punto b y d
cantidad_numeros = 0
cantidad_blancos = 0
while(not pila_simbolos.pila_vacia()):
    letra = pila_simbolos.desapilar()
    if(letra ==' '):
        cantidad_blancos +=1
    elif(ord(letra)>=48 and ord(letra)<=57):
        cantidad_numeros += 1

print('cantidad de espacios en blanco', cantidad_blancos)
print('cantidad de numeros', cantidad_numeros)

#! punto f letra z
while(not pila_consonantes.pila_vacia()):
    letra = pila_consonantes.desapilar()
    if(letra.lower()=='z'):
        print('hay una z')
        # break
