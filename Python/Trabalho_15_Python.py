totalnarray = int(input("Total de números no array: "))
numeros = []
for i in range (totalnarray):
    numero = float(input(f"Diz o {i+1}º número: "))
    numeros.append(numero)
soma = sum(numeros)
print(f"\n Soma dos números: {soma}")    