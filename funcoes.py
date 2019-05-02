# Módulos:
def plus(parcela1, parcela2):
    return parcela1 + parcela2


def minus(minuendo, subtraendo):
    return minuendo - subtraendo


def times(fator1, fator2):
    return fator1 * fator2


def division(dividendo, divisor):
    return round((dividendo / divisor), 0)


def percentagem(lido, total):
    resultado_porcentagem = lido / total * 100
    return round(resultado_porcentagem, 1)
