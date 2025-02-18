i = 0
for x in range (0,4,1):
    i = int(input("Diz um número: \n"))
    if i%2 == 0 and i > 10:
        print("É par e maior que 10\n")
    elif i%2 != 0 and i > 10:
        print("É impar e maior que 10\n")
    elif i%2 == 0 and i == 10:
        print("É par e igual que 10\n")
    elif i%2 != 0 and i == 10:
        print("É impar e igual que 10\n")
    else:
        print("Número menor que 10. Perdes-te um numero")
        