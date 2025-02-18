import random
import time
listanumger = []
acabar = False

while acabar == False:
 numadiv = int(input("Diz um número: \n"))
 certo = 0
 for i in range (1,10,1):
  numgerados = random.randint(1,10)
  print(numgerados)
 if numgerados == numadiv:
   certo += 1
 listanumger.append(numgerados)
 if certo >= 1:
   print("Um dos números da lista é igual ao número que puseste!")
   
 elif certo == 0:
   print("Nenhum dos números da lista é igual ao número que puseste! \n A Fechar programa...")
   time.sleep(2.5)
   break