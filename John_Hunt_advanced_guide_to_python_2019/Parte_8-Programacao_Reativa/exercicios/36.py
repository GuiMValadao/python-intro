# Dado o seguinte conjunto de tuplas representando preços de ações:
stocks = (("APPL", 12.45), ("IBM", 15.55), ("MSFT", 5.66), ("APPL", 13.33))
# Escreva um programa que criará um Observável baseado nos dados das ações.
# Em seguida, escreva três observadores diferentes ao Observável. O primeiro
# deveria exibir o preço da ação, o segundo o nome da açõa e o terceiro a tupla
# completa.

import rx

observavel = rx.from_list(stocks)

observavel.subscribe(lambda v: print("Preço:", v[1]))
observavel.subscribe(lambda v: print("Nome da ação:", v[0]))
observavel.subscribe(lambda v: print("Preço e nome:", v))
