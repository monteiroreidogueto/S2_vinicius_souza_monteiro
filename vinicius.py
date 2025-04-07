def main():
    
    loja.adicionar_carro(Carro("Corolla Cros", "Toyota", 2020, 150000.00, 20))
    loja.adicionar_carro(Carro("Onix premier", "Chevrolet", 2024, 90000.00, 10))
    loja.adicionar_carro(Carro("Q7", "Audi", 2023, 220000.00, 15))
    loja.adicionar_carro(Carro("SW4", "Toyota", 2022, 240000.00, 20))
    
    while True:
        print("Bem-vindo à loja de carros!")
        print("1. Listar shorts")
        print("2. Adicionar produto ao carrinho")
        print("4. Realizar compra")
        print("5. Sair")

        opcao = input("Escolha uma opção (1-5): ")

        if opcao == "1":
            loja.listar_carros()
        elif opcao == "2":
            modelo_carro = input("Digite o modelo do carro: ")
            quantidade = int(input("Digite a quantidade: "))
            loja.adicionar_ao_carrinho(modelo_carro, quantidade)
        elif opcao == "3":
            loja.exibir_carrinho()
        elif opcao == "4":
            loja.realizar_compra()
        else:
            print("Opção inválida. Tente novamente.")