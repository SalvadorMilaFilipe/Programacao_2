import time
nalunos = 6
alunos = []
idades = []
medias = []
mediasalunos = []
nnotas = 0
mediaa = 0
acumulador = 0
status = []
while nalunos <= 0 or nalunos > 5:
 nalunos = int(input("Nº de alunos na turma: \n"))
 nnotas = int(input("Nº de disciplinas: \n"))
linhas = nalunos
colunas = nnotas
notas = [[None for _ in range(colunas)] for _ in range(linhas)]
for i in range (nalunos):
    nomealuno = input(f"{i+1}º aluno: \n")
    alunos.append(nomealuno)
    idadealuno = input(f"Idade do {i+1}º aluno: \n")
    idades.append(idadealuno)
for i in range(nalunos):
    acumulador = 0  
    for x in range(nnotas):
        notas[i][x] = float(input(f"Nota do(a) {alunos[i]} na disciplina {x+1}: \n"))
        acumulador += notas[i][x]
    mediaa = acumulador / nnotas
    mediasalunos.append(mediaa)
    if mediasalunos[i] >= 7:
       status.append("Aprovado")
    elif mediasalunos[i] < 7:
       status.append("Reprovado")
print("Processo Concluido...\n")   
time.sleep(2)   
print("A Criar Tabela de dados...\n")
time.sleep(3)   
for x in range(nnotas):
    soma = sum(notas[i][x] for i in range(nalunos))  # Soma das notas da disciplina x
    media = soma / nalunos  # Média da disciplina x
    medias.append(media)
    

# Ajustar largura da primeira coluna (maior nome)
largura_nome = max(len(nome) for nome in alunos + ["Média"]) + 2  
print("\nAlunos:\n")
for i in range (nalunos):
 print(f"{alunos[i]}: {idades[i]}")
print("\nTabela de Notas:\n")


print("Aluno".ljust(largura_nome), end="")  # Primeira coluna (nomes dos alunos)
for x in range(nnotas):
    print(f"Disc{x+1}".rjust(8), end="")  # Disciplinas alinhadas 
print()


for i in range(nalunos):
    print(alunos[i].ljust(largura_nome), end="")  # Nome do aluno 
    for x in range(nnotas):
        print(f"{notas[i][x]:>8.2f}", end="")  # Notas alinhadas
    print()

#Linha para as médias das disciplinas
print("Média".ljust(largura_nome), end="")  # Título das médias
for x in range(nnotas):
    print(f"{medias[x]:>8.2f}", end="")  # Médias alinhadas 
print()
for i in range (nalunos):
 print(f"Média {alunos[i]}: {mediasalunos[i]} - {status[i]}\n")

