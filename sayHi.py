def sayHello():
    age = int(input('¿Cuál es tu edad actual? '))
    if(age >= 18):
        print('Eres un boomer')
    else:
        print('Eres un chaval')


if __name__ == '__main__':
    sayHello()