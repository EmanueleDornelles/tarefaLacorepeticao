import random

total_coroa = 0
total_cara = 0
count = 0
jogadas = int(input('Insira a quantidade de jogadas que deseja fazer: '))

while count < jogadas:
    moeda = random.randint(1, 2)
    if moeda == 1:
        print("Coroa!\n")
        total_coroa += 1
        count += 1

    elif moeda == 2:
        print("Cara!\n")
        total_cara += 1
        count += 1

print("\nVocê jogou coroa", total_coroa, "vezes ")
print("\ne Coroa", total_cara, "vezes ")