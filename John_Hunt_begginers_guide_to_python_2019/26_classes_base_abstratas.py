# Capítulo 26 - Classes base abstratas
# Este capítulo apresente Classes base abstratas(também conhecidas
# como ABCs) que foram originalmente introduzidas em Python 2.6. 
# Uma Classe Base Abstrata é uma classe que não se pode instanciar
# e que é esperada que seja estendida por uma ou mais subclasses.
# Estas subclasses irão, então, preencher quaisquer lacunas deixadas
# pela classe base. Elas são muito úteis para criar hierarquias de
# classes com um alto nível de reutilização da classe raiz na 
# hierarquia.
# -----------------------------------------------
# Classes abstratas como um conceito
# Uma classe abstrata é uma classe da qual você não pode
# criar um objeto. Tipicamente estão ausentes um ou mais elementos
# necessários para criar um objeto completamente funcional.
# Em contraste, uma classe não-abstrata(ou concreta) não deixa
# nada indefinido e pode ser usada para criar um objeto funcional.
# Você poderia questionar qual a utilidade de uma classe abstrata?
# A resposta é que você pode agrupar elementos para serem compartilhados
# por um número de classes, sem fornecer uma implementação completa.
# Além disso, você pode forçar que subclasses providenciem métodos
# específicos garantindo que implementadores de uma subclasse pelo
# menos forneçam métodos nomeados apropriadamente. Você deveria, portanto,
# usar classes abstratas quando:
#   * você quer especificar dados ou comportamentos comuns a um conjunto de 
#       classes, mas insuficientes para uma única instância
#   * você quer forçar subclasses a fornecer comportamentos específicos.
# Em muitos casos, as duas situações ocorrem simultaneamente. Tipicamente,
# os aspectos da classe a ser definida como abstrata são específicos
# de cada classe, enquanto o que foi implementado é comum a todas as classes.
# --------------------------------------------------
# Classes base abstratas em Python
# ABCs não podem ser instanciadas por si só, mas podem ser extendidas 
# por subclasses. Estas subclasses podem ser classes concretas ou
# podem ser, elas também, ABCs (que extendem o conceito definido
# na ABC raiz).
# ABCs podem ser usadas para definir comportamento genérico (potencialmente
# abstrato) que pode ser misturado em outras classes Python e agem
# como uma raiz abstrata da hierarquia de classe. Eles podem também
# ser usados para fornecer um modo formal de especificar comportamento
# que deve ser fornecido por uma classe concreta.
# ABCs podem ter:
#   * Zero ou mais métodos ou propriedades abstratos (mas não são requiridas) 
#   * Zero ou mais métodos e propriedades concretas (não são requiridas)
#   * Ambos atributos privados e protegidos (seguindo as convenções de
#       barra única _ e barra dupla __)
# ABCs também podem ser usados para especificar uma interface específics
# ou protocolo formal. Se um ABC define quaisquer métodos ou propriedades
# abstratos, então as subclasses devem fornecer implementações para 
# todos os tais elementos abstratos.
# Há muitos ABCs embutidos em Python, incluindo:
#   * estruturas de dados (módulo collection),
#   * módulo numbers,
#   * streams (fluxos?)(módulo IO).
# De fato, ABCs são amplamente usadas internamente dentro do próprio Python
# e muitos desenvolvedores usam ABCs sem mesmo saber que elas existem
# ou entender como definí-las.
# Realmente, ABCs não são amplamente usadas por desenvolvedores 
# construindo sistemas com Python, apesar disso ser, em parte,
# porque elas são mais apropriadas para quem constrói bibliotecas,
# em particular aquelas que se esperam que sejam estendidas pelos
# próprios desenvolvedores.
# ---------------------------------------
# Subclassificando um ABC
# Tipicamente, uma ABC precisará ser importada do módulo
# em que é definida; claro, se a ABC é definida no módulo atual
# então isso não é necessário. Como um exemplo, a classe 
# collections.MutableSequence é uma ABC; esta é uma ABC para uma
# sequência de elementos que podem ser modificados (mutáveis) e 
# iterados sobre. Nós podemos usar isso como a classe base para
# nosso próprio tipo de coleção que chamaremos Bag, por exemplo:
# 
# from collections import MutableSequence
# class Bag(MutableSequence):
#   pass
# 
# Neste exemplo, estamos importando MutableSequence do módulo
# collections. Então definimos a classe Bag como extensão da ABC
# MutableSequence. Por hora, estamos usando a palavra chave especial
# de Python 'pass' como um reservador de espaço para o corpo da classe.
# Entretanto, isto significa que a classe Bag é, de fato, também uma classe
# abstrata como ela não implementa nenhum dos métodos abstratos na
# ABC MutableSequence. Entretanto, Python não valida isto na hora da
# importação; em vez disso, valida na hora da execução quando uma instância
# do tipo está para ser criada. Assim, se um programa tentar criar uma
# instância de Bag, o seguinte erro seria levantado:
# Traceback (most recent call last):
#
#File "/pythonintro/abstract/Bag.py", line 10, in <module>
#main()
#File "/pythonintro/abstract/Bag.py", line 7, in main
#bag = Bag()
#TypeError: Can't instantiate abstract class Bag with abstract
#methods __delitem__, __getitem__, __len__, __setitem__,
#insert 
# 
# Como pode ser visto, este é um requerimento bem formal; se você
# não implementar todos os métodos definidos como abstratos na classe
# mãe, então não pode criar uma instância da classe que está definindo
# (pois ela também é abstrata).
# Podemos definir um método para cada uma das classes abstratas a classe
# Bag e então seremos capazes de criar uma instância da classe. Por
# exemplo:
# 
# from collections import MutableSequence
# class Bag(MutableSequence):
#   def __getitem__(self, index):
#       pass
#   def __delitem__(self, index):
#       pass
#   def __len__(self):
#       pass
#   def __setitem__(self, index, value):
#       pass
#   def insert(self, index, value):
#       pass
# 
# Esta versão de Bag cumpre todos os requerimentos impostos sobre
# ela pela ABC MutableSequence; isto é, ela implementa cada um dos
# métodos especiais listados e o método insert. A classe Bag pode
# agora ser considerada como uma classe concreta. Entretanto, neste
# caso os métodos em si não fazem nada (usam novamente a palavra chavem
# de Python pass). Entretanto, agora podemos escrever:
# bag = Bag()
# E a aplicação não gerará uma mensagem de erro. Neste ponto poderíamos
# agora implementar cada método de modo que fornece uma implementação
# apropriada de Bag.
# -----------------------------------------------    
