def foreign_exchange_calculator(ammount):
    mex_to_col_rate = 145.97
    return mex_to_col_rate * ammount
def run():
    print('C A L C U D O R A DE C O N V E R S I O N')
    print('Convierte pesos mexicanos a pesos colombianos')
    print('')

    ammount = float(input('Ingresa la cantidad de pesos mexicanos que quieres convertir'))
    result = foreign_exchange_calculator(ammount)

    print('${} pesos mexicanos son ${} pesos colombianos'.format(ammount, result))
    print()


if __name__ ==  '__main__':
    run()