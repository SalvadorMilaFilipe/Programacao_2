idade = int(input("Diga a sua idade: \n"))
ping = 0
if idade > 0 and idade <= 12:
 ping == 0
if idade > 12 and idade <= 18:
 ping == 1
if idade > 18 and idade <= 70:
 ping == 2
if idade > 70:
 ping == 3
match ping:
    case 0: 
         print("Criança")
    case 1: 
         print("Adolescente")
    case 2: 
         print("Adulto")
    case 3: 
         print("Idoso")