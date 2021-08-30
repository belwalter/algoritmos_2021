

from arbol_binario import Arbol
from random import randint

arbol = Arbol()

for i in range(10):
    numero = randint(1000, 9999)
    arbol.insertar_nodo(numero)

print('inorden')
arbol.inorden()
print()

# pos = arbol.busqueda(int(input('ingrese el numero a buscar ')))
# if(pos is not None):
#     print('el valor esta', pos.info)
# else:
#     print('el valor no esta')

arbol.eliminar_nodo(int(input('ingrese el numero a buscar ')))

print('inorden')
arbol.inorden()
print()
# print('postorden')
# arbol.postorden()
# print()
# print('preorden')
# arbol.preorden()
# print()