def main():
<<<<<<< Updated upstream

=======
    
    loja.adicionar_carro(Carro("Corolla Cros", "Toyota", 2020, 150000.00, 20))
    loja.adicionar_carro(Carro("Onix premier", "Chevrolet", 2024, 90000.00, 10))
    loja.adicionar_carro(Carro("Q7", "Audi", 2023, 220000.00, 15))
    while True:
      
        print("2. Adicionar produto ao carrinho")
        print("4. Realizar compra")
        print("5. Sair")

      
        if opcao == "1":
            loja.listar_carros()
        
           
            quantidade = int(input("Digite a quantidade: "))
            loja.adicionar_ao_carrinho(modelo_carro, quantidade)
        elif opcao == "3":
            loja.exibir_carrinho()
       
            loja.realizar_compra()
>>>>>>> Stashed changes
        else:
            print("Opção inválida. Tente novamente.")