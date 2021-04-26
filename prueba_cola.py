

from cola import Cola
from random import randint


cola_datos = Cola()
# cola_aux = Cola()

for i in range(0, 10):
    num = randint(0, 100)
    cola_datos.arribo(num)
    print(num)
print()
cantidad_elemento = 0
while(cantidad_elemento < cola_datos.tamanio()):
    dato = cola_datos.mover_final()
    print(dato)
    cantidad_elemento += 1
# while(not cola_datos.cola_vacia()):
#     dato = cola_datos.atencion()
#     cola_aux.arribo(dato)
#     print(dato)

# while(not cola_aux.cola_vacia()):
#     dato = cola_aux.atencion()
#     cola_datos.arribo(dato)

print('tamanio', cola_datos.tamanio())