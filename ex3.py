soma = 0
number = int(input('Entre com um número ou digite -1 para parar: '))

while number != -1:
    soma += number 
    number = int(input('Entre com um número ou digite -1 para parar: '))        
print('A soma é: ', soma)