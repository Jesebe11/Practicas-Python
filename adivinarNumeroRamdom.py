#-*- coding: utf-8 -*-
import random

def run ():
    numberFound = False
    randomNumber = random.randint(0,20)

    while not numberFound:
        number = int(input('Intenta adivinar el número: '))

        if number == randomNumber:
            print('Felicidades, encontraste el número')
            numberFound = True
        elif number > randomNumber:
            print('Ufff ese número es muy alto')
        else:
            print('UMMM estás muy por debajo crack')



if __name__ == '__main__':
    run()