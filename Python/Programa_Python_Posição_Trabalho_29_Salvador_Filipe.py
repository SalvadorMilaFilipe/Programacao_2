import curses
import os

nometreinador = input("Insira o seu nome: ")
selecaotrinador = input("Insira a Selecao que treina/comanda: ")
os.system('cls' if os.name == 'nt' else 'clear')
nomejogador = []
idadejogador = []
posicaojogador = []
numeroselecao = []
posicaojogadordisponiveis = ["Guarda-Redes","Lateral Esquerdo","Lateral Esquerdo","Defesa Central","Medio Defensivo","Medio Esquerdo","Medio Centro","Medio Direito","Medio Ofensivo","Extremo Esquerdo","Extremo Direito","Segundo Avançado","Ponta de Lança"]
posicaojogadorabreviadas = ["GR","LE","LD","DC","MDF","ME","MC","MD","MO","EE","ED","SA","PL"]

def Convocar_Jogador():
    curses.endwin()
    jogadic = int(input("Nº de jogadores a adicionar: "))
    for i in range(jogadic):
     os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela antes de cada input
    
     print(f"Adicionando jogador {i+1}/{jogadic}\n")
    
     nomejogador.append(input("Nome jogador: "))
     idadejogador.append(input("Idade jogador: "))
     posicaojogador.append(input("Posição jogador: "))
     numeroselecao.append(input("Numero camisola jogador: "))

    curses.wrapper(menu)

def Dispensar_Jogador():
    curses.endwin()
    if not nomejogador:  # Verifica se há jogadores convocados
        input("\n Não há jogadores para dispensar! Pressione ENTER para voltar ao menu...")
        curses.wrapper(menu)
        return  

    print("\n📋 Lista de jogadores convocados:")
    for i, nome in enumerate(nomejogador):
        print(f"{i + 1}. {nome} ({posicaojogador[i]}) - {idadejogador[i]} anos \n")

    try:
        index = int(input("\nDigite o número do jogador a dispensar: ")) - 1

        if 0 <= index < len(nomejogador):
            print(f"\n Jogador {nomejogador[index]} foi dispensado!")
            nomejogador.pop(index)
            idadejogador.pop(index)
            posicaojogador.pop(index)
        else:
            print("\n Índice inválido!")

    except ValueError:
        print("\n Entrada inválida! Digite um número.")
    curses.wrapper(menu)

def Verificar_Convocatoria(stdscr):
    curses.endwin
    stdscr.clear()
    stdscr.addstr("📋 Convocatória dos Jogadores\n\n", curses.A_BOLD)

    if not nomejogador:
        stdscr.addstr("Nenhum jogador convocado!\n")
        stdscr.addstr("\nPressione qualquer tecla para voltar...")
        stdscr.refresh()
        stdscr.getch()
        return

    # Criar uma lista de dicionários com os dados dos jogadores
    jogadores = [{"Nome": nome, "Idade": idade, "Número": numero, "Posição": posicao}
                 for nome, idade, numero, posicao in zip(nomejogador, idadejogador, numeroselecao, posicaojogador)]

    # Ordenar os jogadores com base na posição usando a ordem de `posicaojogadordisponiveis`
    jogadores.sort(key=lambda j: posicaojogadordisponiveis.index(j["Posição"]) if j["Posição"] in posicaojogadordisponiveis else len(posicaojogadordisponiveis))
    
    # Definir a largura da coluna 'Nome' baseada no maior nome (mínimo 20 caracteres)
    largura_nome = max(20, max(len(j["Nome"]) for j in jogadores))
    
    # Cabeçalho da tabela
    stdscr.addstr(f"{'Nº':<5}{'Nome':<{largura_nome}}{'Idade':<8}{'Nº Camisola':<12}{'Posição':<20}\n", curses.A_UNDERLINE)

    # Exibir jogadores formatados
    for i, jogador in enumerate(jogadores, start=1):
        stdscr.addstr(f"{i:<5}{jogador['Nome']:<{largura_nome}}{jogador['Idade']:<8}{jogador['Número']:<12}{jogador['Posição']:<20}\n")

    abreviar = input("Deseja Abreviar as Posições (s/n): ")
    if abreviar == "s":
        
     jogadores = [{"Nome": nome, "Idade": idade, "Número": numero, "Posição": posicao}
                 for nome, idade, numero, posicao in zip(nomejogador, idadejogador, numeroselecao, posicaojogador)]

     jogadores.sort(key=lambda j: posicaojogadorabreviadas.index(j["Posição"]) if j["Posição"] in posicaojogadorabreviadas else len(posicaojogadorabreviadas))
    
   
     largura_nome = max(20, max(len(j["Nome"]) for j in jogadores))
    
   
     stdscr.addstr(f"{'Nº':<5}{'Nome':<{largura_nome}}{'Idade':<8}{'Nº Camisola':<12}{'Posição':<20}\n", curses.A_UNDERLINE)

   
     for i, jogador in enumerate(jogadores, start=1):
        stdscr.addstr(f"{i:<5}{jogador['Nome']:<{largura_nome}}{jogador['Idade']:<8}{jogador['Número']:<12}{jogador['Posição']:<20}\n")
    if abreviar == "n":
        curses.wrapper(menu)
    stdscr.addstr("\nPressione qualquer tecla para voltar...")
    stdscr.refresh()
    stdscr.getch()

def Verificar_Jogos():
    curses.endwin

def menu(stdscr):
    curses.curs_set(0)  # Esconder o cursor
    stdscr.keypad(1)  # Permitir captura de teclas especiais
    options = ["Convocar Jogador", "Dispensar Jogador", "Verificar Convocatória", "Verificar Jogos", "Fechar Programa"]
    selected = 0

    while True:
        stdscr.clear()
        stdscr.addstr("\tMenu de Posição\n\n")

        for i, option in enumerate(options):
            if i == selected:
                stdscr.addstr(f" > {option}\n", curses.A_REVERSE)
            else:
                stdscr.addstr(f"   {option}\n")

        key = stdscr.getch()

        if key == curses.KEY_UP:
            selected = (selected - 1) % len(options)  # Mover para cima
        elif key == curses.KEY_DOWN:
            selected = (selected + 1) % len(options)  # Mover para baixo
        elif key == 10:  # Enter pressionado
            stdscr.clear()
            if options[selected] == "Convocar Jogador":
                stdscr.addstr(f"\nAbrindo {options[selected]}...\n")
                Convocar_Jogador()
                stdscr.refresh()
                stdscr.getch()
            elif options[selected] == "Dispensar Jogador":
                stdscr.addstr(f"\nAbrindo {options[selected]}...\n")
                Dispensar_Jogador()
                stdscr.refresh()
                stdscr.getch()
            elif options[selected] == "Verificar Convocatória":
                stdscr.addstr(f"\nAbrindo {options[selected]}...\n")
                Verificar_Convocatoria(stdscr)
                stdscr.refresh()
                stdscr.getch()
            elif options[selected] == "Verificar Jogos":
                stdscr.addstr(f"\nAbrindo {options[selected]}...\n")
                Verificar_Jogos()
                stdscr.refresh()
                stdscr.getch()
            elif options[selected] == "Fechar Programa":
                exit()  # Fecha o programa imediatamente
                stdscr.refresh()
                stdscr.getch()
            break  


curses.wrapper(menu)

