"""
"abacabad" c
"abacabaabacaba" _
"abcdefghijklmnopqrstuvwxyziflskecznslkjfabe" d
"bcccccccccccccyb" y
"""

def first_not_repeating_char(char_sequence):
    seenLetters = {}
    for idx, letter in enumerate(char_sequence):
        if letter not in seenLetters:
            seenLetters[letter] = (idx, 1)
        else:
            seenLetters[letter] = (seenLetters[letter][0], seenLetters[letter][1] + 1 )
    finalLetters = []
    for key, value in seenLetters.items():
        if value[1] ==1:
            finalLetters.append( (key, value[0]) )
    notRepeteadLetters = sorted(finalLetters, key=lambda value: value[1])

    if notRepeteadLetters:
        return notRepeteadLetters[0][0]
    else:
        return '_'

if __name__ == '__main__':
    char_sequence = str(input('Escribe una secuencia de caracteres: '))

    result = first_not_repeating_char(char_sequence)

    if result == '_':
        print('Todos los caracteres se repiten.')
    else:
        print('El primer caracter no repetido es: {}'.format(result))