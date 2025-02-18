import random
numreand = random.randint(1,10)
tentativas = random.randint(1,5)
print(f"Tens {tentativas} tentativas para acertar um número entre 1 e 10\n")
for i in range (tentativas):
    numero = int(input("Escolha: "))
    if numero == numreand:
        print("Parabens Ganhaste!!!")
        exit
    elif numero != numreand:
        print("Número errado!!!")
        tentativas = tentativas - 1
        print(f" {tentativas} tentativas restantes \n")
    if tentativas == 0:
        print(f"Perdeste!!! O número certo era {numreand}")