qnum = int(input("Diz quantos números queres somar: \n"))
soma = 0
numeros = []
for i in range (qnum):
    numero = float(input("Diz um número: \n"))
    numeros.append(numero)
    soma = numeros[i] + soma
    print("Soma dos números: {:.7f}".format(soma),"\n")
print("Soma Total dos números: {:.7f}".format(soma),"\n")
print("Media: {:.7f}".format(soma/qnum))

    
