
from lista import Lista

jedis = Lista()
file = open('jedis.txt')

lineas = file.readlines()
lineas.pop(0)
for linea in lineas:
    jedi = linea.split(';')
    # print(jedi)
    jedi[7] = float(jedi[7].split('\n')[0])
    # print(jedi)
    jedi_data = {}
    jedi_data['name'] = jedi[0].title()
    jedi_data['rank'] = jedi[1]
    jedi_data['species'] = jedi[2]
    jedi_data['master'] = jedi[3].split('/')
    jedi_data['lightsaber_color'] = jedi[4].split('/')
    jedi_data['homeworld'] = jedi[5]
    jedi_data['birth_year'] = jedi[6]
    jedi_data['height'] = jedi[7]
    if(len(jedi) > 8):
        jedi_data['to_darkside'] = jedi[8]
        jedi_data['come_lightside'] = jedi[9]
    jedis.insertar(jedi_data, 'species')


file.close()


jedis.barrido_jedi()

# print(jedis.busqueda('Kit Fisto', 'name'))

# jedis.barrido_green()
jedis.ordenar('name')
print()
jedis.barrido_jedi()
print()
jedis.ordenar('name')