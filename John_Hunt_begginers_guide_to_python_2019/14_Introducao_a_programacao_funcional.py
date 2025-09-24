# Introduçao a programaçao funcional
# Programaçao funcional e um estilo ou abordagem de programaçao de software
# e separada do conceito de funçao em Python
# As funçoes do Python podem ser usadas para escrever programas funcionais
# mas tambem podem ser usadas para escrever programas em estilo processual.
#-----------------------------------------------
# O que e programaçao funcional?
# A wikipedia descreve programacao funcional como:
#   ... um paradigma de programaçao, um estilo de construir a estrutura e elementos
#   de programas de computador, que trata a computaçao como a avaliaçao de funçoes
#   matematicas e evita estado e dados mutaveis.
# Esta definiçao e focada no lado computacional da programaçao de computadores.
# O modo como as computaçoes sao representadas enfatiza funlçies que geram resultados
# baseados puramente nos dados fornecidos a elas. Isto e, estas funçoes dependem
# apenas de suas entradas para gerar uma nova saida. Elas nao geram em nenhum
# efeito colateral e nao dependem no estado atual do programa. Como um exemplo
# de efeito colateral, se uma funçao guardou um total em processo em uma
# variavel global e outra funçao usou esse valor para realizar algum calculo
# entao a primeira funçao tem um efeito colateral de modificar uma variavel
# global e a segunda depende em algum estado global para sua saida,
# 1 -   Programaçao Funcional objetiva eliminar efeitos colaterais. Uma funçao
#       deveria ser substituivel tomando os dados que ela recebe e alinhando o
#       resultado gerado (isto e referido como transparencia referencial).
#       Isto quer dizer que nao deveriam haver efeitos colaterais da funçao.
#       Efeitos colaterais escondidos tornam mais dificil de entender o que um
#       programa esta fazendo e assim tornam a compreensao, desenvolvimento e
#       manutençao mais dificeis. Funçoes puras tem as seguintes caracteristicas:
#           * A unica saida observavel e o valor em 'return'.
#           * A unica dependencia da saida sao os argumentos.
#           * Argumentos sao completamente determinados antes de qualquer saida ser gerada.
# 2 -   Programaçao Funcional evita conceitos como estado. Se alguma operaçao e
#       dependente do (possivelmente escondido) estado do programa em algum elemento de um
#       programa ou algum elemento de um programa, entao seu comportamento pode
#       diferir denpendendo deste estado. Isto pode tornar o programa mais dificil
#       de compreennder, implementar, testar e fazer depurar. Como todos esses
#       impactam a estabilidade e provavelmente a confiabilidade de um sistema.
#       operaçoes baseadas em estado podem resultar em software menos confiavel
#       sendo desenvolvido. Como funçoes nao dependem (nao deveriam) em um dado
#       estado (apenas aos dados que lhe sao fornecidos) elas deveriam, como resultado
#       ser mais faceis de entender, implementar, testar e depurar.
# 3 -   Programaçao Funcional promove dados imutaveis. FP tambem tende evitar
#       conceitos como dados mutaveis. Dados mutaveis sao dados que podem mudar
#       de estado. Em contrapartida, imutabilidade indica que uma vez criado,
#       o dado nao pode ser mudado. Em Python, 'strings' sao imutaveis. Quaisquer
#       funçoes aplicadas a uma string que podem conceitualmente altera-la, resultam
#       em uma nova string gerada. Muitos desenvolvedores usam isto para ter uma
#       presunçao de imutabilidade em seus codigos; isto quer dizer que por padrao
#       todos os typos que guardam dados sao implementados como imutaveis. Isto garante
#       que funçoes nao podem receber efeitos colaterais escondidoss e assim simplifica
#       programaçao em geral.
# 4 -   Programaçao Funcional promove programaçao declarativa, o que significa
#       que a programaçao e orientada para criar expressoes que descrevem a
#       soluçao em vez de focar na abordagem imperativa da maioria das linguagens
#       de programaçao processuais. Linguagens imperativas enfatizam aspectos de
#       como a soluçao e derivada. Por exemplo, uma abordagem imperativa para
#       fazzer loop atravez de algum container e exibir cada resultado seria:
#int sizeOfContainer = container.length
#for(int i = 1 to sizeOfContainer) do
#    element = container.get(i)
#    print(element)
#enddo
#       Enquanto a abordagem de programaçao funcional seria:
#container.foreach(print)
# Programaçao imperativa: o que e atualmente percebida como programaçao tradicional.
# Isto e, o estilo usado em linguagens como C, C++, Java e C#, etc.
# Programaçao funcional: objetiva descrever a soluçao, que e o que o programa
# precisa fazer (em vez de como deveria ser feito)
#----------------------------------------------------
# Vantagens da Programaçao Funcional
# 1 - Menos codigo
# 2 - Ausencia de efeitos colaterais (escondidos) (Transparencia Referencial)
# 3 - Reccursao e uma estrutura de controle natural
# 4 - Boa para prototipar soluçoes
# 5 - Funcionalidade modular
# 6 - Evitar comportamento baseado em estado
# 7 - Estruturas de controle adicionais
# 8 - Simultaneidade e dados imutaveis
# 9 - Avaliaçao parcial
#----------------------------------------------------
# Desvantagens da programaçao funcional
# 1 - Entrada-Saida e mais difiicil em uma linguagem puramente funcional
# 2 - Aplicativos interativos sao mais dificeis de desenvolver
# 3 - Programas que executam continuamente
# 4 - Linguagens de programaçao funcional tendem a ser menos eficiente em plataformas de hardware atuais
# 5 - Nao e orientada por dados
# 6 - Programadores sao menos familiarizados com conceitos de programaçao funcional
# 7 - Idiomas de programaçao funcional sao normalmente menos intuitivos
# 8 - Costumavam ser vista como um linguagem puramente academica.
#----------------------------------------------------
# Transparencia referencial
# Uma operaçao e dita Transparente Referencialmente se ela pode ser substituida
# com seu valor correspondente, sem alterar o comportamento do programa, para
# um dado conjunto de parametros.
# Por exemplo:
#def increment(num):
#    return num+1
#print(increment(5))
# Uma funçao e dita Transparente Referencialmente(RT) se ela sempre retorna
# o mesmo resultado para o mesmo valor (ou seja, increment(5) sempre retorna 6)
# Qualquer funçao que referncia um valor que foi obtido do seu entorno no
# contexto do programa e que pode ser modificado nao pode ser garantidamente RT.
# Por exemplo:
#amount = 1
#def increment(num):
#    return num + amount
#print(increment(5))
#amount = 2
#print(increment(5))
# O retorno desta funçao e 6 e 7.
# Uma ideia similar e a de 'Sem efeitos colaterais'. Isto e, uma funçao
# nao deveria ter nehum efeito colateral, com sua operaçao baseada
# completamente nos valores que recebe e seu impacto no resultado retornado.
# Obviamente, dentro da maioria das aplicaçoes ha grande necessidade de efeitos
# colaterais, por exemplo, qualquer registro de açoes realizadas por um programa
# tem o efeito colateral de atttualizar alguma informaçao registrada em algum lugar
# (como um arquivo), qualquer base de dados vai ter algum efeito colateral (a atualizaçao
# da base de dados). Alem disso, alguns comportamentos sao inerentemente nao-RT
# como a funçao que retorna o tempo atual.