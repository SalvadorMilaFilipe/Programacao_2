class Livro:
    def __init__(self, titulo, autor, disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel  

    def emprestar(self):
        if self.disponivel:  
            print(f"Livro '{self.titulo}' emprestado com sucesso!")
            self.disponivel = False
        else:
            print(f"Erro! O livro '{self.titulo}' não está disponível.")

    def devolver(self):
        if not self.disponivel:
            print(f"Livro '{self.titulo}' devolvido com sucesso!")
            self.disponivel = True
        else:
            print(f"Erro! O livro '{self.titulo}' já está disponível.")

    def informacoes(self):
        print(f"Título: {self.titulo} | Autor: {self.autor} | {'Disponível' if self.disponivel else 'Indisponível'}")


class Biblioteca:
    def __init__(self):
        self.livros = []  

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f"Livro '{livro.titulo}' adicionado à biblioteca.")

    def listar_livros(self):
        if not self.livros:
            print("A biblioteca não tem livros.")
        else:
            print("\nLivros na biblioteca:")
            for livro in self.livros:
                estado = "Disponível" if livro.disponivel else "Indisponível"
                print(f"- {livro.titulo} | {livro.autor} | {estado}")  



biblioteca = Biblioteca()


livro1 = Livro("Harry Potter e a Câmara de Gás", "Adolf Haller", True)
livro2 = Livro("Irreversível", "Ana Lincoln", False)
livro3 = Livro("Uma Aventura com o Ventura", "Sergio Ravlyuk", True)

livros = [livro1, livro2, livro3]  


biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)


while True:
    print("\n_____Titulo_____\n")
    print("Livros: \n")
    print("1 - Emprestar Livro\n2 - Devolver Livro\n3 - Informação de livro")
    print("\nBiblioteca: \n")
    print("4 - Adicionar Livro\n5 - Listar Livros\n6 - Sair")

    escolha = int(input("\nEscolha uma opção: "))

    if escolha in [1, 2, 3]:
        titulo = input("Digite o título do livro: ")
        livro_encontrado = next((livro for livro in livros if livro.titulo.lower() == titulo.lower()), None)

        if livro_encontrado:
            if escolha == 1:
                livro_encontrado.emprestar()
            elif escolha == 2:
                livro_encontrado.devolver()
            elif escolha == 3:
                livro_encontrado.informacoes()
        else:
            print(f"Erro! O livro '{titulo}' não foi encontrado.")

    elif escolha == 4:
        titulo = input("Digite o título do novo livro: ")
        autor = input("Digite o nome do autor: ")
        novo_livro = Livro(titulo, autor, True)
        livros.append(novo_livro)
        biblioteca.adicionar_livro(novo_livro)

    elif escolha == 5:
        biblioteca.listar_livros()

    elif escolha == 6:
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida! Tente novamente.")

            
