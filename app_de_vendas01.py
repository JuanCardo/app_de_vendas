print("Bem Vindo a Loja do Juan Cardoso dos Santos")
# Variáveis e Entrada de Dados
produto = float(input("Entre com valor do produto: "))
quantidade = int(input("Entre com valor da quantidade: "))
comDesconto = float
semDesconto = float(produto * quantidade)  # Cálculo sem desconto
print("O valor sem desconto foi: R$ {:.2f}".format(semDesconto))
# Estrutura Condicionais de Múltipla Escolha - Mostra o desconto Recebido
if quantidade <= 9:
    print("O valor com desconto foi: R$ {:.2f}  (desconto 0%)" .format(
        semDesconto))
elif quantidade <= 99:
    comDesconto = semDesconto - (semDesconto * 0.05)  # Cálculo com Desconto
    print("O valor com desconto foi: R$ {:.2f}  (desconto 5%)" .format(
        comDesconto))
elif quantidade <= 999:
    comDesconto = semDesconto - (semDesconto * 0.1)
    print("O valor com desconto foi: R$ {:.2f}  (desconto 10%)" .format(
        comDesconto))
else:
    comDesconto = semDesconto - (semDesconto * 0.15)
    print("O valor com desconto foi: R$ {:.2f}  (desconto 15%)" .format(
        comDesconto))
