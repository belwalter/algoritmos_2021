

from arbol_binario import Arbol
from random import randint

arbol = Arbol()

for i in range(20):
    numero = randint(1, 10)
    arbol.insertar_nodo(numero)

print('inorden')
arbol.inorden()
print()

# print('cantidad de ocurrencias', arbol.contar_ocurrencias(int(input('ingrese el valor '))))

print('cantidad de pares impares', arbol.contar_pares_impares())

# pos = arbol.busqueda(int(input('ingrese el numero a buscar ')))
# if(pos is not None):
#     print('el valor esta', pos.info)
# else:
#     print('el valor no esta')

# arbol.eliminar_nodo(int(input('ingrese el numero a buscar ')))


# print('postorden')
# arbol.postorden()
# print()
# print('preorden')
# arbol.preorden()
# print()