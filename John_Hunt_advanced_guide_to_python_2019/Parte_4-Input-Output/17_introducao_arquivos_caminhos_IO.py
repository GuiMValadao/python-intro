# Capítulo 17 - Introdução a arquivos, caminhos e IO

# O sistema operacional é uma parte crítica de quaisquer sistemas de computadores.
# É composto por elementos que gerenciam os processos que são executados na
# CPU, como a memória é utilizada e gerenciada, como dispositivos periféricos
# são usados (como impressoras e scanners), permite ao computador que se
# comunique com outros sistemas e também fornece suporte ao sistema de arquivos usado.
# O Sistema de Arquivos permite que programas armazenem dados permanentemente.
# Estes dados podem, então, ser recuperados pelos aplicativos posteriormente;
# potencialmente após o computador ser desligado e reiniciado. O Sistema de
# Gerenciamento de Arquivos é responsável por cuidar da criação, acesso e
# modificação do armazenamento de longo prazo em arquivos.
# Estes dados podem ser armazenados localmente ou remotamente em discos,
# fitas, dispositivos de DVD, USB etc. A maioria dos sistemas operacionais
# organizam arquivos em uma estrutura hierárquica, geralmente na forma
# de uma árvore invertida. Por exemplo, no diagrama da figura 'arquivos.png',
# a raiz(root) da estrutura de arquivos é mostrada como '/'. Esta pasta raiz
# armazena seis subpastas. Por sua vez, a subpasta Users tem outras 3 pastas.
# Cada arquivo é contido dentro de um diretório(também conhecido como pasta
# em alguns sistemas operacionais como Windows). Uma pasta pode guardar zero
# ou mais arquivos e zero ou mais pastas. Para qualquer pasta, existem
# relações com outras pastas como indicado abaixo:
# / - root
# Users - pai
# jhunt - pasta de trabalho
# workspaces - subpasta
# A pasta root é o ponto inicial para a estrutura de árvore hierarquica.
# Uma pasta filha de uma dada pasta é conhecida como subpasta. A pasta
# que armazena a pasta dada é conhecida como pai. Em qualquer tempo, a pasta
# dentro da qual o programa ou usuário está atualmente trabalhando é
# conhecido como pasta de trabalho atual.
# Um usuário ou programa pode mover-se nesta estrutura de pastas como necessário.
# Para fazer isso, o usuário pode, tipicamente, ou enviar uma série de comandos
# em um terminal ou janela de comando, como cd para mudar de pasta ou pwd para
# exibir a pasta de trabalho. Alternativamente, GUIs de sistemas operacionais
# geralmente incluem alguma forma de aplicativo gerenciador de arquivos que
# permite que usuários vejam a estrutura de arquivos na forma de uma árvore.
# ----------------------------------------------------
# Atributos de arquivos
# Um arquivo tem um conjunto de atributos associados com ele como a data em
# que foi criado, a data da última modificação/atualização, o tamanhos do
# arquivo etc. Normalmente, também terá um atributo indicando quem é o dono
# do arquivo; entretanto, a autoria de um arquivo pode ser alterada ou pela
# linha de comando ou por interfaces GUI. Por exemplo, em Linux e MacOS X
# o comando chown pode ser usado para alterar a autoria(ownership) do arquivo.
# Também pode ter outros atributos que indicam quem pode ler, escrever ou
# executar o arquivo. Em sistemas do estilo Unix, estes direitos de acesso
# podem ser especificados para o dono do arquivo, para o grupo associado
# ao arquivo e para todos os outros usuários.
# O dono do arquivo pode ter direitos especificados para leitura, escrita
# e execução de um arquivo. Eles são, geralmente, representados pelos símbolos
# 'r', 'w' e 'x', respectivamente. Por exemplo, os seguinte usa a notação
# simbólica associada com arquivos Unix e indica que o dono do arquivo tem
# permissão de ler, escrever e executar:
# -rwx---------
# Aqui, o primeiro traço é deixado em branco pois tem relação a arquivos
# (ou pastas) especiais, então os próximos três caracteres representam as
# permissões para o dono e os próximos três as permissões para todos os
# outros usuários. Como este exemplo tem rwx no primeiro grupo de três
# caracteres, o usuário pode realizar os três tipos de ações. Entretanto,
# os próximos 6 caracteres são todos traços indicando que o grupo e todos
# os outros usuários não podem acessar o arquivo.
# O grupo ao qual um arquivo pertence é um grupo que pode ter qualquer número
# de usuários como membros. Um membro de um grupo terá direito de acesso
# conforme indicado pelas configurações do grupo no arquivo. Assim como para
# o dono de um arquivo, elas podem ser leitura, escrita e execução. Por exemplo,
# se os membros do grupo tem permissão de leitura e execução de um arquivo,
# então isso seria mostrado usando a notação simbólica como:
# ----r-x---
# Se um usuário não é o dono de um arquivo, nem um membro do grupo do qual
# o arquivo faz parte, então seus direitos de acesso estão na categoria 'todos
# os outros'. Por exemplo, se todos tiverem permissão de leitura, seria:
# -------r--
# Obviamente, um arquivo pode ter uma mistura das permissões acima, de modo
# que o dono pode ser permitido rwx, o grupo rx e todos os outros r:
# -rwxr-xr--
# Além da notação simbólica, também há uma notação numérica que é usada com
# sistemas no estilo Unix. A notação numérica usa três dígitos para representar
# as permissões. Cada um dos três dígitos mais à direita representam um
# componente diferente de permissões: dono, grupo e outros.
# Cada um desses dígitos é a soma dos bits componentes no sistema binário
# numérico. Como resultado, bits especificados são somados como representado
# por um numeral:
#   * O bit leitura adiciona 4 ao total(em binário, 100)
#   * O bit escrita adiciona 2 ao total(em binário, 010)
#   * O bit execução adiciona 1 ao total(em binátio, 001)
#   * Assim a notação simbólica pode ser representada por uma numérica equivalente:
#       -rwx------|0700; -rwxrwx---|0770; -rwxrwxrwx|0777
# Pastas tem atributos e direitos de acesso similares aos arquivos. Por
# exemplo, a seguinte notação simbólica indica que uma pasta (indicada por
# 'd') tem permissões de leitura e execução para o dono e para o grupo.
# dr-xr-x---
# As permissões associadas a um arquivo ou pasta podem ser alteradas ou usando
# um comando do terminal ou janela de comando ou interativamente pela ferramenta
# de estilo do explorador de arquivos.
# ---------------------------------------------
# Caminhos (Paths)
# Um caminho é uma combinação particular de pastas que levam e uma pasta
# ou arquivo específico. Este conceito é importante pois sistemas de arquivos
# Unix/Linux/MaxOS/Windows representa uma árvore invertida de pastas e arquivos.
# Assim, é importante ser capaz de referenciar unicamente locais da árvore.
# Um caminho pode ser absoluto ou relativo. Um caminho absoluto fornece uma
# sequência completa de pastas a partir da raiz do sistema até uma subpasta
# ou arquivo. Um caminho relativo fornece uma sequência da parta de trabalho
# atual até uma subpasta ou arquivo particular.
# _--------------------------------------------------------
# Entrada/Saída de arquivos
# Em inglês File Input/Output(File I/O), envolve a leitura e escrita de dados
# de e para arquivos. Os dados sendo escritos podem estar em formatos
# diferentes. Por exemplo, um formato comum usado no Unix/Linux e Windows
# é o formato de texto ASCII(American Standard Code for Information Interchange).
# ASCII é um conjunto de códigos que representa vários caracteres que são
# amplamente usados por sistemas operacionais.
# ASCII pe um formato bastante útil ára arquivos de texto pois eles podem ser
# lidos por uma ampla variedade de editores e browsers. Esses editores e
# browsers facilitam a criação de arquivos legíveis para humanos. Entretanto,
# linguagens de programação como Python costumam usar um conjunto de codificação
# de caracteres diferentes como o Unicode(UTF-8). Unicode é outro padrão
# para representar caracteres usando vários códigos. Sistemas Unicode
# permitem uma maior quantidade de caracteres possíveis que ASCII.
# Entretanto, isso significa que pode ser necessário traduzir ASCII em
# Unicode e vice-versa ao ler e escrever arquivos ASCII em Python. Outra
# opção é usar um formato binário para dados em um arquivo. A vantagem de
# usar dados binários é que há pouca ou nenhuma tradução necessária para a
# representação interna dos dados usados no programa Python para o formato
# armazenado no arquivo. Também costuma ser mais conciso que o equivalente
# em ASCII e mais rápido para um programa ler e escrever, além de ocupar
# menos espaço em disco etc. Entretanto, o problema do formato binário é que
# não é fácil de ler para humanos. Também pode ser difícil para outros
# programas, particularmente aqueles escritos em outra linguagem de programação
# como Java ou C#, de ler os dados no arquivo.
# --------------------------------------------------
# Acesso sequencial x acesso aleatório
# Dados podem ser lidos de (ou escritos em) um arquivo ou sequencialmente
# ou por uma abordagem de acesso aleatório.
# Acesso sequencial de dados em um arquivo significa que o programa lê
# (ou escreve) dados em um arquivo sequencialmente, iniciando no começo de um
# arquivo e processando os dados um item por vez até o final do arquivo. O
# processo de leitura apenas se move para a frente, e apenas até o próximo
# item de dado a ser lido.
# Acesso aleatório de um arquivo de dados significa que o programa pode ler
# (ou escrever) dados em qualquer lugar no arquivo em qualquer momento. Isto é,
# o programa pode se posicionar em um ponto particular no arquivo (ou melhor,
# um apontador pode ser posicionado dentro do arquivo) e então pode começar
# a ler(escrever) naquele ponto. Se está lendo, então lerá o próximo item de dado
# relativo ao apontador em vez do início do arquivo. Se está escrevendo dados,
# então escreverá daquele ponto em vez de no final do arquivo. Se já existe
# dados naquele ponto no arquivo, então será sobrescrito. Este tipo de acesso
# também é conhecido como Acesso Direto pois o programa do computador precisa
# saber onde o dado está guardado dentro do arquivo e, assim, vai diretamente
# àquele lugar para o dado. Em alguns casos, o lugar do dado é guardado em um
# índice, sendo assim conhecido também como acesso indexado.
# Acesso sequencial a um arquivo tem suas vantagens quando um programa
# precisa acessar informação na mesma ordem toda vez que dados forem lidos.
# Também é mais rápido ler ou escrever todos os dados sequencialmente do que
# por acesso direto pois não há necessidade de mover o apontador do arquivo.
# O Acesso aleatório é mais flexível pois dados não precisam ser escritos ou
# lidos na ordem em que foram obtidos. Também é possível pular apenas para
# o lugar do dado requirido e ler aquele dado.
# -------------------------------------------
# Arquivos e I/O em Python
# No restante desta seção serão explorados recursos básicos fornecidos para
# leitura e escrita de arquivos em Python. Também olharemos no modelo de fluxos
# subjacente de I/O de arquivos. Em seguida, será explorado os formatos de arquivo
# CSV e Excel e bibliotecas existentes para suportá-los. Por fim, essa seção
# é concluída explorando recursos de expressão regular(Regular Expressions)
# em Python.
