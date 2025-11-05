# Exercício capítulo 6
# A seguinte tabela fornece informação das cidades no Reino Unido e suas
# populações. Use a tabela para criar:
# 1 - Um gráfico de dispersão
# 2 - Um gráfico de barras

import matplotlib.pyplot as pyplot

cidades = [
    "Bristol",
    "Cardiff",
    "Bath",
    "Liverpool",
    "Glasgow",
    "Edinburgh",
    "Leeds",
    "Reading",
    "Swansea",
    "Manchester",
]

populacao = [
    617280,
    447287,
    94782,
    864122,
    591620,
    464990,
    455123,
    318014,
    300352,
    395515,
]

pyplot.scatter(
    x=cidades,
    y=populacao,
    c="green",
    marker="o",
    linewidths=3,
)
pyplot.xlabel("Cidade")
pyplot.ylabel("População")
pyplot.title("População por cidade no Reino Unido")
# pyplot.legend()
pyplot.show()

indices = (
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
)
pyplot.bar(indices, populacao, tick_label=cidades)
pyplot.xlabel("Cidade")
pyplot.ylabel("População")
pyplot.title("População por cidade no Reino Unido")
pyplot.show()
