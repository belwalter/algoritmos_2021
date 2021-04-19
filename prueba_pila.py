

from pila import Pila
from random import randint

pila_datos = Pila()
pila_aux = Pila()

for i in range(0, 100):
    num = randint(1, 100)
    print(num)
    pila_datos.apilar(num)

cantidad = 0
contar = int(input('ingrese el numero que desea contar '))

while(not pila_datos.pila_vacia()):
    x = pila_datos.desapilar()
    if(x == contar):
        cantidad += 1

print('cantidad de ocurrencias', cantidad)

    


