# -*- coding: utf-8 -*-
import random


IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']


WORDS = [
    'lavadora',
    'secadora',
    'sofa',
    'silla',
    'colchon',
    'computador',
    'teclado'
]

def randomWord():
    idx = random.randint(0, len(WORDS)-1)
    return WORDS[idx]

def displayBoard(hiddenWord, tries):
    print(IMAGES[tries])
    print('')
    print(hiddenWord)
    print('---*---*---*---*---*---*---*---*---*-----')


def run():
    word = randomWord()
    hiddenWord = ['-'] * len(word)
    tries = 0
    while True:
        displayBoard(hiddenWord, tries)
        currentLetter = str(input('Escoge una letra: '))

        letterIndexes = []
        for idx in range(len(word)):
            if word[idx] == currentLetter:
                letterIndexes.append(idx)
        if len(letterIndexes) == 0:
            tries += 1
        if tries == 7:
            displayBoard(hiddenWord, tries)
            print('')
            print('Lo sentimos, perdiste! La palabra correcta era: {}'.format(word))
            break
        else:
            for idx in letterIndexes:
                hiddenWord[idx] = currentLetter
            letterIndexes = []

        try:
            hiddenWord.index('-')
        except ValueError:
            print('')
            print('ENHORABUENA! Has acertado')
            break
    

if __name__ == '__main__':
    print('A H O R C A D O S')
    print('')

    run()