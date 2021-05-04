

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
    
    def busqueda(self, buscado, criterio=None):
        pos = -1
        primero = 0
        ultimo = len(self.__elementos)
        while(primero <= ultimo and pos == -1):
            medio = (primero + ultimo) // 2
            if(self.__criterio(self.__elementos[medio], criterio) == buscado):
                pos = medio
            elif(self.__criterio(self.__elementos[medio], criterio) > buscado):
                ultimo = medio -1
            else:
                primero = medio + 1

        return pos
    
    def obtener_elemento(self, pos):
        return self.__elementos[pos]
    
    # def modificar_elemento(self, pos, nuevo_valor):
    #     self.__elementos[pos] = nuevo_valor

    def lista_vacia(self):
        return len(self.__elementos) == 0
    
    def tamanio(self):
        return len(self.__elementos)

    def barrido(self):
        for elemento in self.__elementos:
            print(elemento)


from random import randint
lista_num = Lista()
lista_personas = Lista()

datos = [
    {'name':'juan','edad': 34, 'provincia' : 'misiones', 'dni': 32},
    {'name':'juan','edad': 80, 'provincia' : 'misiones', 'dni': 20},
    {'name':'maria','edad': 56, 'provincia' : 'entre rios', 'dni': 28},
    {'name':'julieta','edad': 18, 'provincia' : 'catamarca', 'dni': 45},
    {'name':'carlos','edad': 40, 'provincia' : 'entre rios', 'dni': 38},

]
for persona in datos:
    lista_personas.insertar(persona, 'name')
lista_personas.barrido()

print(lista_personas.busqueda('juan', 'name'))

# for i in range(0, 10):
#     lista_num.insertar(randint(0, 100))

# print()
# numero = int(input('ingrese valor a buscar '))
# pos = lista_num.busqueda(numero)


# lista_num.modificar_elemento(pos, 43)
# print()
# lista_num.barrido()
# numero = int(input('ingrese valor a eliminar '))
# print(lista_num.eliminar(numero))
# print()
# lista_num.barrido()