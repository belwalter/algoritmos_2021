
from lista import Lista

lista_entrenadores = Lista()


entrenadores = [
     {'name':'juan','torneos_ganados': 12, 'batallas_perdidas' : 5, 'batallas_ganadas': 32, 'pokemons': Lista()},
     {'name':'enzo','torneos_ganados': 2, 'batallas_perdidas' : 8, 'batallas_ganadas': 20, 'pokemons': Lista()},
     {'name':'maria','torneos_ganados': 4, 'batallas_perdidas' : 15, 'batallas_ganadas': 28, 'pokemons': Lista()},
]

pokemons = [{'name':'tyrantrum', 'nivel': 12 ,'tipo':'fuego', 'subtipo':'planta', 'entrenador': 'juan' },
            {'name':'wingull', 'nivel': 180 ,'tipo':'agua','subtipo':'volador', 'entrenador': 'juan'},
            {'name':'wolverine', 'nivel':3  ,'tipo':'fuego'  ,'subtipo':'terreno', 'entrenador': 'enzo' },
            {'name':'tyrantrum'  , 'nivel': 12 ,'tipo':'fuego'  ,'subtipo':'planta', 'entrenador': 'maria' },
            {'name':'wingull' , 'nivel': 18 ,'tipo':'agua'  ,'subtipo':'volador', 'entrenador': 'enzo' },
            {'name':'tyrantrum,'  , 'nivel': 12 ,'tipo':'fuego'  ,'subtipo':'planta', 'entrenador': 'maria' },
            {'name':'gigante' , 'nivel': 21 ,'tipo':'agua','subtipo':'volador', 'entrenador': 'juan' },
            {'name':'rayo' , 'nivel':3  ,'tipo':'fuego'  ,'subtipo':'terreno', 'entrenador': 'enzo' }
]


for entrenador in entrenadores:
    lista_entrenadores.insertar(entrenador, 'name')

for pokemon in pokemons:
    pos = lista_entrenadores.busqueda(pokemon['entrenador'], 'name')
    if(pos > -1):
        del pokemon['entrenador']
        lista_entrenadores.obtener_elemento(pos)['pokemons'].insertar(pokemon, 'name')


pos = lista_entrenadores.busqueda('enzo', 'name')

if(pos > -1):
    print(lista_entrenadores.obtener_elemento(pos)['pokemons'].tamanio())


maximo = 0
pos_maximo = -1

for i in range(lista_entrenadores.tamanio()):
    if(lista_entrenadores.obtener_elemento(i)['torneos_ganados'] > maximo):
        maximo = lista_entrenadores.obtener_elemento(i)['torneos_ganados'] 
        pos_maximo = i

nivel_max = 0
pos_nivel_max = -1
entrenador_max = lista_entrenadores.obtener_elemento(pos_maximo)
print(entrenador_max['name'])

for i in range(entrenador_max['pokemons'].tamanio()):
    if(entrenador_max['pokemons'].obtener_elemento(i)['nivel'] > nivel_max):
        nivel_max = entrenador_max['pokemons'].obtener_elemento(i)['nivel']
        pos_nivel_max = i

print(entrenador_max['pokemons'].obtener_elemento(pos_nivel_max)['name'])



print(entrenador_max['name'], entrenador_max['torneos_ganados'], entrenador_max['batallas_ganadas'], entrenador_max['batallas_perdidas'])
print('pokemons: ')
entrenador_max['pokemons'].barrido()
# lista_entrenadores.barrido()