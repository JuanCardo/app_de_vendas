# Identificador Pessoal
print("Bem Vindo a Companhia de Logística Juan Cardoso dos Santos S.A.")
# Função - Transforma as dimensões(cm³) em valor(R$)


def quadro1(volume):
    if volume < 1000:
        x = 10
    elif 1000 <= volume < 10000:
        x = 20
    elif 10000 <= volume < 30000:
        x = 30
    elif 30000 <= volume < 100000:
        x = 50
    else:
        print("Não aceitamos objetos com dimensões tão grandes")
        print("Entre com as dimensões desejados novamente")
        x = 0
    return x
# Função - Transforma o peso(kg) em multiplicador


def quadro2(peso):
    if peso < 0.1:
        x = 1
    elif 0.1 <= peso < 1:
        x = 1.5
    elif 1 <= peso < 10:
        x = 2
    elif 10 <= peso < 30:
        x = 3
    else:
        print("Não aceitamos objetos tão pesados")
        print("Entre com o peso desejado novamente")
        x = 0
    return x
# Função - Transforma a rota em multiplicador


def quadro3(rota):
    if rota == "RS" or rota == "SR":
        x = 1
    elif rota == "BS" or rota == "SB":
        x = 1.2
    elif rota == "BR" or rota == "RB":
        x = 1.5
    else:
        print("Você digitou uma rota que não existe")
        print("Por favor entre com a rota desejada novamente")
        x = 0
    return x
# Função - Cálcula o volume do objeto e retorna o valor em R$ dele


def dimensoesObjeto():
    while True:
        try:  # Tentativas - executando linhas 49,50,51 sem Erros
            cmp = float(input("Digite o comprimento do objeto (em cm): "))
            lrg = float(input("Digite a largura do objeto (em cm): "))
            alt = float(input("Digite o altura do objeto (em cm): "))
        except ValueError:  # Erro de excessão
            print("Você digitou alguma dimensão do objeto com valor não numério") # noqa
            print("Por favor entre com as dimensões desejados novamente")
        else:
            print("O volume do objeto é (em cm³): {}".format(cmp * lrg * alt))
            rs = quadro1(cmp * lrg * alt)  # Passagem de parâmetro
            if rs == 0:
                continue
            break
    return rs
# Função - Retorna o multiplicador dependendo do peso(kg) do objeto


def pesoObjeto():
    while True:
        try:  # Tentativas - executando linha 66 sem Erros
            kg = float(input("Digite o peso do objeto (em kg): "))
        except ValueError:  # Erro de excessão
            print("Você digitou peso do objeto com valor não numérico")
            print("Por favor entre com o peso desejado novamente")
        else:
            mtpPeso = quadro2(kg)  # Passagem de parâmetro
            if mtpPeso == 0:
                continue
            break
    return mtpPeso
# Função - Retorna o multiplicador dependendo da rota do objeto


def rotaObjeto():
    while True:
        print("Selecione a rota:")
        print(" BR - De Brasília para Rio de Janeiro")
        print(" BS - De Brasília para São Paulo")
        print(" RB - De Rio de Janeiro para Brasília")
        print(" RS - De Rio de Janeiro para São Paulo")
        print(" SB - De São Paulo para Brasília")
        print(" SR - De São Paulo para Rio de Janeiro")
        sigla = input(">>")
        mtpRota = quadro3(sigla)  # Passagem de parâmetro
        if mtpRota == 0:
            continue
        break
    return mtpRota


# Programa Principal - Variáveis recebendo Valores das funções
dm = dimensoesObjeto()
ps = pesoObjeto()
rt = rotaObjeto()
total = dm * ps * rt  # Cálculo do valor por objeto
print("Total a pagar(R$): {:.2f} (dimensões: {} * peso: {} * rota: {})" .format(total, dm, ps, rt)) # noqa
