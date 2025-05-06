while True:
    print("1 - Biblioteca")
    print("2 - Calendário")
    print("0 - Sair")
    P = int(input())
    if P == 1:
        livro_lista = []
        autor_lista = []
        limite = 5
        for i in range (limite):
            livro = input()
            autor = input()
            livro_lista.append(livro)
            autor_lista.append(autor)

        iterador = iter(range(limite))

        while True:
            try:
                i = next(iterador)
                print(f"Livro {i}: {livro_lista[i]}")
                print(f"Autor {i}: {autor_lista[i]}")
            except StopIteration:
                break
        while True:
            print("1 - Procurar Livro por autor")
            print("0 - Sair")
            escolha = int(input())
            if escolha == 1:
                nome = input("Nome do Autor:")
                for i in range (limite):
                    if nome == autor_lista[i]:
                        print(f"{livro_lista[i]}")
                        print(f"{autor_lista[i]}")
            elif escolha == 0:
                break
    if P == 2:
        Disciplinas = ["TLP","Matemática","Português"]
        Dias_Semana = ["Segunda-Feira","Terça-Feira","Quarta-Feira","Quinta_Feira","Sexta_Feira"]
        disc_dia =[]
        dias = 5
        def contar_ate(dias):
            diaatual = 0
            while diaatual < dias:
                yield diaatual
                diaatual += 1


        dia_contador = 0
        for i in contar_ate(dias):
            disciplina = Disciplinas[dia_contador % len(Disciplinas)]
            disc_dia.append(disciplina)
            dia_contador += 1
        for i in range (dias):
            print(f"{Dias_Semana[i]}: {disc_dia[i]}")
    if P == 0:
        exit()
    if P != 1 and P != 2 and P != 0:
        print("Erro! Repita o seu número novamente")
