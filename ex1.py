print('\t ----Tabuada---- ')
num = int(input('Informe o numero para ver a tabuada: '))
print('\n Tabuada de', num, ':')
if (num >=1 and num <=10):
    for i in range(1, 11):
        print('\t ----Tabuada---- ')
        print(num, 'X', i, '=', (num * i))
else:
    print('Informe um valor válido!')