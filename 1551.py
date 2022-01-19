n = int(input())

for i in range(n):
    strg = str(input())
    onlyLetters = list()
    for i in strg:
        if i.isalpha():
            onlyLetters.append(i)
    length = len(set(onlyLetters))
    if length == 26:
        print('frase completa')
    elif length >= 13:
        print('frase quase completa')
    else:
        print('frase mal elaborada')
