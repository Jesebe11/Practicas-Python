
"""s = set([1, 2, 3])

t = set([3, 4, 5])

s.union(t)"""

"""s = set([1, 2, 3])

t = set([3, 4, 5])

s.intersection(t)"""

"""s = set([1, 2, 3])

t = set([3, 4, 5])

s.difference(t)"""


nombres = set(['Maria', 'Jose', 'Simon', 'Eleonor', 'Jesebell', 'Taner'])

findName = str(input('Ingresa tu nombre: '))

if findName in nombres:
    print('Hola {} : como estas? pasa adelante'.format(findName))
else:
    print('Uf {} tu no te encuentras en la lista, mi loco dele pa fuera'.format(findName))