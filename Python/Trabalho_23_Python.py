num = int(input("Diz um número: "))


horas = int(num // 3600)  
resto1 = num % 3600
minutos = int(resto1 // 60)  
segundos = resto1 % 60  

print(f"Horas: {horas} Minutos: {minutos} Segundos: {segundos}")
