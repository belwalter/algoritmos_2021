

def bernstein(cadena): 
    """Función hash de Bernstein para cadenas."""
    h = 0
    for caracter in cadena:
        h = h * 33 + ord(caracter)
    return h


print(bernstein('oso') % 5)
print(bernstein('osa') % 5)

palabra = ['arlbol', 'sginificado']

