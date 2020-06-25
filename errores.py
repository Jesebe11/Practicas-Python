

countries = {
    'mexico': 122,
    'colombia': 49,
    'argentina': 43,
    'chile': 18,
    'peru': 31
}

while True:
    country = str(input('Escribe el nombre de un país:   ')).lower()

    try:
        print('La población de {} es: {} millones'.format(country, countries[country]))
        
    except KeyError:
        print('No tenemos el dato de la población de {} ¿Desea agregarlo?'. format(country))
        print ('Si / No')
        respuesta = str(input(''))
        
        if respuesta == "si":
            habitantes = int(input('cuantos millones de habitantes tiene {}? '.format(country)))
            countries[country] = habitantes
        elif respuesta == "no":
            break