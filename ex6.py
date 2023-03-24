deposito = float(input('Insira o valor do seu depósito: '))
taxa = 0.5
mes = 1
montante = 0
saldo = deposito
while mes <= 12:
    saldo = saldo + (saldo * (taxa / 100))
    print(f"Saldo do mês {mes} é de R${saldo:5.2f}.")
    mes = mes + 1
print(f"O ganho obtido com os juros foi de R${saldo-deposito:8.2f}.")
