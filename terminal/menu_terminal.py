from services.multas_service import cadastrar_multa, carregar_multas


def iniciar_terminal():
    multas = carregar_multas()

    while True:
        print("\n--- SISTEMA DE CONTROLE DE MULTAS (TERMINAL) ---")
        print("1 - Cadastrar multa")
        print("2 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            placa = input("Placa: ")
            data = input("Data: ")
            valor = input("Valor: ")
            descricao = input("Descrição: ")

            try:
                cadastrar_multa(placa, data, valor, descricao)
                print("Multa cadastrada com sucesso!")

            except ValueError as erro:
                print("Erro:", erro)

        elif opcao == "2":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")
