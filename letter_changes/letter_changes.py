from string import ascii_lowercase

VOWELS = 'aeiou'


def LetterChanges(str):
    new_chars = []

    for char in str:
        if char == 'z':  # o caracter/ "z" tem o indice "26" no array, neste caso não há indice "27"
            new_chars.append('a')  # o indice "a" é  "0", indice 26 + 1 fica "0"
            continue  # Faz o for "pular" para o próximo elemento, caso o valor sejka "z", ou seja não executa o "try"
        try:
            index_char = ascii_lowercase.index(char)
        except ValueError:
            new_chars.append(char)  # caracteres especias neste caso, assumem o caracter atual/original
        else:
            new_index = index_char + 1
            new_char = ascii_lowercase[new_index]
            new_chars.append(new_char)

    def vowels_to_upper(vChar): # função que substitui a condição ternária > Se o caracter estiver contido ele executa a
        # ação, se não reotna ele mesmo
        if vChar in VOWELS:
            return vChar.upper()
        return vChar

    new_chars = [
        vowels_to_upper(char)
        for char in new_chars
    ]

    return ''.join(new_chars)  # concatena os elementos de uma lista em uma string inteira
