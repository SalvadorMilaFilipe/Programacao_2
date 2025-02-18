listnum = []
for i in range (10):
    num = int(input("Diz um número"))
    listnum.append(num)
for i in range (10):
    if listnum [i] >= 25:
        print(f"O número {listnum[i]} é maior que 25")
    elif listnum [i] < 25:
        print(f"O número {listnum[i]} é menor que 25")
