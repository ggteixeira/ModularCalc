# modular-calc
from funcoes import plus
from funcoes import minus
from funcoes import times
from funcoes import division
from funcoes import percentagem

print(
    "Bem-vindo! \n Selecione a operação desejada:\n 1) Adição \n 2) Subtração \n 3) Multiplicação \n 4) Divisão \n 5) Percentagem \n 0) 0 para sair."
)

while True:
    entrada_usuario = int(input("Digite o número da operação desejada: \n"))

    if entrada_usuario == 1:
        print("Você escolheu: Adição!\n")

        parcela1 = input("Adição: Insira a primeira parcela: \n")
        parcela2 = input("Adição: Insira a segunda parcela: \n")

        print(f"A soma é: {plus(int(parcela1), int(parcela2))}")

    if entrada_usuario == 2:
        print("Você escolheu: Subtração!\n")

        minuendo = input("Insira o minuendo: \n")
        subtraendo = input("Insira o subtraendo: \n")

        print(f"O resultado da diferença é {minus(int(minuendo), int(subtraendo))}")

    if entrada_usuario == 3:
        print("Você escolheu multiplicação!\n")

        fator1 = input("Digite o primeiro fator: \n")
        fator2 = input("Digite o segundo fator: \n")

        print(f"O produto da multiplicação é {times(int(fator1), int(fator2))}")

    if entrada_usuario == 4:
        print("Você escolheu divisão!")

        dividendo = input("Insira um dividendo: \n")
        divisor = input("Insira um divisor: \n")

        print(f"A resposta da divisão é {division(int(dividendo), int(divisor))}")

    if entrada_usuario == 5:
        print("Você escolheu porcentagem!\n")
        total = input("Porcentagem: Qual o total de páginas? \n")
        lido = input("Porcentagem: Quantas páginas já foram lidas? \n")
        resposta_porcentagem = percentagem(int(lido), int(total))
        print("Você leu: %s%%." % (resposta_porcentagem))

    elif entrada_usuario == 0:
        print("Programa encerrado.")
        break
