numero = 1
numeros = []
while numero != 0:
    numero = int(input("Diz um número (o programa acaba quando digitares 0): "))
    numeros.append(numero)
    soma = sum(numeros)
print(f"Soma dos Números: {soma}")