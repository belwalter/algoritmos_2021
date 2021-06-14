
from lista import Lista

jedis = Lista()
file = open('jedis.txt')

lineas = file.readlines()
lineas.pop(0)
for linea in lineas:
    jedi = linea.split(';')
    # print(jedi)
    jedi_data = {}
    jedi_data['name'] = jedi[0].title()
    jedi_data['rank'] = jedi[1]
    jedi_data['species'] = jedi[2]
    jedi_data['master'] = jedi[3].split('/')
    jedi_data['lightsaber_color'] = jedi[4].split('/')
    jedi_data['homeworld'] = jedi[5]
    jedi_data['birth_year'] = jedi[6]
    jedi_data['height'] = float(jedi[7].split('\n')[0])
    if(len(jedi) > 8):
        jedi_data['to_darkside'] = jedi[8]
        jedi_data['come_lightside'] = jedi[9]
    jedis.insertar(jedi_data, 'name')


file.close()

# jedis.ordenar('species')
pos = jedis.busqueda('Luke Skywalker', 'name')

if(pos > -1):
    jedi = jedis.obtener_elemento(pos)['name'] = "Nuevo"
    jedis.ordenar('name')
    # jedis.modificar_elemento(pos, jedi, 'name')


jedis.barrido_jedi()

# jedi_aux = jedis.obtener_elemento(3)
# jedi_aux['name'] = 'Yahsoka Tano'

# jedis.modificar_elemento(3, jedi_aux, 'name')
# print('busqueda', jedis.busqueda('Yahsoka Tano', 'name'))
# print(jedis.obtener_elemento(3))
# jedis.barrido_jedi()
# print(jedis.busqueda('Kit Fisto', 'name'))

# jedis.barrido_green()
# jedis.ordenar('name')
# print()
# jedis.barrido_jedi()
# print()
# jedis.ordenar('name')
