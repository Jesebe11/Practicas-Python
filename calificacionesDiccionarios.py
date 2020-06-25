# -*- coding: utf-8 -*-

calificaciones = {}

calificaciones['Algortimos'] = 6
calificaciones['Matemáticas'] = 6
calificaciones['Web'] = 6
calificaciones['Logica'] = 6
calificaciones['Bases de Datos'] = 6

sumaDeCalificaciones = 0

for key, value in calificaciones.items():
    print('Calificaciones por materia: {}, valor: {}'.format(key, value))

for calificacion in calificaciones.values():
    sumaDeCalificaciones += calificacion

promedio = sumaDeCalificaciones // len(calificaciones.values())
      

print('Tu promedio querido estudiante, es de {}'.format(promedio))
if promedio <= 5:
    print('Sigue intentando, debes esforzarte más')
elif promedio >= 6:
    print('Adelante, vas por buen camino')