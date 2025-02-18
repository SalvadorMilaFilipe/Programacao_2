numeros = []
ninicial = float(input("Número Inicial: "))

for i in range(14):
    numero_atual = ninicial + (i * 2.5)  
    numeros.append(numero_atual)

print("\nContagem feita de 2,5 em 2,5:")
for i, numero in enumerate(numeros):
    print(f"Posição {i + 1}: {numero}")

acumulador = sum(numeros)  
media = acumulador / len(numeros)  
print(f"\nA média é de {media:.2f}")
