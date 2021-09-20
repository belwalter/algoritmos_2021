

class Heap(object):

    def __init__(self):
        self.elementos = []
        self.tamanio = 0


    def vacio(self):
        return self.tamanio == 0


    def agregar(self, datos):
        self.elementos.append(datos)
        self.flotar(len(self.elementos)-1)
        self.tamanio += 1
    
    def flotar(self, indice):
        padre = (indice-1) // 2
        while(indice > 0 and self.elementos[indice] > self.elementos[padre]):
            self.elementos[indice], self.elementos[padre] = self.elementos[padre], self.elementos[indice]
            indice = padre
            padre = (indice-1) // 2
    
    def quitar(self):
        self.elementos[0], self.elementos[self.tamanio-1] = self.elementos[self.tamanio-1], self.elementos[0]
        self.tamanio -= 1
        self.hundir()

    def hundir(self, indice=0):
        hijo_izq = indice * 2 + 1
        control = True
        while(control and hijo_izq < self.tamanio):
            hijo_der = hijo_izq + 1
            aux = hijo_izq
            if(hijo_der < self.tamanio):
                if(self.elementos[hijo_der] > self.elementos[hijo_izq]):
                    aux = hijo_der
            
            if(self.elementos[indice] < self.elementos[aux]):
                self.elementos[indice], self.elementos[aux] = self.elementos[aux], self.elementos[indice]
                indice = aux
                hijo_izq = indice * 2 + 1
            else:
                control = False

    def heap_sort(self):
        for i in range(self.tamanio):
            self.quitar()

h = Heap()

from random import randint
for i in range(20):
    h.agregar(randint(0, 100))

print(h.elementos)

h.heap_sort()

print(h.elementos)