tamanho = ""
tamanhosdisponiveiz = ["Pequeno","Médio","Grande"]
sabores = ["chocolate","baunilha","morango"]
ingredientes = ["ovos","farinha","açúcar","fermento","manteiga","óleo","leite","iogurte","corante alimentar","raspa de limão"]
sabordobolo = ""
ingredientesdobolo = []
menufuncional = True
class bolo():
    def __init__(self, tamanho,pronto = False):
        self.tamanho = tamanho
        self.sabordobolo = []
        self.ingredientesdobolo = []
        self.pronto = pronto
        self.mostrar_receita()
    def mostrar_receita(self):
        
        while True:
            sabor = input(f"Sabores disponíveis: {sabores}\nEscolha o sabor do bolo: ").strip().lower()
            if sabor in sabores:
                self.sabordobolo = sabor
                break
            else:
                print("Erro! Esse sabor não está disponível. Escolha novamente.")

        print(f"Escolha 5 ingredientes entre: {ingredientes}")
        while len(self.ingredientesdobolo) < 5:
            boloingre = input(f"Ingrediente {len(self.ingredientesdobolo) + 1}: ").strip().lower()

            if boloingre not in ingredientes:
                print("Erro! Esse ingrediente não está disponível. Escolha novamente.")
            elif boloingre in self.ingredientesdobolo:
                print("Erro! Ingrediente já escolhido. Escolha outro.")
            else:
                self.ingredientesdobolo.append(boloingre)

        
        print(f"Sabor do bolo: {self.sabordobolo}\n Ingredientes no bolo: {', '.join(self.ingredientesdobolo)}")
        self.preparar_bolo()

    def preparar_bolo(self):
        print("O seu bolo já está pronto ou deseja completá-lo?")
        print("1 - Pronto")
        print("2 - Desejo Completá-lo")
        escolha = int(input("R: "))
        self.escolha = escolha
        if self.escolha == 1:

            self.pronto = True

        elif self.escolha == 2:

            self.pronto = False

        if self.pronto == True:
         
         self.mostrar_status()

        else:
         
         self.mostrar_receita()

    def mostrar_status(self):
        print(f"O seu bolo de {self.sabordobolo} com {', '.join(self.ingredientesdobolo)} está pronto. O tamanho escolhido foi o {tamanho}. Bom Apetite!") 

while menufuncional == True:
    print("___Menu___")
    print("1 - Criar Bolo")
    print("2 - Sair")
    fazer = int (input("Escolha:"))
    match fazer:
        case 1:
         tamanho = input("Tamanho do bolo: ")
         if tamanho != "Pequeno" and tamanho != "Médio" and tamanho != "Grande":
            print("Opção Inválida!!! Voltando ao menu")
         else:
          bolinho = bolo(tamanho) 
        case 2:
          menufuncional = False
        case _:
         print("Opção Inválida. Repita a sua escolha!!!")
   
