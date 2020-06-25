#-*- coding: utf-8 -*-

def generacion(age):
if age >= 72:
print (‘Eres de la generacion Niños de la postguerra, es decir seres humanos que nacieron entre los años de 1930 y 1948’)
elif age <= 71 and age >= 52:
print (‘Eres de la generacion Baby boom, es decir seres humanos que nacieron entre los años de 1949 y 1968’)
elif age <= 51 and age >= 40:
print (‘Eres de la generacion X, es decir seres humanos que nacieron entre los años de 1969 y 1980’)
elif age <= 39 and age >= 27:
print (‘Eres de la generacion Millennials, es decir seres humanos que nacieron entre los años de 1981 y 1993’)
elif age <= 26 and age >= 10:
print (‘Eres de la generacion Z, es decir seres humanos que nacieron entre los años de 1994 y 2010’)
elif age <= 9 and age >= 1:
print (‘Eres un baby y aún no tienes generacion definida, es decir seres humanos que nacieron entre los años de 2011 y 2020’)
elif age <= 1:
print (‘No existes!!! Pero no te preocupes porque tal vez tus padres te tengan en planes’)

def run():
age = int(input('Escribe tu edad: '))
result = generacion(age)

if name == ‘main’:
run()
print (’ ‘)
print (‘Esto fue todo por ahora’)
print (’ ')
print (‘Fue un placer indicar tu generacion de acuerdo con tu edad’)