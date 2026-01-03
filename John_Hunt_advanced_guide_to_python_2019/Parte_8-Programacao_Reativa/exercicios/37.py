import rx
from rx import operators as op

# Dado o seguinte conjunto de tuplas representando prços de ações:
stocks = (("APPL", 12.45), ("IBM", 15.55), ("MSFT", 5.66), ("APPL", 13.33))
observavel1 = rx.from_(stocks)
# Dê as soluções para o seguinte:
#   * Selecione todas as ações 'APPL'
pipe1 = observavel1.pipe(op.filter(lambda value: value[0] == "APPL"))
pipe1.subscribe(lambda v: print("Ações APPL:", v))
#   * Selecione todas as ações com preço acima de 15.00
pipe2 = observavel1.pipe(op.filter(lambda value: value[1] > 15.00))
pipe2.subscribe(lambda v: print("Ações acima de 15:", v))
#   * Encontre o preço médio de todas as ações 'APPL'
pipe3 = pipe1.pipe(op.average(lambda value: value[1]))
pipe3.subscribe(lambda v: print("Preço médio das ações APPL:", v))
# Agora use o segundo conjunto de tuplas e junte com o primeiro:
stocks2 = (
    ("GOOG", 8.95),
    ("APPL", 7.65),
    ("APPL", 12.45),
    ("MSFT", 5.66),
    ("GOOG", 7.65),
    ("IBM", 12.76),
)
observavel2 = rx.from_list(stocks2)
todos = rx.merge(observavel1, observavel2)

# Converta cada tupla em uma lista e calcule quanto 25 partes naquela ação seriam,
# e exiba o resultado.
todos_lista = todos.pipe(op.map(lambda value: list(value)))
todos_lista.subscribe(lambda v: print("25 ações de", v[0], "custam", 25 * v[1]))
#   * Encontre a ação mais cara
mais_cara = todos.pipe(op.max(lambda v1, v2: v1[1] - v2[1]))
mais_cara2 = todos.pipe(op.map(lambda v: v[1]), op.max())
mais_cara.subscribe(lambda v: print("A ação de maior valor é:", v))
mais_cara2.subscribe(lambda v: print("A ação de maior valor custa:", v))
#   * Encontre a ação mais barata
mais_barata = todos.pipe(op.min(lambda v1, v2: v1[1] - v2[1]))
mais_barata.subscribe(lambda v: print("A ação de menor valor é:", v))
#   * Apenas publique dados únicos (isto é, suprima duplicatas)
unicos = todos_lista.pipe(op.distinct()).subscribe(lambda v: print(v))
