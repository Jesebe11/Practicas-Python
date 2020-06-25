
#Sin compresión pares
"""par = []

for num in range (1, 31):
    if num % 2 == 0:
        par.append(num)
print(par)"""


#Con compresion pares

"""even = [ num for num in range (1, 31) if num %2 ==0]
print(even)"""

# Con compresion Cuadrados

"""cuadrados = {}
for num in range(1,11):
    cuadrados[num] = num**2
    print(cuadrados)
"""

#Sin compresion Cuadrados

squares = {num: num**2 for num in range(1,11)}
print(squares)


