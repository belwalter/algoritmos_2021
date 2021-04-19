

# n1 * n2 --> 2 * 5 --> 2 + 2 + 2 + 2 + 2 --> n1 * n2 = n1 + (n1, n2-1)

def producto(numero1, numero2):
    if(numero2 == 1):
        return numero1
    else:
        print(numero1, numero2)
        return numero1 + producto(numero1, numero2)


def sumatoria(numero): #! 3 
    if(numero == 1):
        return numero
    else:
        return 1/numero + sumatoria(numero-1)

# 1/3 + 1/2 + 1

# print(sumatoria(3))

# hola --> aloh



def invertir_cadena(cadena):#! 6
    if(len(cadena) == 0):
        return ""
    else:
        return cadena[-1] + invertir_cadena(cadena[0:-1])


# print(invertir_cadena("hola mundo desde python"))

#! ESTRUCTURAS DE DATOS SIMPLES VECTORES Y MATRICES 
# n = 3
# # vector = [[1] * n,[2] * n,[3] * n]
# vector = ["a", "b", "c", "d", "e"]

# for nombre in vector:
#     print(nombre)

# cortar vector SLICING


# print(vector[:-1])


def logaritmo(numero, base):
    if(numero / base < 1):
        return 0
    else:
        return 1 + logaritmo(numero/base , base)

# print(logaritmo(6, 2))


def invertir_numero(numero):
    """Invertir un número."""
    if(numero < 10):
        return numero
    else:
        return ((numero % 10) * 10 ** len(str(numero//10))) + invertir_numero(numero // 10)



# print(invertir_numero(791))

def sumar_digitos(numero):
    """Invertir un número."""
    if(numero < 10):
        return numero
    else:
        return (numero % 10) + sumar_digitos(numero // 10)
 
# print(sumar_digitos(791))

def raizcuadrada(n1, n2):
    if((n1 * n1) <= n2):
        return n1
    else:
        return raizcuadrada(n1-1, n2)


def raiz(n):
    if n == 0:
        return n
    else:
        return raizcuadrada(n, n)



# print(raiz(10))


datos = [100,3, 4, 10, 7, 5, 20, 11, 22, 81, 25, 30, 45]



def quicksort(vector, inicio, fin):
    primero = inicio
    ultimo = fin -1
    pivote = fin
    while(primero < ultimo):
        while(vector[primero]<vector[pivote] and primero <= ultimo):
            primero += 1
        while(vector[ultimo]>vector[pivote] and ultimo >= primero):
            ultimo -= 1
        
        if(primero < ultimo):
            vector[primero], vector[ultimo] = vector[ultimo], vector[primero]
    if(vector[pivote]<vector[primero]):
        vector[primero], vector[pivote] = vector[pivote], vector[primero]

    if(inicio < primero):
        quicksort(vector, inicio, primero -1)
    if(fin > primero):
        quicksort(vector, primero + 1, fin)

def busqueda_binaria(vector, buscado, inicio, fin):
    if(inicio<= fin):
        medio = (inicio + fin) // 2
        if(vector[medio] == buscado):
            return medio
        elif(vector[medio] < buscado):
            return busqueda_binaria(vector, buscado, medio+1, fin)
        else:
            return busqueda_binaria(vector, buscado, inicio, medio-1)
    else:
        return -1


# quicksort(datos,0, len(datos)-1)
# print(datos)
# pos = busqueda_binaria(datos, 100, 0, len(datos)-1)
# if(pos > -1):
#     print('esta')
# else:
#     print('no esta')


# laberinto = [ [0, 0, 1, 0, 0],
#               [1, 0, 0, 0, 1],
#               [1, 0, 1, 0, 0],
#               [0, 0, 1, 1, 1],
#               [0, 0, 0, 0, 0],
#             ]

#! int, float, string 

datos = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mochila = ['Pan', 'Capa', 'Sable de luz', 'otro']

def usar_fuerza(mochila, pos):
    if(pos< len(mochila)):
        if(mochila[pos] == 'Sable de luz'):
            return pos
        else:
            return usar_fuerza(mochila, pos+1)
    else:
        return -1

# print(usar_fuerza(mochila, 0))

def barriro(vector):
    if(len(vector)>0):
        print(vector[0])
        barriro(vector[1:])



def salida_laberinto(matriz, x, y, caminos=[]):
    """Salida del laberinto."""
    if(x >= 0 and x <= len(matriz)-1) and (y >= 0 and y <= len(matriz[0])-1):
        if(matriz[x][y] == 2):
            caminos.append([x, y])
            print("Saliste del laberinto")
            print(caminos)
            caminos.pop()
        elif(matriz[x][y] == 1):
            matriz[x][y] = 3
            caminos.append([x, y])
            # print("mover este")
            salida_laberinto(matriz, x, y+1, caminos)
            # print("mover oeste")
            salida_laberinto(matriz, x, y-1, caminos)
            # print("mover norte")
            salida_laberinto(matriz, x-1, y, caminos)
            # print("mover sur")
            salida_laberinto(matriz, x+1, y, caminos)
            caminos.pop()
            matriz[x][y] = 1


lab = [[1, 1, 1, 1, 1, 1, 1],
       [0, 0, 0, 0, 1, 0, 1],
       [1, 1, 1, 0, 1, 0, 1],
       [1, 0, 1, 1, 1, 1, 1],
       [1, 0, 0, 0, 0, 0, 0],
       [1, 1, 1, 1, 1, 1, 2]]
    
salida_laberinto(lab, 0, 0)




# barriro(datos)



# def prueba(num1, num2, cad, vector):
#     num1 = num2 * 2
#     print(num1)
#     cad = "mundo"
#     vector[0] = 100


# num1 = 2
# num2 = 5
# cadena = "hola"

# prueba(num1, num2, cadena, datos)

# print(num1, num2, cadena)
# print(datos)

# num1 = 1
# num2 = num1
# num2 = num2 + 3

# print(num1, num2)

# lista1 = {'a': True}
# lista2 = {'a': True}

# # print(lista1 == lista2)

# class Persona(object):

#     edad = None


# num1 = Persona()
# num1.edad = 10

# num2 = Persona()
# num2.edad = 10

# print(num1 == num2)