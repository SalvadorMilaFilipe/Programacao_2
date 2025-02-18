numi = int(input("Diz um número inicial: "))
numf = int(input("Diz um número final: "))
nprimos = []
for i in range(numi, numf + 1):
    if i > 1:
        for x in range(2, int(i**0.5) + 1):
            if i % x == 0:
                break 
        else:
            nprimos.append(i)
print(f"Números primos: {nprimos}")