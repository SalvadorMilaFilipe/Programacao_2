prod = ['Camisa', 'Calça', 'Casaco', 'T-shirt']
box2 = [15, 25, 50, 10]
nprodutos = [] #array do nome dos produtos
pprodutos = [] #array do preço dos produtos
desativar = 0
total = 0
while desativar == 0:
    print("1-Adicionar, 2-Ver carrinho, 3- Remover Produto 0-Sair")
    esc = int(input())

    match esc:
        case 1: # Adiciona os Produtos ao Carrinho
            print("1-Camisa=15€\n2-Calça=25€\n3-Casaco=50€\n4-T-shirt=10€\n")
            produto = input("Diz o nome de um dos produtos acima: \n")

            if produto in prod:
                index = prod.index(produto)
                total += box2[index]
                nprodutos.append(produto) # Adiciona o nome do produto ao array do nome dos produtos no carrinho
                pprodutos.append(box2[index]) # Adiciona o preço do produto ao array do preço dos produtos no carrinho
                print(f"{produto} adicionado ao carrinho por {box2[index]}€")
            else:
                print("Produto não encontrado!")
        
        case 2: # Vê os produtos no carrinho
            if not nprodutos:
                print("Carrinho vazio!")
            else:
                print("Produtos no carrinho:")
                for i in range(len(nprodutos)):
                    print(f"{nprodutos[i]} - {pprodutos[i]}€")
                print("\n Total - ", total, "€\n")   
        case 3: # Remove produtos no carrinho
              produto = input("Diz o nome de um dos produtos acima: \n")

              if produto in prod:
                index = nprodutos.index(produto)
                total -= pprodutos[index]
                nprodutos.pop(index) # Remove o nome do produto ao array do nome dos produtos no carrinho
                pprodutos.pop(index) # Remove o preço do produto ao array do preço dos produtos no carrinho
                print(f"{produto} removido ao carrinho")
                
              else:
                print("Produto não encontrado!")
        
        case 0:
            desativar = 1
        case _:
            print("Opção inválida! Diz outro número")
