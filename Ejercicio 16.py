from pila import Pila


pila_episodioV = Pila()
pila_episodioVII = Pila() 
pila_interseccion = Pila()
pila_aux = Pila()
# pila_aux1 = Pila()
# pila_aux2 = Pila()

personajes_V = ['Luke','Obi','Yoda','Rey','Kylo Ren']
personajes_VII = ['Luke','Obi','Darth Vader','Yoda']

for i in range(len(personajes_V)):
    personaje_V = personajes_V[i]
    pila_episodioV.apilar(personaje_V)
for j in range(len(personajes_VII)):
    personaje_VII = personajes_VII[j]
    pila_episodioVII.apilar(personaje_VII)
#        if (personaje_V in personajes_VII):
 #           pila_interseccion.apilar(personaje_V)



# for i in range(len(personajes_V)):
#     personaje_V = personajes_V[i]
#     pila_episodioV.apilar(personaje_V) 

# for j in range (len(personajes_VII)):
#     personaje_VII = personajes_VII[j]
#     pila_episodioVII.apilar(personaje_VII) 

while (not pila_episodioV.pila_vacia()):
    aux1 = pila_episodioV.desapilar()
    while(not pila_episodioVII.pila_vacia()):
        aux2 = pila_episodioVII.desapilar()
        if (aux1 == aux2):
             pila_interseccion.apilar(aux1)
        pila_aux.apilar(aux2)
    while (not pila_aux.pila_vacia()):
        pila_episodioVII.apilar(pila_aux.desapilar())

while (not pila_interseccion.pila_vacia()):
    print('El personaje que se repite es: ',pila_interseccion.desapilar())



