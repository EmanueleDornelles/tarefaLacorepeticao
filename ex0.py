n1 = int(input('Insira o primeiro valor:'))
n2 = int(input('Insira o último valor: '))

maior_numero = 0
menor_numero = 0

if n1>n2:
    maior_numero = n1
    menor_numero = n2
    contador = menor_numero
else: 
    maior_numero = n2
    menor_numero = n1
    contador = maior_numero

while contador <= maior_numero:
    print(contador)
    contador +=1
    break
