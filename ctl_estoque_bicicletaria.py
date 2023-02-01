# Identificador Pessoal
print("Bem Vindo ao Controle de Estoque da Bicicletaria do Juan Cardoso dos Santos")  # noqa


def cadastrarPeca(codigo):
    print("Você Selecionou a Opção de Cadastrar Peça")
    print("Código da Peça 00{}" .format(codigo))
    # Dicionário(peca) - Inserção de dados em cada chave
    nome = input("Por favor entre com o NOME da peça:")
    fab = input("Por favor entre com o FABRICANTE da peça:")
    val = float(input("Por favor entre com o VALOR(R$) da peça:"))
    peca = {"codigo": codigo, "nome": nome, "fabricante": fab, "valor": val}
    return peca


def consultarPeca():
    op = 0
    print("Você Selecionou a Opção de Consultar Peças")
    while True:
        print("Escolha a opção desejada:")
        print("1-Consultar Todas as Peças")
        print("2-Consultar Peças por Código")
        print("3-Consultar Peças por Fabricante")
        print("4-Retornar")
        op = int(input(">>"))
        if op == 1:
            for cliente in pecas:  # Anda pelos indices da Lista - Cadastro de cada Cliente  # noqa
                print("-" * 15)
                for i, dados in cliente.items():  # Anda detro do Dicionário - Items e Dados do Cliente  # noqa
                    print("{} : {}". format(i, dados))
            print("-" * 15)
        elif op == 2:
            codigo = int(input("Digite o CÓDIGO da Peça: "))
            for cliente in pecas:
                for dados in cliente.values():
                    if dados == codigo:  # Condição para verificar o código dentro do dicionário  # noqa
                        print("-" * 15)
                        for i, dado in cliente.items():
                            print("{} : {}". format(i, dado))
            print("-" * 15)
        elif op == 3:
            fab = input("Digite o FABRICANTE da Peça: ")
            for cliente in pecas:
                for x, y in cliente.items():
                    if x == "fabricante" and y == fab:  # Condição para verificar o fabricante dentro do dicionário # noqa
                        print("-" * 15)
                        for i, dado in cliente.items():
                            print("{} : {}".format(i, dado))
            print("-" * 15)
        elif op == 4:
            break


def removerPeca():
    print("Você Selecionou a Opção de Remover Peça")
    apagar = int(input("Digite o codigo da peca a ser removida: "))
    deletar = 0
    for cliente in pecas:
        for dados in cliente.values():
            if dados == apagar:
                del pecas[deletar]  # Deleta os dados do código da Peça
                break
        deletar += 1


# Programa Principal
cod = 0
opcao = 0
pecas = []  # Lista para receber cada cadastro de Peças
while True:  # Menu de Opções
    print("Escolha a opção desejada:")
    print("1-Cadastrar Peças")
    print("2-Consultar Peças")
    print("3-Remover Peças")
    print("4-Sair")
    opcao = int(input(">>"))
    if opcao == 1:
        cod += 1
        # Inserção de um Novo elemento na Lista
        pecas.append(cadastrarPeca(cod).copy())
    elif opcao == 2:
        consultarPeca()  # Varredura de Lista e Dicionário
        continue
    elif opcao == 3:
        removerPeca()  # Remover um Elemento qualquer da Lista
    elif opcao == 4:
        break
