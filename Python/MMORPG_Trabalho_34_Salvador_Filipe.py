import random
import time

class Jogador:
    def __init__(self, nome, vida_total, nivel, exp):
        self.nome = nome
        self.vida_total = vida_total
        self.vida_atual = vida_total
        self.nivel = nivel
        self.exp = exp

    def ganhar_exp(self, monstro):
        if monstro == 1 :
            chance = random.randint(1 * self.nivel, 5 * self.nivel)
            if chance >= 2.5:
                exp_ganho = random.randint(1 * self.nivel, 8 * self.nivel)
                self.exp += exp_ganho
                print(f"Ganhaste!!! O exp ganho foi de {exp_ganho}")
            else:
                vida_perdida = random.randint(1 * monstro, 5 * monstro)
                self.vida_atual -= vida_perdida
                print(f"Perdeste!!! Vida Removida: {vida_perdida}")
        
        elif monstro == 2 and self.nivel > 10:
            chance = random.randint(2 * self.nivel, 8 * self.nivel)
            if chance >= 12:
                exp_ganho = random.randint(2 * monstro, 10 * monstro)
                self.exp += exp_ganho
                print(f"Ganhaste!!! O exp ganho foi de {exp_ganho}")
            else:
                vida_perdida = random.randint(2 * monstro, 10 * monstro)
                self.vida_atual -= vida_perdida
                print(f"Perdeste!!! Vida Removida: {vida_perdida}")
        elif self.nivel < 10:
            print("Não podes fazer esta luta (Nivel Requirido: 10)")
            pass
        elif monstro == 3 and self.nivel > 20:
            chance = random.randint(3 * self.nivel, 8 * self.nivel)
            if chance >= 35:
                exp_ganho = random.randint(3 * monstro, 10 * monstro)
                self.exp += exp_ganho
                print(f"Ganhaste!!! O exp ganho foi de {exp_ganho}")
            else:
                vida_perdida = random.randint(3 * monstro, 5 * monstro)
                self.vida_atual -= vida_perdida
                print(f"Perdeste!!! Vida Removida: {vida_perdida}")
        elif self.nivel < 20:
            print("Não podes fazer esta luta (Nivel Requirido: 20)")
            pass
        elif monstro == 4 and self.nivel > 40:
            chance = random.randint(4 * self.nivel, 8 * self.nivel)
            if chance >= 85:
                exp_ganho = random.randint(4 * monstro, 10 * monstro)
                self.exp += exp_ganho
                print(f"Ganhaste!!! O exp ganho foi de {exp_ganho}")
            else:
                vida_perdida = random.randint(5 * monstro, 6 * monstro)
                self.vida_atual -= vida_perdida
                print(f"Perdeste!!! Vida Removida: {vida_perdida}")
        elif self.nivel < 40:
            print("Não podes fazer esta luta (Nivel Requirido: 40)")
            pass
        # Verifica subida de nível
        while self.exp >= 100:
            self.nivel += 1
            self.exp -= 100
            self.vida_total += 5
            self.vida_atual = self.vida_total
            print(f"SUBISTE DE NIVEL!!! Nivel Atual: {self.nivel} e a tua vida foi restaurada")
            if self.nivel >= 100:
                print("Parabéns!!! Acabaste o Jogo!!!")
                exit

        # Verifica se o jogador morreu
        if self.vida_atual <= 0:
            print("O teu jogador morreu! Game Over!")
            exit()

    def exibir_status(self):
        print(f"Nome do Jogador: {self.nome}\nVida: {self.vida_atual}/{self.vida_total}\nNível: {self.nivel}\nExperiência: {self.exp}")


# Início do jogo
Nomejogador = input("Nome Jogador: ")
time.sleep(1.5)
print(f"Olá {Nomejogador} como estás? Vou agora te explicar como isto funciona.\n")
time.sleep(3)
print("O jogo consiste em derrotar monstros de diversos niveis, mas tem cuidado que quanto maior o nivel deles menor a chance de ganhares. \n")
time.sleep(3)
print("Mas não te preocupes!!! Quanto maior for o teu nivel maiora a chance de ganhares uma batalha. Chega até nivel 100 para ganhares o jogo.\n")
time.sleep(1.5)
print(f"Adeus {Nomejogador} e boa sorte! ")
VidaInicial = 100
NivelInicial = 1
EXPInicial = 0

jogador = Jogador(Nomejogador, VidaInicial, NivelInicial, EXPInicial)

# Menu principal
while True:
    print("\n=== Menu Principal ===")
    print("1 - Combater Monstro")
    print("2 - Ver Estatísticas")
    print("0 - Sair")
    escolha = input("Escolha: ")

    if escolha == "1":
        print("1 - Monstro nível 1")
        print("2 - Monstro nível 10")
        print("3 - Monstro nível 50")
        print("4 - Final Boss (nível 100)")
        monstro = int(input("Escolhe o monstro (1-4): "))
        jogador.ganhar_exp(monstro)

    elif escolha == "2":
        jogador.exibir_status()

    elif escolha == "0":
        print("Até à próxima!")
        break

    else:
        print("Opção inválida.")
