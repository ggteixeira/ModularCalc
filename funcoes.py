# Módulos:
def plus(parcela1, parcela2):
    return parcela1 + parcela2


def minus(minuendo, subtraendo):
    return minuendo - subtraendo


def times(fator1, fator2):
    produto = fator1 * fator2
    return produto


def division(dividendo, divisor):
    quociente = dividendo / divisor
    return round(quociente, 0)


def percentagem(lido=input, total=input, multiplica=100):
    resultado_porcentagem = lido / total * multiplica
    return round(resultado_porcentagem, 1)
