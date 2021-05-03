

from cola import Cola
from random import randint


cola_datos = Cola()
# cola_aux = Cola()

# for i in range(0, 10):
#     num = randint(0, 100)
#     cola_datos.arribo(num)
#     print(num)
# print()
# cantidad_elemento = 0
# while(cantidad_elemento < cola_datos.tamanio()):
#     dato = cola_datos.mover_final()
#     print(dato)
#     cantidad_elemento += 1
# while(not cola_datos.cola_vacia()):
#     dato = cola_datos.atencion()
#     cola_aux.arribo(dato)
#     print(dato)

# while(not cola_aux.cola_vacia()):
#     dato = cola_aux.atencion()
#     cola_datos.arribo(dato)

# print('tamanio', cola_datos.tamanio())

# cola_letras = Cola()
# palabra = input('ingrese una palabra ')

# for letra in palabra:
#     cola_letras.arribo(letra.lower())

# vocales = ['a', 'e', 'i', 'o', 'u']
# i, cantidad_elemento = 0, cola_letras.tamanio()

# while(i < cantidad_elemento):
#     dato = cola_letras.atencion()
#     if(not dato in vocales):
#         cola_letras.arribo(dato)
#     i += 1

# cantidad_elemento = 0
# while(cantidad_elemento < cola_letras.tamanio()):
#     dato = cola_letras.mover_final()
#     print(dato)
#     cantidad_elemento += 1

# from pila import Pila
# datos = Cola()
# datos_aux = Pila()

# for i in range(0, 10):
#     num = randint(0, 100)
#     datos.arribo(num)
#     print(num)

# print()

# while(not datos.cola_vacia()):
#     dato = datos.atencion()
#     datos_aux.apilar(dato)

# while(not datos_aux.pila_vacia()):
#     datos.arribo(datos_aux.desapilar())


# cantidad_elemento = 0
# while(cantidad_elemento < datos.tamanio()):
#     dato = datos.mover_final()
#     print(dato)
#     cantidad_elemento += 1


def es_primo(numero):
    cantidad = 0
    for i in range(1, numero+1):
        if(numero % i == 0):
            cantidad += 1
    return cantidad == 2

# cola_numeros = Cola()
# from random import randint

# for i in range(0, 20):
#     cola_numeros.arribo(randint(2, 100))

# cantidad = cola_numeros.tamanio()
# i = 0
# while(i < cantidad):
#     numero = cola_numeros.atencion()
#     if(es_primo(numero)):
#         cola_numeros.arribo(numero)
#     else:
#         print(numero)
#     i += 1
# print()
# while(not cola_numeros.cola_vacia()):
#     print(cola_numeros.atencion())


cola_uno = Cola()
cola_dos = Cola()
cola_aux = Cola()
from random import randint

for i in range(0, 20):
    cola_uno.arribo(randint(2, 100))
    cola_dos.arribo(randint(2, 100))

cantidad = 0 

while(not cola_uno.cola_vacia()):
    numero1 = cola_uno.atencion()
    while(not cola_dos.cola_vacia()):
        numero2 = cola_dos.atencion()
        if(numero1 == numero2):
            cantidad += 1
        cola_aux.arribo(numero2)
    while(not cola_aux.cola_vacia()):
        cola_dos.arribo(cola_aux.atencion())
    

print(cantidad)
