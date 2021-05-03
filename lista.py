

class Lista(object):
    """crea un objeto de tipo lista"""

    def __init__(self):
        self.__elementos= []

    def insertar(self, dato):#! tener en cuenta que la insercion es ordenada
        if(len(self.__elementos) == 0):
            self.__elementos.append(dato)
        elif(dato < self.__elementos[0]):
            self.__elementos.insert(0, dato)
        else:
            pos = 0
            while(pos < len(self.__elementos) and dato>=self.__elementos[pos]):
                pos +=1 
            self.__elementos.insert(pos, dato)
    
    def eliminar(self, dato):
        if(dato in self.__elementos):
            self.__elementos.remove(dato)
            return dato
        else:
            return None
    
    def busqueda(self, buscado):
        pass

    def lista_vacia(self):
        return len(self.__elementos) == 0
    
    def tamanio(self):
        return len(self.__elementos)

    def barrido(self):
        for elemento in self.__elementos:
            print(elemento)


from random import randint
lista_num = Lista()

for i in range(0, 50):
    lista_num.insertar(randint(0, 100))

lista_num.barrido()
print()
numero = int(input('ingrese valor a eliminar '))
print(lista_num.eliminar(numero))
print()
lista_num.barrido()