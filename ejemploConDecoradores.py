
def protected(func):
    def wrapper(password):
        if password == 'Jesebell':
            return func()
        else:
            print('La contraseña es incorrecta')
    
    return wrapper

@protected


def protectedFunc():
    print('Tu contraseña es correcta')




if __name__ == '__main__':
    password = str(input('Ingresa tu contraseña:  '))
   
protectedFunc(password)