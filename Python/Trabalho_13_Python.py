print("______MENU______")
print("1 - Calcular IMC")
print("2 - Fechar o programa")
escolha = int(input("e: "))
if escolha == 1:
    peso = float(input("Diga a sua peso: \n"))
    altura = float(input("Diga a sua altura: \n")) 
    IMC = peso/(altura * 2)
    ping = 0
    if  IMC < 18.5:
        ping == 0
    if IMC > 18.5 and IMC <= 24.9:
        ping == 1
    if IMC > 25 and IMC <= 29.9:
         ping == 2
    if IMC > 30 and IMC <= 34.9:
        ping == 3
    if IMC > 35 and IMC <= 39.9:
        ping == 4
    if IMC > 40:
        ping == 5
    match ping:
        case 0: 
         print("Magreza")
        case 1: 
         print("Normal")
        case 2: 
         print("Sobrepeso")
        case 3: 
         print("Obesidade Grau - I")
        case 4: 
         print("Obesidade Grau - II")
        case 4: 
         print("Obesidade Grau - III")
elif escolha == 2:
   print("A sair...")