

class Lista(object):
    """crea un objeto de tipo lista"""

    def __init__(self):
        self.__elementos= []
    
    def __criterio(self, dato, criterio):
        if(criterio == None):
            return dato
        else:
            return dato[criterio]

    def insertar(self, dato, criterio=None):#! tener en cuenta que la insercion es ordenada
        if(len(self.__elementos) == 0):
            self.__elementos.append(dato)
        elif(self.__criterio(dato, criterio) < self.__criterio(self.__elementos[0], criterio)):
            self.__elementos.insert(0, dato)
        else:
            pos = 0
            while(pos < len(self.__elementos) and self.__criterio(dato, criterio)>=self.__criterio(self.__elementos[pos], criterio)):
                pos +=1 
            self.__elementos.insert(pos, dato)
    
    def eliminar(self, dato):
        if(dato in self.__elementos):
            self.__elementos.remove(dato)
            return dato
        else:
            return None
    
    def modificar_elemento(self, pos, nuevo_valor):
        self.__elementos.pop(pos)
        self.insertar(nuevo_valor)
    
    def busqueda(self, buscado, criterio=None, clave=None, criterio_clave=None):
        pos = -1
        primero = 0
        ultimo = len(self.__elementos) -1
        while(primero <= ultimo and pos == -1):
            medio = (primero + ultimo) // 2
            if(self.__criterio(self.__elementos[medio], criterio) == buscado):
                pos = medio
            elif(self.__criterio(self.__elementos[medio], criterio) > buscado):
                ultimo = medio -1
            else:
                primero = medio + 1

        if(pos != -1 and clave is not None and self.__elementos[pos][criterio_clave] != clave):
            while(self.__criterio(self.__elementos[pos], criterio) == self.__criterio(self.__elementos[pos-1], criterio)):
                pos -= 1
            
            while(self.__elementos[pos][criterio_clave] != clave and 
                self.__criterio(self.__elementos[pos], criterio) == self.__criterio(self.__elementos[pos+1], criterio)):
                pos += 1
            
            if(self.__elementos[pos][criterio_clave] != clave):
                pos = -1

        return pos

        # [1, 2, 3, 4, 4, 4, 5, 6,7]
    
    def obtener_elemento(self, pos):
        if(pos >= 0 ):
            return self.__elementos[pos]
        else:
            return None

    def lista_vacia(self):
        return len(self.__elementos) == 0
    
    def tamanio(self):
        return len(self.__elementos)

    def barrido(self):
        for elemento in self.__elementos:
            print(elemento)
        
    def barrido_eliminando(self, datos_eliminar):

        for elemento in self.__elementos:
            if(elemento in datos_eliminar):
                self.__elementos.remove(elemento)
    
    def ordenar(self, criterio):
        pass


from random import randint
lista_vocales = Lista()
lista_num = Lista()
lista_par = Lista()
lista_impar = Lista()
lista_personas = Lista()
lista_uno = Lista()
lista_dos = Lista()

for i in range(5):
    lista_uno.insertar(i)
    lista_dos.insertar(randint(1,10))

print('lista uno')
lista_uno.barrido()
print()
print('lista dos')
lista_dos.barrido()
print()

for i in range(lista_dos.tamanio()):
    num = lista_dos.obtener_elemento(i)
    if(lista_uno.busqueda(num) == -1):
        lista_uno.insertar(num)

lista_uno.barrido()


# for i in range(20):
#     lista_num.insertar(randint(1,999))

# # lista_num.barrido()
# # while(not lista_num.lista_vacia()):
# #     print(lista_num.eliminar(lista_num.obtener_elemento(0)))

# for i in range(lista_num.tamanio()):
#     num = lista_num.obtener_elemento(i)
#     if(num % 2 == 0):
#         lista_par.insertar(num)
#     else:
#         lista_impar.insertar(num)

# print('lista par')
# lista_par.barrido()
# print()
# print('lista impar')
# lista_impar.barrido()



# for i in range(50):
#     vocal = chr(randint(65, 90))
#     lista_vocales.insertar(vocal)

# lista_vocales.barrido()

# vocales = ['A', 'E', 'I', 'O', 'U']

# for vocal in vocales:
#     aux = lista_vocales.eliminar(vocal)
#     while(aux is not None):
#         aux = lista_vocales.eliminar(vocal)

# # lista_vocales.barrido_eliminando(vocales)
# print()
# lista_vocales.barrido()

# datos = [
#     {'name':'juan','edad': 34, 'provincia' : 'chaco', 'dni': 32},
#     {'name':'juan','edad': 80, 'provincia' : 'misiones', 'dni': 20},
#     {'name':'maria','edad': 18, 'provincia' : 'entre rios', 'dni': 28},
#     {'name':'julieta','edad': 18, 'provincia' : 'catamarca', 'dni': 45},
#     {'name':'carlos','edad': 40, 'provincia' : 'entre rios', 'dni': 38},

# ]

# for i in range(10):
#     persona = {}
#     persona['name'] = input('ingrese nombre ')
#     persona['edad'] = int(input('ingrese edad '))
#     # faltan campos
#     lista_personas.insertar(persona, 'edad')

# for persona in datos:
#     lista_personas.insertar(persona, 'edad')

# lista_personas.barrido()

# print()
# pos = lista_personas.busqueda(18, 'edad', 'catamarca', 'provincia')
# print(lista_personas.obtener_elemento(pos))

# for i in range(0, 10):
#     lista_num.insertar(randint(0, 100))

# lista_num.barrido()
# print()
# numero = int(input('ingrese valor a buscar '))
# print(lista_num.busqueda(numero))


# lista_num.modificar_elemento(pos, 43)
# print()
# numero = int(input('ingrese valor a eliminar '))
# print(lista_num.eliminar(numero))
# print()
# lista_num.barrido()