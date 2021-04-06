

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

print(logaritmo(6, 2))


def invertir_numero(numero):
    """Invertir un número."""
    if(numero < 10):
        return numero
    else:
        return ((numero % 10) * 10 ** len(str(numero//10))) + invertir_numero(numero // 10)



print(invertir_numero(791))

def sumar_digitos(numero):
    """Invertir un número."""
    if(numero < 10):
        return numero
    else:
        return (numero % 10) + sumar_digitos(numero // 10)
 
print(sumar_digitos(791))

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



print(raiz(10))
