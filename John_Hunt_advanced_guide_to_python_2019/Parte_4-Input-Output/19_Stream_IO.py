# Capítulo 19 - Fluxo Entrada/Saída(I/O)

# Neste capítulo estudaremos o modelo de Fluxo Entrada/Saída(Stream I/O)
# que sustenta o modo com o qual dados são lidos de e escritos em fontes e
# sumidouros. Um exemplo de uma fonte ou sumidouro de dados é um arquivo,
# mas outro poderia ser uma matriz de bytes. Este modelo é, na verdade, o
# que está abaixo dos mecanismos de acesso a arquivos discutidos no capítulo
# anterior. Não é, de fato, necessário entender este modelo para ser capaz
# de ler e escrever dados de e para um arquivo, mas em algumas situações
# é útil entendê-lo para poder modificar o comportamento padrão quando
# ---------------------------------------------------
# O que é um fluxo(Stream)
# Fluxos são objetos que servem como fontes ou sumidouros de dados. Num
# primeiro momento, este conceito pode parecer estranho. O modo mais fácil
# de se pensar em um fluxo é como condutor de dados fluindo de ou para
# uma piscina. Alguns fluxos leem dados direto da 'fonte de dados' e outros
# leem dados de outros fluxos. Esses últimos, então, fazem algum processamento
# 'útil' dos dados como converter os dados brutos em um formato específico.
# Um fluxo pode ler ou escrever dados em uma fonte de dados em vez de apenas
# um arquivo. Essa fonte pode ser um arquivo, um socket, um pipe, uma string,
# um serviço web etc.
# ----------------------------------------------------------
# Fluxos Python
# O módulo Python 'io' fornece os principais recursos de Python para lidar
# com entrada e saída de dados. Há três tipos principais de IO, sendo eles:
# texto I/O, binário I/O e raw I/O. Essas categorias podem ser usadas com
# vários tipos de fontes/sumidouros de dados. Independente da categoria,
# cada fluxo concreto pode ter um número de propriedades, como ser somente-leitura,
# somente-escrita ou leitura-escrita. Também pode suportar acesso sequencial
# ou aleatório dependendo da natureza do sumidouro de dados. Por exemplo,
# ler dados de um socket ou pipe é inerentemente sequencial enquanto ler
# dados de um arquivo pode ser feito sequencialmente ou por uma abordagem
# de acesso aleatório.
# Entretanto, seja qual for o fluxo utilizado, eles são cientes do tipo de
# dado que podem processar. Por exemplo, tentar fornecer uma string a um
# fluxo somente-leitura binário levantará um TypeError. Da mesma forma que
# fornecer dados binários para um fluxo de texto etc. Como sugerido por isto,
# existem vários tipos diferentes de fluxos fornecidos pelo módulo io, e alguns
# deles são mostrados na figura fluxos.png.
# -----------------------------------------------------
# IOBase
# Esta é a classe base abstrata para todas as classes de fluxo I/O. A classe
# fornece muitos métodos abstratos que subclasses precisarão implementar.
# A classe IOBase (e suas subclasses) suportam o protocolo iterador. Isto
# significa que um objeto IOBase (ou um objeto de uma subclasse) pode
# iterar pelos dados de entrada do fluxo. IOBase também implementa o
# Protocolo de Gerenciamento de Contexto e, portanto, pode ser usada
# com declarações with e with-as.
# A classe IOBase define um conjunto de métodos e atributos incluindo:
#   * close(): remove e fecha o fluxo.
#   * closed: um atributo indicando se um fluxo está fechado.
#   * flush(): remove o buffer de escrita do fluxo se aplicável.
#   * readable(): retorna True se o fluxo pode ser lido.
#   * readline(size=-1): retorna uma linha do fluxo. Se o tamanho é especificado
#       no máximo 'size' bytes serão lidos.
#   * readline(hint=-1): lê uma lista de linhas. Se o hint é especificado,
#       então é usado para controlar o número de linhas lido.
#   * seek(offset[, whence]): Este método move a posição/ponteiro atual do fluxo
#       para o offset indicado. O significado do offset depende do parâmetro
#       whence. O valor padrão de whence é SEEK_SET.
#       * SEEK_SET ou 0: procura do início do fluxo (o padrão); offset
#       deve ser um número retornado por TextIOBase.tell(), ou zero. qualquer
#       outro valor produz comportamento indefinido.
#       * SEEK_CUR ou 1: procura até a posição atual; offset deve ser zero,
#       que é uma 'não-operação'(todos outros valores não são suportados).
#       * SEEK_END ou 2: procura até o final do fluxo; offset deve ser zero
#       (todos outros valores não são suportados).
#   * seekable(): se o fluxo suporta seek()
#   * tell(): retorna a posição/ponteiro atual do fluxo.
#   * writeable(): retorna True se dados podem ser escritos no fluxo.
#   * writelines(lines): escreve uma lista de linhas para o fluxo.
# --------------------------------------------------
# IO Bruto/Classes IO não-buffer
# IO bruto ou não-buffer IO é fornecido pelas classes RawIOBase e FileIO.
# RawIOBase é uma subclase de IOBase e é a classe base para binário bruto
# (aka não-buffer) I/O. I/O binário bruto tipicamente fornece acesso de baixo
# nível ao dispositivo OS ou API, e não tenta encapsular em primitivos de
# alto-nível(esta é a responsabilidade das classes Buffered I/O  e Text I/O
# que podem encapsular um fluxo I/O bruto). A classe acrescenta métodos como:
#   * read(size=-1): Lê até 'size' bytes do fluxo e os retorna. Se o tamanho
#       não é especificado ou -1, então todos lê todos os bytes disponíveis.
#   * readall(): Lê e retorna todos os bytes disponíveis dentro do fluxo.
#   * readint(b): Lê os bytes no fluxo em um objeto gravável tipo-bytes
#       pré-alocado 'b'(como uma matriz de byte). Retorna o número de bytes lido.
#   * write(b): Escreve os dados fornecidos por 'b'(um objeto tipo-bytes
#       como uma matriz de bytes) no fluxo bruto.
# FileIO representa um fluxo de IO não-buffered binário ligado a um arquivo
# no nível do sistema operacional. Quando a classe FileIO é instanciada,
# pode receber um nome de arquivo e o modo (como 'r' ou 'w'). Também pode
# ser dada uma flag para indicar se o descritor de arquivo associado com o
# arquivo do nível do OS deveria ser fechado ou não. Esta classe é usada para
# a leitura de baixo nível de dados binários e está no centro de todos
# acessos orientados a arquivos(apesar de ser frequentemente encapsulada por
# outro fluxo como um leitor ou escritor com buffer).
# -------------------------------------------
# Classes IO Binário/Buffered IO
# IO Binário, também chamado IO Buffered, é um fluxo de filtro que encapsula
# um fluxo de nível menor RawIOBase(como um fluxo FileIO). Todas as classes que
# implementam IO buffered extendem a classe BufferedIOBase e são:
# BufferedReader: Ao ler dados deste objeto, uma quantidade maior de dados
# pode ser pedida do fluxo bruto, e mantida em um buffer interno. Os dados
# buffered podem, então, ser retornados diretamente em leituras subsequentes.
# BufferedWriter: Ao escrever para este objeto, dados são normalmente
# colocados em um buffer interno. O buffer será escrito do objeto subjacente
# (underlying) RawIOBase sob várias condições, incluindo:
#   * quando o buffer tornar-se muito pequeno para todos os dados pendentes.
#   * quando flush() é chamado.
#   * quando BufferedWriter é fechado ou destruído.
# BufferedRandom: Uma interface buffered combinando dois objetos unidirecionais
# RawIOBase - um legível, o outro gravável- em um único ponto de acesso(endpoint)
# bidirecional.
# Cada uma das classes acima encapsula uma classe fluxo orientada a bytes
# de nível menos como a classe io.FileIO, por exemplo>
# f = io.FileIO('data.dat')
# br = io.BufferedReader(f)
# print(br.read())
# Isto permite que dados na forma de bytes sejam lidos do arquivo 'data.dat'.
# Pode-se ler dados de diferentes fontes, como em um objeto em memória
# BytesIO:
# binary_stream_from_file = io.BufferedReader(io.BytesIO(b'starship.png'))
# bytes = binary_stream_from_file.read(4)
# print(bytes)
# Neste exemplo, os dados são lidos do objeto BytesIO pelo BufferedReader.
# O método read() é, então, usado para ler os primeiros 4 bytes, com a saída:
# b'star'
# Note que 'b' na frente da string e do resultado indica que o literal
# string deveria tornar-se um literal bytes em Python 3. Literais Bytes sempre
# são prefixados por 'b' ou 'B'; eles produzem uma instância do tipo bytes
# em ver do tipo string. Podem conter apenas caracteres ASCII.
# As operações suportadas pelos fluxos buffered incluem, para leitura:
#   * peek(n): retorna até n bytes de dados sem avançar o ponteiro do fluxo.
#       O número de bytes retornado pode ser menor ou maior que requisitado,
#       dependendo da quantidade de dados disponíveis.
#   * read(n): retorna n bytes de dados como bytes, se n não é suportado
#       (ou negativo) então lê todos os dados disponíveis.
#   * readl(n): lê até n bytes de dados usando uma única chamada no fluxo de dados bruto.
# As operações suportadas pelos escritores com buffer incluem:
#   * write(bytes): escreve os dados tipo-bytes e retorna o número de bytes escrito.
#   * flush(): este método força os bytes mantidos no buffer para o fluxo bruto.
# -------------------------------------------------
# Classes de fluxo de texto
# As classes de fluxo de texto são a classe TExtIOBase e suas duas subclasses
# TextIOWrapper e StringIO.
# TextIOBase: É a classe raiz para todas as classe de fluxo de texto. Fornece
# uma interface baseada em caractere e linha ao fluxo I/O. Esta classe
# possui vários métodos adicionais aos definidos em sua classe pai:
#   * read(size=-1): retornará, no máximo, 'size' caracteres do fluxo como
#       uma única string. Se o tamanho é negativo ou None, lerâ todos os dados restantes.
#   * readline(size=-1): retornará uma string representando a linha atual (até
#       uma nova linha ou o final dos dados, o que vier primeiro). Se o fluxo
#       já alcançou o fim do arquivo (EOF), uma string vazia é retornada. Se
#       size é especificado, no máximo 'size' caracteres serão lidos.
#   * seek(offset, [, whence]): altera a posição/ponteiro do fluxo pelo
#       offset especificado. O parâmetro opcional 'whence' indica onde o seek
#       deveria começar:
#       * SEEK_SET ou 0: (o padrão) busca do início do fluxo.
#       * SEEK_CUR ou 1: busca até a posição atual; offset deve ser zero.
#       * SEEK_END ou 2: busca até o final do fluxo; offset deve ser zero.
#   * tell(): Retorna a posição/ponteiro atual do fluxo como um número opaco(opaque)
#       O número não representa, geralmente, um número de bytes no armazenamento binário.(?)
#   * write(s): Este método gravará a string s no fluxo e retornará o núemro de caracteres escritos.
# TextIOWrapper: É um fluxo de texto com buffer que encapsula um fluxo binário
# com buffer e é uma subclasse direta de TextIOBase. Quando um TextIOWrapper
# é criado, há várias opções disponíveis para controlar seu comportamento:

# io.TextIOWrapper(buffer, encoding=None, errors=None, newline=None, line_buffering=False, write_through=False)

# Onde:
#   * buffer é o fluxo binário buffered.
#   * encoding representa a codificação usada no texto como UTF-8.
#   * errors define a política de lidar com erros como 'strict' ou 'ignore'.
#   * newline controla como os finais de linha são resolvidos, por exemplo,
#       se eles deveriam se rignorados(None) ou representados como um 'linefeed',
#       'carriage return' ou 'newline/carriage return' etc.
#   * line_buffering: se True, então flush() é implicado quando uma chamada
#       para escrever contém um caractere de nova linha ou carriage return.
#   * write_through: se True, então uma chamada de write é garantida sem buffer.
# O TextIOWrapper é encapsulado em torno de um fluxo binário com buffer de
# menor nível, por exemplo:
# f = io.FileIO('data.txt')
# br=io.BufferedReader(f)
# text_stream = io.TextIOWrapper(br, 'utf-8')
# StringIO é um fluxo de memória para I/O textual. O valor inicial do
# buffer armazenado pelo objeto StringIO pode ser fornecido quando a
# instância é criada, por exemplo:
# in_memory_text_stream = io.StringIO('to be or not to be that is the question')
# print('in_memory_text_stream', in_memory_text_stream)
# print(in_memory_text_stream.getvalue())
# in_memory_text_stream.close()
# Que gera a saída:
# in_memory_text_stream <_io.StringIO object at 0x10fdfaee8>
# to be or not to be that is the question
# Note que o buffer (representado pela string passada à instância String())
# é descartado quando o método close() é chamado. O método getvalue() retorna
# uma string contendo todos os conteúdos do buffer. Se for chamada após
# o fluxo ser fechado, então gera um erro.
# ---------------------------------------------
# Propriedades de fluxo
# É possível consultar um fluxo para determinar que tipos de operações ele
# suporta. Isto pode ser feito com readable(), seekable() e writable().
# Por exemplo:
# import io

# f = io.FileIO("myfile.txt")
# br = io.BufferedReader(f)
# text_stream = io.TextIOWrapper(br, encoding="utf-8")
# print("text_stream", text_stream)
# print("text_stream.readable()", text_stream.readable())
# print("text_stream.seekable(()", text_stream.seekable())
# print("text_stream.writable()", text_stream.writable())

# text_stream.close()
# -------------------------------------------
# Fechando fluxos
# Todos os fluxos abertos devem ser fechados. Entretanto, você pode fechar o
# fluxo de nível mais alto e isto fechará automaticamente fluxos de níveis menores, por exemplo:
# import io

# f = io.FileIO("myfile.txt")
# br = io.BufferedReader(f)
# text_stream = io.TextIOWrapper(br, "utf-8")
# print(text_stream.read())
# text_stream.close()
# --------------------------------------------
# Retornando à função open()
# A função open(assim como io.open()) ambas retornam um objeto fluxo. O
# tipo real do objeto retornado depende do modo de arquivo especificado,
# se buffering está sendo usado etc. Por exemplo:
# import io

# # Fluxo textual
# f1 = open("myfile.txt", mode="r", encoding="utf-8")
# print(f1)
# # Fluxo binário(Buffered IO)
# f2 = open("myfile.txt", mode="rb")
# print(f2)
# f3 = open("myfile.txt", mode="wb")
# print(f3)
# # IO Bruto(Unbuffered IO)
# f4 = open("starship.png", mode="rb", buffering=0)
# print(f4)

# A saída desse exemplo é:
# <_io.TextIOWrapper name='myfile.txt' mode='r' encoding='utf-8'>
# <_io.BufferedReader name='myfile.txt'>
# <_io.BufferedWriter name='myfile.txt'>
# <_io.FileIO name='starship.png' mode='rb' closefd=True>

# Como pode ver da saída, 4 tipos diferentes de objeto foram retornados
# da função open(). Eles refletem a diferença nos parâmetros passados
# para a função open(). Por exemplo, f1 referencia io.TextIOWrapper pois
# deve codificar(converter) o texto de entrada para Unicos usando UTF-8.
# f2 armazena um io.BufferedReader pois o modo indica que queremos ler
# dados binários e f3 um io.BufferedWriter pois queremos escrever. A chamada
# final retorna FileIO pois indicados que não queremos usar buffer para os dados.
# Em geral, as seguintes regras são aplicadas para determinar o tipo de
# objeto retornado baseado nos modos e codificação especificados:

# Classe         | modo                  | Buffering
# FileIO         | binário               | não
# BufferedReader | 'rb'                  | sim
# BufferedWriter | 'wb'                  | sim
# BufferedRandom | 'rb+', 'wb+', 'ab+'   | sim
# TextIOWrapper  | qualquer texto        | sim

# Note que nem todas as combinações de modo fazem sentido e, assim, algumas
# combinações irão gerar um erro.
# Em geral, não é necessário se preocupar sobre qual fluxo estará usando
# ou o que aquele fluxo faz.
# Entretanto, é útil entender as implicações do que você está fazendo para
# tomar escolhas melhor informadas. Por exemplo, fluxos binários são mais
# rápidos que fluxos orientados a Unicode que precisam converter ASCII para Unicode.
# Além disso, entender o papel de fluxos na entrada e saída pode permitir
# alterar a fonte e destino de dados sem precisar reescrever toda a aplicação.
# Assim, pode-se usar um arquivo ou stdin para testar um socket ou ler dados
# em produção.
