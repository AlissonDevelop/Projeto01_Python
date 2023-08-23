saldo = 0
depositos = []
saques = []

while True:
    print("\nMenu:")
    print("1. Depósito")
    print("2. Saque")
    print("3. Extrato")
    print("4. Sair")

    opcao = input("Escolha uma opção: ") 

    if opcao == "1":
        valor = float(input("\nDigite o valor do depósito: "))
        if valor > 0:
            print(" ")
            print("-------------------------------------------------------------")
            print(" ")
            saldo += valor
            depositos.append(valor)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!!!\n\n-------------------------------------------------------------")
        else:
            print("Valor inválido para depósito!!!")
    elif opcao == "2":
        print(" ")
        valor = float(input("Digite o valor do saque: "))
        if valor > 0 and valor <= 500 and len(saques) < 3:
            print(" ")
            print("-------------------------------------------------------------")
            print(" ")
            if saldo >= valor:
                saldo -= valor
                saques.append(valor)
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!!!\n\n-------------------------------------------------------------")
            else:
                print("Saldo insuficiente para realizar o saque!!!\n\n-------------------------------------------------------------")
        else:
            print("Limite de saque diário atingido ou valor inválido!!!\n\n-------------------------------------------------------------")
    elif opcao == "3":
        print("Extrato:")
        print("Depósitos:")
        for valor in depositos:
            print(f"  Depósito: R$ {valor:.2f}")
        print("Saques:")
        for valor in saques:
            print(f"  Saque: R$ {valor:.2f}")
        print(f"Saldo atual: R$ {saldo:.2f}")
        print(" ")
        print("-------------------------------------------------------------")
    elif opcao == "4":
        print("Saindo do programa!!! Obrigado pela preferencia!!!")
        break
    else:
        print("Opção inválida. Escolha uma opção válida.([1] [2] [3] [4])")
        print(" ")
        print("-------------------------------------------------------------")
