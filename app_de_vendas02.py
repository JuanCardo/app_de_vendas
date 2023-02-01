# Identificador Pessoal
print("Bem Vindo a Lanchonete do Juan Cardoso dos Santos")
print("*****************Cardápio*****************")
print("| Código |       Descrição       | Valor |")
print("|   100  |    Cachorro Quente    |  9,00 |")
print("|   101  | Cachorro Quente Duplo | 11,00 |")
print("|   102  |          X-Egg        | 12,00 |")
print("|   103  |        X-Salada       | 12,00 |")
print("|   104  |         X-Bacon       | 14,00 |")
print("|   105  |         X-Tudo        | 17,00 |")
print("|   200  |   Refrigerante Lata   |  5,00 |")
print("|   201  |      Chá Gelado       |  4,00 |")
soma = 0  # Soma o total á ser pago
# Estrutura de Repetição(Loop) - Adiciona mais de 1 pedido
while True:
    cod = int(input("Entre com código desejado: "))
    # Estrutura Condicionais de Múltipla Escolha
    # Verificar qual foi o pedido - pelo código digitado
    if cod == 100:
        print("Você pediu um Cachorro-Quente no valor de 9,00")
        soma += 9
    elif cod == 101:
        print("Você pediu um Cachorro-Quente Duplo no valor de 11,00")
        soma += 11
    elif cod == 102:
        print("Você pediu um X-Egg no valor de 12,00")
        soma += 12
    elif cod == 103:
        print("Você pediu um X-Salada no valor de 12,00")
        soma += 12
    elif cod == 104:
        print("Você pediu um X-Bacon no valor de 14,00")
        soma += 14
    elif cod == 105:
        print("Você pediu um X-Tudo no valor de 17,00")
        soma += 17
    elif cod == 200:
        print("Você pediu um Refrigerante Lata no valor de 5,00")
        soma += 5
    elif cod == 201:
        print("Você pediu um Chá Gelado no valor de 4,00")
        soma += 4
    else:
        print("Opção Inválida")
        continue  # Código Incorreto - Retorna ao início do Loop
    print("Deseja pedir mais alguma coisa?")
    print("1 - Sim")
    print("0 - Não")
    opcao = int(input(">>"))
    if opcao == 0:
        break  # Finaliza do Pedido - Interrompe o Loop
print("O total a ser pago é: {:.2f}" .format(soma))
