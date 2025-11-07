# Capítulo 7 - Interfaces Gráficas de Usuário
# Uma Interface Gráfica do Usuário (GUI) pode capturar a essência de uma
# ideia ou situação, muitas vezes evitando a necessidade para uma longa
# passagem de texto. Estas interfaces podem evitar que o usuário precise
# aprender comandos complexos. Elas diminuem a probabilidade de usuários
# de computador se sentirem intimidados e fornecem grandes quantidades de
# informação rapidamente de uma forma que pode ser facilmente assimilada pelo
# usuário. A ampla utilização de interfaces gráficas de alta qualidade levou
# muitos usuários de computados a esperar que qualquer software que usem
# tenham tais interfaces. A maioria das linguagens de programação ou incorporam
# uma biblioteca GUI ou tem bibliotecas de terceiros disponíveis.
# Como Python é uma linguagem multiplataforma, isto traz algumas complexidades
# devido diferentes sistemas poderem fornecer diferentes instalações de janelas.
# Neste capítulo, será introduzido o que significam uma GUI e interfaces de usuários
# (UIs) baseadas em WIMP.
# -------------------------------------------------
# GUIs e WIMPs
# Os estilos de interface GUIs e WIMP(Windows, Icons, Mice and Pop-up
# Menus/Janelas, Ícones, Mouses, e Menus de Pop-up) estão disponíveis dentro de
# sistemas de computador por muitos anos, mas ainda são um dos desenvolvimentos
# mais significativos a terem acontecido. Elas forma criadas originalmente para
# lidar muitas das fraquezas percebidas em iterfaces puramente textuais.
# A interface textual de um sistema operacional foi tipificada por um prompt
# autoritário(peremptório). Em sistemas Unix/Linux, por exemplo, o prompt é
# frequentemente simplesmente um único caractere como %, > ou $, o que pode
# ser intimidador. Por exemplo, um usuário que gostaria de copiar um arquivo de
# uma pasta para outra poderia ter de digitar algo como:
# >cp file.pdf ~otheruser/projdir/srcdir/newfile.pdf
# Esta longa sequência deve ser digitada sem erros para poder ser aceita. Qualquer
# erro neste comando fará com que o sistema gere uma mensagem de erro que
# poderia ou não ser esclarecedora. Mesmo onde sistemas tentam ser mais
# 'amigáveis a usuários' por recursos como histórico de comandos, muita
# digitação de teclas de setas e arquivos de nomes é tipicamente necessário.
# O principal problema tanto na entrada quanto na saída é a largura de banda.
# Por exemplo, em situações onde as relações entre grandes quantidades de
# informação devem ser descritas, é muito mais fácil assimilar isto se a saída
# é exibida graficamente em vez de ser exibida como tabelas de figuras. Na
# entrada, combinações de ações do mouse podem ser dadas um significado que
# poderia, de outra forma, ser entregue por muitas linhas de texto.
# Interfaces WIMP permitem que o usuário supere, pelo menos, algumas das
# fraquezas de suas contra-partes textuais.
# Os conceitos fundamentais apresentados por uma interface WIMP foram, originalmente,
# desenvolvidas no Centro de Pesquisa XEROX's de Palo Alto e usados na máquina
# Xerox Star, mas ganharam aceitação maior pelo Macintosh da Apple e então
# implementações no PC da IBM.
# A maioria de ambientes de estilo WIMP usam a analogia desktopp:
#   * a tela inteira representa uma superfície de trabalho (ou desktop)
#   * janelas gráficas que podem se sobrepor representam folhas de papel na mesa
#   * objetos gráficos são usados para conceitos específicos, por exemplo,
#       armários-arquivos para discos ou uma lixeira de lixo para remoção de arquivos.
#   * vários programas de aplicação são mostrados na tela, estes equivaleriam
#       a ferramentas que poderia usar na mesa.
# Para poder interagir com esta exibição, o usuário do WIMP é fornecido com um
# mouse (ou uma caneta de luz ou tela sensível ao toque), que pode ser usado
# para selecionar ícones e menus ou manipular janelas.
# A base de software de qualquer ambiente no estilo WIMP é o gerenciado de
# janela. Ela controla as múltiplas, possivelmente sobrepostas, janelas e ícones
# mostrados na tela. Também cuida da transferência de informação sobre eventos que
# ocorrem naquelas janelas à aplicação apropriada e gera os vários menus e
# prompts utilizados. Uma janela é uma área da tela gráfica na qual uma página
# ou uma parte de uma página de informação pode ser exibida; pode mostrar
# texto, gráficos ou uma combinação de ambos. Estas janelas podem se sobrepor,
# e associada ao mesmo processo, ou podem ser associadas com diferentes processos.
# As janelas podem ser geralmente criadas, abertas, fechadas, movidas e redimensionadas.
# Um ícone é um pequeno objeto gráfico que é, geralmente, simbólico de uma
# operação ou de uma entidade maior como um programa de aplicação ou arquivo.
# A abertura de um ícone causa ou a aplicação associada a executar ou a janela
# associada ser exibida. No coração da habilidade dos usuários de interagir
# com programas baseados em WIMP está o loop de evento. Este loop escuta
# eventos como o usuário clicar em um botão ou selecionar um item do menu ou
# entrar um campo de texto. Quando tal evento ocorre, ele aciona o comportamento associado.
# -----------------------------------------------
# Estruturas de janelamento para Python
# Python é uma linguagem de programação multiplataforma. Como tal, programas
# em Python podem ser escritos em uma plataforma (como Linux) e executados
# na mesma plataforma ou uma plataforma com outro sistema operacional (como
# Windows ou Max OS). Entretanto, isto pode gerar problemas para biblioetecas
# que precisam estar disponíveis através de plataformas baseadas em múltiplos
# sistemas operacionais. A área de GUIs é particularmente problemática como
# uma biblioteca escrita para explorar recursos disponíveis no sistema Windows
# da Microsoft podem não estar disponíveis (ou serem diferentes) de sistemas
# Linux ou Mac OS. Cada sistema operacional que executa Python pode ter um ou
# mais sistemas de janelamento escritos para ele e estes sistemas podem ou não
# estar disponíveis em outros sistemas operacionais. Isto torna o trabalho de
# fornecer uma biblioteca GUI para Python bem mais difícil.
# Desenvolvedores de GUIs para Python escolhem uma entre duas abordagens para
# lidar com isso:
#   * Uma abordagem é escrever um empacotador(wrapper) que abstrai as instalações
#       subjacentes da GUI de modo que o desenvolvedor trabalha em um nível
#       acima das instalações de janelamento de um sistema específico. A
#       biblioteca Python então mapeia (o melhor que pode) as instalações
#       com o sistema adjacente que está sendo usado.
#   * A outra abordagem é fornecer um empacotador de fechamento para um
#       particular conjunto de instalações no sistema GUI adjacente e apenas
#       escolhe sistemas que tem suporte àquelas instalações.
# Algumas das bibliotecas para Python são listadas abaixo e foram categorizadas
# em bibliotecas independente de plataformas e específicas para uma plataforma.
# ------------------------------------------------------
# Bibliotecas GUI Independente de plataformas:
#   * Tkinter: A biblioteca GUI padrão embutida em Python. É construída em
#       cima do conjunto de dispositivos Tcl/Tk que estão disponíveis há
#       muitos anos para muitos sistemas operacionais diferentes. Tcl significa
#       Tool Command Language, enquanto Tk é o conjunto de ferramentas de interface
#       gráfica de usuários para Tcl.
#   * wxPython: wxWidgets é uma biblioteca GUI gratuita e altamente portável.
#       É escrita em C++ e pode fornecer um visual e sensação nativos em
#       sistemas operacionais como Windows, Mac OS, Linux etc. exPython é
#       um conjunto de ligações de Python ao wxWidgets.
#   * PyQT ou PySide: ambas bibliotecas  empacotam instalações do kit de
#       ferramentas Qt. Qt é um sistema de desenvolvimento de software
#       multiplataforma para a implementação de GUIs e aplicações.
# ----------------------------------------------------
# Bibliotecas GUI Específico de Plataforma
#   * PyObj: é uma biblioteca específica do sistema Mac OS que fornece uma
#       ponte Objective-C para bibliotecas GUI Appla Mac Cocoa.
#   * PythonWin: fornece um conjunto de empacotadores em torno de classes
#       da Microsoft Windows Foundation e pode ser usado para criar
#       GUIs baseadas em Windows.
