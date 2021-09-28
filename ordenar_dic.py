
dic = {'zeus': 5, 'heracles': 4, 'otro': 2, 'nuevo': 2}

def ordenar(item):
    return item[1]


lista = list(dic.items())
lista.sort(key=ordenar, reverse=True)
print(lista[:3])

for elemento in lista:
    print(elemento)
