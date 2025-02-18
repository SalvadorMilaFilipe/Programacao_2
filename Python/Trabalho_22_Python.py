def CparaF():
    ValorCelsius = float(input("Diz a Temperatura: \n"))
    TF= ValorCelsius * (9/5) + 32
    print(f"Temperatura em Fahrenheit: {TF}")
def FparaC():
    ValorFahrenheit = float(input("Diz a Temperatura: \n"))
    TC = (ValorFahrenheit - 32) * 5/9
    print(f"Temperatura em Celsius: {TC}")
print("_____Menu_____\n 1 - Celsius para Fahrenheit \n 2 - Fahrenheit para Celsius\n")
escolha = int(input("E: "))
if escolha == 1:
 CparaF()
elif escolha == 2:
 FparaC()
