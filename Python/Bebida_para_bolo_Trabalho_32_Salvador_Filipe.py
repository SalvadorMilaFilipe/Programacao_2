import time

bebidas = ["Café","Chá","Chocolate Quente"]

tamanhos = ["Pequena", "Média","Grande"]

Proceder = False

pf = True

sf = True

while Proceder == False:
 print(f"Bebidas deisponiveis: {bebidas}")
 bebida = input("")

 if bebida not in bebidas:
     print("Deve escolher 1 bebida na lista")
 else:
    Proceder = True

while Proceder == True:
 while pf == True:
  print(f"{tamanhos}")
  tamanho = input("")
  if tamanho not in tamanhos:
   print("Deve escolher um tamanho da lista")
  else:
   pf = False
 while sf == True:
    print("Deseja aquecer a Bebidas?")
    print("1 - Sim")
    print("2 - Não")
    aquecer = int(input("Escolha:"))

    if aquecer == 1:
        print("A Aquecer...")
        time.sleep(3)
        print(f"Bebida escolhida: {bebida} ({tamanho}) - Temperatura: Quente")
        sf = False

    elif aquecer == 2:
            print(f"Bebida escolhida: {bebida} ({tamanho}) - Temperatura: Fria")
            sf = False