import time
class Veiculo:
    def __init__(self, modelo, marca, ano, consumo, deposito_combustivel):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.consumo = consumo
        self.deposito_combustivel = deposito_combustivel 

    def abastecer(self, litros):
        self.deposito_combustivel += litros

    def conduzir(self, distancia):
        combustivel_necessario = distancia / self.consumo
        if combustivel_necessario <= self.deposito_combustivel:
            self.deposito_combustivel -= combustivel_necessario
            print(f"Você percorreu {distancia} km. Combustível restante: {self.deposito_combustivel:.2f} litros.")
        else:
            print("Combustível insuficiente para percorrer essa distância.")

    def exibir_informacoes(self):
        print(f"Modelo: {self.modelo}")
        print(f"Marca: {self.marca}")
        print(f"Ano: {self.ano}")
        print(f"Depósito: {self.deposito_combustivel:.2f} litros")
        print(f"Consumo: {self.consumo:.2f} km/l")

class Frota:
    def __init__(self):
        self.veiculos = []

    def adicionar_veiculo(self, veiculo):
        self.veiculos.append(veiculo)

    def listar_veiculo(self):
        if len(self.veiculos) == 0:
            print("Nenhum veículo na frota.")
        for i, veiculo in enumerate(self.veiculos):
            print(f"\nVeículo {i+1}:")
            veiculo.exibir_informacoes()

    def encontrar_veiculo(self, modelo_buscado):
        encontrado = False
        for veiculo in self.veiculos:
            if veiculo.modelo.lower() == modelo_buscado.lower():
                print("\nVeículo encontrado:")
                veiculo.exibir_informacoes()
                encontrado = True
                break
        if not encontrado:
            print("Veículo com esse modelo não encontrado.")



frota = Frota()


veiculo = Veiculo("Corolla", "Toyota", 2020, 12, 40)
frota.adicionar_veiculo(veiculo)

Menuativo = True
while Menuativo:
    print("\n    Menu    ")
    print("Veículos:")
    print(" 1 - Abastecer Veículo")
    print(" 2 - Conduzir Veículo")
    print(" 3 - Exibir Informações do Veículo")
    print("Frota:")
    print(" 4 - Adicionar Veículo")
    print(" 5 - Listar Veículos")
    print(" 6 - Encontrar Veículo")
    print("Outros:")
    print(" 0 - Sair")
    escolha = int(input("Escolha: "))

    match escolha:
        case 1:
            if len(frota.veiculos) == 0:
                print("Nenhum veículo disponível.")
                continue
            frota.listar_veiculo()
            indice = int(input("Escolha o número do veículo: ")) - 1
            if 0 <= indice < len(frota.veiculos):
                litros = float(input("Quantos litros deseja abastecer? "))
                frota.veiculos[indice].abastecer(litros)
            else:
                print("Índice inválido.")
        case 2:
            if len(frota.veiculos) == 0:
                print("Nenhum veículo disponível.")
                continue
            frota.listar_veiculo()
            num = int(input("Escolha o número do veículo para conduzir: "))
            indice = num - 1
            if 0 <= indice < len(frota.veiculos):
                distancia = float(input("Digite a distância a ser percorrida (km): "))
                frota.veiculos[indice].conduzir(distancia)
            else:
                print("Índice inválido.")
        case 3:
            if len(frota.veiculos) == 0:
                print("Nenhum veículo disponível.")
                continue
            frota.listar_veiculo()
        case 4:
            modelo = input("Modelo: ")
            marca = input("Marca: ")
            ano = int(input("Ano: "))
            consumo = float(input("Consumo (km/l): "))
            deposito = float(input("Quantidade de combustível no depósito (l): "))
            novo_veiculo = Veiculo(modelo, marca, ano, consumo, deposito)
            frota.adicionar_veiculo(novo_veiculo)
            print("Veículo adicionado com sucesso!")
        case 5:
            frota.listar_veiculo()
        case 6:
            modelo_buscado = input("Digite o modelo do veículo que deseja encontrar: ")
            frota.encontrar_veiculo(modelo_buscado)
        case 0:
            Menuativo = False
            print("Encerrando o programa...")
            time.sleep(3)
        case _:
            print("Opção inválida.")
