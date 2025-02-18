import random

Tentativas = 0
palavras = ["homem", "impossível", "poltrona", "caneta", "estojo", "rato", "fonte", "Sanita", "Mila", "Porta"]
palavra_adivinhar = random.choice(palavras)
palavra_adivinhar = palavra_adivinhar.lower() 
adivinha = ["_"] * len(palavra_adivinhar)  # Um string que fica com o mesmo tamanho da palavra a adivinhar. Pq não ter, né?
letras_tentadas = set()  # Armazena letras já ditas (nem sabia que isto existia)

print("Palavra:", " ".join(adivinha))

while adivinha != palavra_adivinhar and Tentativas != 6:

    tentativa_adivinhar = input("Digite uma letra: \n")  # Recebe a entrada como string
    tentativa_adivinhar = tentativa_adivinhar.lower()   # Garante que é minuscula (a letra)
  

    # Verifica se a entrada é válida
    if len(tentativa_adivinhar) != 1 or not tentativa_adivinhar.isalpha():
        print("Por favor, insira apenas uma letra válida.\n")
        continue  # Vai para a próxima iteração se a entrada for inválida

    # Verifica se a letra já foi tentada
    if tentativa_adivinhar in letras_tentadas:
        print("Já tentaste essa letra. Escolhe outra.\n")
        continue

    letras_tentadas.add(tentativa_adivinhar)  # Adiciona a letra às tentativas

    nova_adivinha = list(adivinha)  # Converter a lista em um array(?) para verificar as letras

    if tentativa_adivinhar in palavra_adivinhar:
        # Verifica TODAS as letras da palavra
        for i, letra in enumerate(palavra_adivinhar):  # Vai rodar todos os _ do array
            if letra == tentativa_adivinhar:
                nova_adivinha[i] = tentativa_adivinhar  # Substitui os _ pela letra dita
    else:
        print("A letra não está na palavra!")
        Tentativas += 1
        print("Tentativas restantes:", 6 - Tentativas, "\n")

    adivinha = "".join(nova_adivinha)  # Converte para string de novo
    print("Palavra: ", " ".join(adivinha))  # Mostra a palavra atualizada

# Vê se o jogador ganhou ou perdeu
if "_" not in adivinha:
    print("\nParabéns! Acertaste a palavra:", palavra_adivinhar)
else:
    print("\nFim de jogo! A palavra era:", palavra_adivinhar)
'''
O isalpha() restringe o input a apenas algo! pode ser simbolos letra numeros, etc
O islower() limita o input a apenas letras minúsculas
O join() introduz palavras inteiras num array, preenchendo cada letra num espaço do array (eu acho)
'''
