

#! 5! = 5 * 4 * 3 * 2 * 1 = 120
#! 5! = 5 * 4! 

def factorail_I(numero):
    factorial = 1
    for i in range(2,numero+1):
        factorial = factorial * i
    return factorial


def factorial_R(numero):
    if(numero == 1 or numero == 0):
        return 1
    else:
        return numero * factorial_R(numero-1)


def fibonacci_I(numero):
    fib_1 = 0
    fib_2 = 1
    fibonacci = 0
    for i in range(2, numero+1):
        print("iterativo")
        fibonacci = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 = fibonacci
    return fibonacci



#! fib(n) = fib(n-1) + fib(n-2)

def fibonacci_R(numero):
    if(numero == 0 or numero == 1):
        return numero
    else:
        print("recursivo")
        return fibonacci_R(numero-1) + fibonacci_R(numero-2)


# print(fibonacci_I(10))
# print(fibonacci_R(10))




# print(factorail_I(30))
# a =input()
# print(factorial_R(30))




#! agregar codigo para prueba git


vector = ["a", "b", "c"]

for i in vector:
    print(i)

for i in range(0, len(vector)):
    print(i, vector[i])



#! XI  IX