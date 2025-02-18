
print("____Lados_dos_Triângulos____")
lado1 = float(input("Diz o calor do 1º lado do Triângulo: \n"))
lado2 = float(input("Diz o calor do 2º lado do Triângulo: \n"))
lado3 = float(input("Diz o calor do 3º lado do Triângulo: \n"))
ladosiguais = 0
if lado1 == lado2:
    ladosiguais += 1
if lado2 == lado3:
    ladosiguais += 1
if lado1 == lado3:
    ladosiguais += 1
if lado2 == lado1:
    ladosiguais += 1
if lado3 == lado2:
    ladosiguais += 1
if lado3 == lado1:
    ladosiguais += 1
if ladosiguais == 2:
    print("Triangulo Isosceles")
if ladosiguais == 0:
    print("Triangulo Escaleno")
if ladosiguais == 3:
    print("Triangulo Equilátero")