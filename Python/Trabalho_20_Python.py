contabilizador = 0
numerosmencem = []
escolha = " "
while contabilizador < 100:
    if contabilizador > 5:
         print("Deseja encerrar o programa? (s/n)\n")
         escolha = input
    if escolha == "s":
           continue
    elif escolha == "n":
           break
    num = int(input("Diz um número: \n"))
    if num > 100:
        print("O número tem que ser menor que 100")
        pass
    else:
     numerosmencem.append(num)
     contabilizador += 1
    if contabilizador > 5:
        print("Deseja continuar o programa? (s/n)\n")
        escolha = input("Escolha: ")
        if escolha == "s":
           contabilizador = 0
           continue
        elif escolha == "n":
           break
    