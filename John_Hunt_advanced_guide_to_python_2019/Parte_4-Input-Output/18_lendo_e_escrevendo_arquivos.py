# Capítulo 18 - Leitura e escrita de arquivos
# Ler de, e escrever em, arquivos de testo em Python é bem direto. A função
# embutida open() cria um objeto arquivo no qual pode-se ler e/ou escrever
# dados de e/ou para um arquivo.
# A função exige no mínimo o nome do arquivo com que irá trabalhar. Opcionalmente,
# você pode especificar o modo de acesso (read, write, append etc). Se não
# especificar, então o arquivo será aberto apenas em modo escrita. Também
# pode especificar se quer que as interações com o arquivo sejam buffered,
# que pode melhorar o desempenho agrupando leituras de dados juntas.
# A sintaxe para a função open() é:
# file_object = open(file_name, acess_mode, buffering)
#   * file_name indica o arquivo a ser acessado
#   * acess_mode determina o modo com que o arquivo deve ser aberto,
#       isto é, leitura, escrita, edição, etc. Uma lista complea de valores
#       possíveis é dada na tabela abaixo. Este parâmetro é opcional, e o
#       valor padrão é r(leitura).
# Modo   |   Descrição
# -------|-----------------------------------------------------
# r      | Abre um arquivo somente para leitura. Inicia no começo do arquivo.
# rb     | Leitura no formato binário. Inicia no começo do arquivo.
# r+     | Leitura e escrita. Inicia no começo do arquivo.
# rb+    | Leitura e escrita no formato binário. Inicia no começo do arquivo.
# w      | Apenas escrita. Sobrescreve o arquivo se já existir ou cria um novo se não.
# wb     | Escrita no formato binário. Sobrescreve se já existir, cria um novo se não.
# w+     | Escrita e leitura. Sobrescreve se existe, cria um novo se não.#
# wb+    | Escrita e leitura em binário. Sobrescreve se existe, cria um novo se não.
# a      | Abre um arquivo para edição. Inicia no final do arquivo se o arquivo existe, cria um novo se não.
# ab     | Abre um arquivo para edição em formato binário. Inicia no fim do arquivo ou cria um novo se não existe.
# a+     | Abre um arquivo para edição e leitura. Inicia no fim do arquivo, ou cria um novo se não existe.
# ab+    | Edição e leitura em binário. Inicia no fim se existe, cria um novo se não.
# -------------------------------------------------------------------------------------------------
# O objeto arquivo em si tem vários atributos úteis como:
#   * file.closed retorna True se o arquivo foi fechado(não pode mais ser acessado
#       pois o método close() foi chamado nele)
#   * file.mode retorna o modo de acesso com que o arquivo foi aberto
#   * file.name é o nome do arquivo.
# O método file.close() é usado para fechar o arquivo após finalizar sua
# utilização. Ele eliminará informações que não foram escritas no arquivo
# e fechará a referência do objeto do arquivo no sistema de arquivos em operação.
# Isto é importante ser feito pois deixar referências a um arquivo abertas pode
# causar problemas em aplicações maiores pois tipicamente haverá apenas
# um certo número de referências possíveis simultaneamente e, sobre um periodo
# longo de tempo, elas podem ser todas ocupadas, resultando em futuros erros
# sendo lançados pois arquivos não podem mais ser abertos.
# A seguinte seção de código ilustra essas ideias:

##############################
# file = open("myfile.txt", "w+")
# print("file.name: ", file.name)
# print("file.closed: ", file.closed)
# print("file.mode: ", file.mode)
# file.close()
# print("file.closed now: ", file.closed)
##############################
# Que tem a saída:
# file.name:  myfile.txt
# file.closed:  False
# file.mode:  w+
# file.closed now:  True
# ---------------------------------------------
# Lendo arquivos
# A leitura de texto de um arquivo é suportada pelos métodos read(), readline()
# e readlines():
#   * read() retornará o conteúdo inteiro de um arquivo como uma única string.
#   * readline() lê a próxima linha de texto de um arquivo. Retorna todo
#       o text de uma linha até, e incluindo, o caractere de nova linha. Pode
#       ser usado para ler um arquivo uma linha por vez.
#   * readlines() retorna uma lista de todas as linhas em um arquivo, onde cada
#       item da lista representa uma única linha.
# Note que, após ler algum texto de um arquivo usando uma das operações acima,
# aquela linha não será lida novamente. Assim, usar readlines() resultaria
# nos próximos readlines retornando uma lista vazia independente do conteúdo
# do arquivo.
# O seguinte ilustra a utilização de readlines() para ler todo o texto em
# um arquivo de texto em um programa e então exibir uma linha de cada vez:
# file = open("myfile.txt", "r")
# lines = file.readlines()
# for line in lines:
#     print(line, end="")
# file.close()
# Note que no loop 'for' indicamos para a função print terminar a linha
# com '' em vez de \n pois a string da linha já possui o caractere de
# nova linha que estava no arquivo.
# --------------------------------------------------
# Iteração dos conteúdos de um arquivo
# Como sugerido no exemplo anterior, é muito comum querer processar os
# conteúdos de um arquivo uma linha de cada vez. De fatoo, Python torna isso
# muito fácil fazendo que o objeto arquivo suporte iteração. A iteração de
# arquivo acessa cada linha no arquivo e disponibiliza aquela linha ao
# loop for. Podemos escrever:
# file = open("myfile.txt", "r")
# for line in file:
#     print(line, end="")
# file.close()
# Também é possível usar list comprehension para fornecer um jeito conciso
# de carregar e processar linhas em um arquivo em uma lista. É similar ao efeito
# de readlines(), mas agora somos capazes de preprocessar os dados antes de
# criar a lista:
# file = open("myfile.txt", "r")
# lines = [line.upper() for line in file]
# file.close()
# print(lines)
# --------------------------------------------------
# Escrevendo dados em arquivos
# Escrever uma string em um arquivo pode ser feito pelo método write().
# Claro, o objeto arquivo que criamos deve ter um modo de acesso que
# permite a escreita(como 'w'). Note que o método write NÃO adiciona um
# caractere de nova linha('\n') ao final da string - deve-se fazer isso manualmente.
# print("Escrevendo no arquivo")
# f = open("myfile.txt", "w")
# f.write("Olá do Python!\n")
# f.write("Trabalhar com arquivos é fácil...\n")
# f.write("É divertido...\n")
# f.close()
# ------------------------------------------------------
# Usando arquivos e declarações with
# Assim como vários outros tipos onde é importante desativar recursos,
# o objeto da classe arquivo implemente o Protocolo Gerenciador de Contexto
# e pode ser usado com a declaração with. Assim, é comum escrever código que
# abrirá um arquivo usando a estrutura with as, garantindo assim que o arquivo
# fechará quando o bloco de código terminar, por exemplo:
# with open("myfile.txt", "r") as f:
#     lines = f.readlines()
#     for line in lines:
#         print(line, end="")
# -------------------------------------------------------
# O módulo Fileinput
# Em algumas situações, você pode precisar ler a entrada de diversos arquivos
# de uma só vez. Poderia fazer isso abrindo cada arquivo independentemente,
# lendo os conteúdos e anexando em uma lista. Entretanto, isto é tão comum
# que o módulo fileinput fornece uma função fileinput.input() que pode pegar
# uma lista de arquivos e tratar todos os arquivos como uma única entrada,
# simplificando o processo significativamente, por exemplo:
# import fileinput
# with fileinput.input(files=('spam.txt', 'eggs.txt')) as f:
#     for line in f:
#         process(line)
# Recursos fornecidos pelo módulo fileinput incluem:
#   * Retornar o nome do arquivo sendo lido no momento
#   * Retornar o inteiro 'descritor do arquivo' para o arquivo atual
#   * Retornar o número cumulativo da linha que acabou de ser lida
#   * Retornar o número da linha no arquivo atual. Antes de ler a primeira linha, retorna 0.
#   * Uma função booleana que indica se a linha atual que acabou de ser lida é a primeira do arquivo.
# Alguns desses são ilustrados abaixo:
# with fileinput.input(files=("textfile1.txt", "textfile2.txt")) as f:
#     lie = f.readline()
#     print("f.filename():", f.filename())
#     print("f.isfirstline():", f.isfirstline())
#     print("f.filelineno():", f.filelineno())
#     for line in f:
#         print(line, end="")
# ---------------------------------------------
# Renomeando arquivos
# Um arquivo pode ser renomeado usando a função os.rename(). Esta função pega
# dois argumentos, o nome atual do arquivo e o novo nome. É parte do módulo
# de Python os que fornece métodos que podem ser usados para realizar diversas
# operações de processamento de arquivos (como renomear).
# import os
# os.rename('myfileoriginalname.txt', 'myfilenewname.txt')
# -----------------------------------------------
# Excluindo arquivos
# Um arquivo pode ser excluído usando o método os.remove(). Ele deleta
# o arquivo especificado pelo nome passado.
# import os
# os.remove('somefilename.txt')
# --------------------------------------------
# Arquivos de acesso aleatório
# Todos os exemplos até aqui sugeriram que os arquivos são acessados
# sequencialmente, com a primeira linha lida antes da segunda e assim por
# diante. Apesar disto ser a abordagem mais comum, não é a única; também
# pode-se usar uma abordagem de acesso aleatório aos conteúdos dentro de
# um arquivo.
# Para entender a ideia de acesso a arquivos aleatório, é útil entender que
# podemos manter um ponteiro(pointer) em um arquivo para indicar onde estamos
# naquele arquivo em termo de leitura ou escrita de dados. Antes de qualquer
# coisa ser lida de um arquivo, o ponteiro está antes do início do arquivo
# e ler a primeira linha do texto, por exemplo, avançaria o ponteiro para o
# início da segunda linha etc.
# Ao acessar os conteúdos de um arquivo aleatoriamente, o programador move
# o ponteiro manualmente ao local requerido e lê ou escreve texto relativo
# àquele ponteiro. Isto significa que eles podem mover pelo arquivo lendo
# e escrevendo dados. O aspecto de acesso aleatório é fornecido pelo método
# seed do objeto do arquivo:
# file.seek(offset, whence): este método determina onde a próxima operação
# de leitura ou escrita ocorre.
# O parâmetro 'offset' indica a posição do ponteiro read/write dentro do
# arquivo. O movimento também pode ser para frente ou para trás (representado
# por um offset negativo). O parâmetro opcional whence indica a posição à qual
# o offset é relativo. Os valores usados para whence são:
#   * 0 indica que o offset é relativo ao início do arquivo (padrão)
#   * 1 significa que o offset é relativo à posição atual do ponteiro.
#   * 2 indica que o offset é relativo ao fim do arquivo.
# Por exemplo, no seguinte código de exemplo, criamos um novo arquivo de texto
# e escrevemos um conjunto de caracteres naquele arquivo. Neste ponto, o
# ponteiro está posicionado após o 'z' no arquivo. Entretanto, usamos seek()
# para mover o ponteiro para o 10° caractere no arquivo, e agora escrevemos
# 'Hello', reposicionamos o ponteiro para o 6° caractere e escrevemos 'BOO'.
# Então fechamos o arquivo. Por fim, lemos todas as linhas do arquivo usando
# a declaração with as e a função open(), e disto vemos que o texto no arquivo
# é, agora, abcdefBOOjHELLOpqrstuvwxyz.
# f = open("text.txt", "w+")
# f.write("abcdefghijklmnopqrstuvwxyz\n")
# f.seek(10, 0)
# f.write("HELLO")
# f.seek(6, 0)
# f.write("BOO")
# f.close()
# with open("text.txt", "r") as f:
#     for line in f:
#         print(line, end="")
# ---------------------------------------------
# Pastas
# O módulo os tem várias funções que podem ajudar com a criação, remoção e
# alteração de pastas. Elas incluem:
#   * mkdir(): usada para criar uma pasta, pega o nome da pasta a ser criada
#       como parâmetro. Se a pasta já existe, FileExistsError é levantada.
#   * chdir(): Pode ser usada para mudar o diretório de trabalho atual. É a
#       pasta na qual a aplicação lerá de/escreverá em por padrão.
#   * getcwd(): Retorna uma string representando o nomde do diretório de trabalho atual.
#   * rmdir(): Remove/exclui uma pasta. Pega o nome da pasta para ser excluída como parâmetro.
#   * listdir(): Esta função retorna uma lista contendo os nomes das entradas
#       na pasta especificada como parâmetro à função(se não for dado um nome,
#       será usada a pasta de trabalho atual).
# Um exemplo simples ilustra algumas as funções:

####################################3
# import os

# print("os.getcwd():", os.getcwd())
# print("Lista de conteúdos da pasta")
# print(os.listdir())
# print("Criar pasta")
# os.mkdir("mydir")
# print("Lista os conteúdos atualizados da pasta")
# print(os.listdir())
# print("Muda para dentro da pasta mydir")
# os.chdir("mydir")
# print("os.getcwd():", os.getcwd())
# print("Retorna para a pasta pai")
# os.chdir("..")
# print("os.getcwd():", os.getcwd())
# print("Remove pasta mydir")
# os.rmdir("mydir")
# print("List os conteúdos resultantes na pasta")
# print(os.listdir())
####################################
# Note que '..' é atalho para a pasta pai da pasta atual e '.' é atalho da pasta atual.
# ------------------------------------------------
# Arquivos temporários
# Durante a execução de muitas aplicações pode ser necessário criar um arquivo
# temporário que será criado em um momento e deletado antes do fim da aplicação.
# É possível, claro, gerenciar esses arquivos temporários você mesmo, mas o
# módulo tempfile fornece vários recursos para simplificar a criação e gerenciamento
# desses arquivos temporários.
# Dentro do módulo tempfile, TemporaryFile, NamedTemporaryFile, TemporaryDirectory,
# e SpooledTemporaryFile são objetos de arquivo de alto nível que fornecem
# limpeza automática de arquivos e pastas temporários. Estes objetos implementam
# o Protocolo Gerenciador de Contexto.
# O módulo tempfile também fornece função de nível menor mkstemp() e mkdtemp()
# que podem ser usadas para criar arquivos temporários que requerem que o
# desenvolvedor gerencie-os e delete-os no momento apropriado.
# Os recursos de alto-nível do módulo tempfile são:
#   * TemporaryFile(mode='w+b'): Retorna um objeto anonimo tipo-arquivo que
#       pode ser usado como área de armazenamento temporária. Ao final do
#       contecto gerenciado (via declaração with) ou destruição do objeto
#       do arquivo, o arquivo temporário será removido do sistema de arquivos.
#       Note que, por padrão, todos os dados são escritos no arquivo temporário
#       em binário, que é, geralmente, mais efeiciente.
#   * NamedTemporaryFile(mode='w+b'): Esta função opera exatamente como
#       TemporaryFile(), exceto que nesse caso o arquivo temporário tem um
#       nome visível no sistema de arquivos.
#   * SpooledTemporaryFile(max_size=0, mode='w+b'): Esta função opera exatamente
#       como TemporaryFile(), exceto que os dados são armazenados na memória
#       até o tamanho do arquivo exceder max_size, ou até o método fileno()
#       é chamado, quando os conteúdos são escritos em disco e a operação procede
#       similar a TemporaryFile().
#   * TemporaryDirectory(suffix=None, prefix=None, dir=None): Esta função cria
#       uma pasta temporária. Ao fim do contexto ou destruição do objeto da
#       pasta temporária, a pasta temporária criada e todos os seus conteúdos são
#       removidos do sistema.
# As funções de nível menor incluem:
#   * mkstemp(): Cria um arquivo temporário que é apenas legível ou gravável
#       pelo usuário que o criou.
#   * mkdtemp(): Cria uma pasta temporária. A pasta é legível, gravável e
#       buscável apena pelo ID do usuário que a criou.
#   * gettempdir(): Retorna o nome da pasta usada para arquivos temporários.
#       Isto define o valor padrão para a pasta temporária padrão a ser usada
#       com as outras funções do módulo.
# Um exemplo da utilização de TemporaryFile é mostrado abaixo. Este código importa
# o módulo tempfile e então exibe a pasta padrão usada para arquivos temporários.
# Então cria um objeto TemporaryFile e exibe seu nome e modo (o modo padrão
# é binário, mas, por exemplo, sobrescrevemos isto para usar texto simples).
# Então, escrevemos uma linha no arquivo. Usando seek, nos reposicionamos no
# início do arquivo e então lemos a linha que acabamos de escrever.
# import tempfile

# print("tempfile.gettempdir():", tempfile.gettempdir())
# temp = tempfile.TemporaryFile("w+")
# print("temp.name:", temp.name)
# print("temp.mode", temp.mode)
# temp.write("Ola mundo!")
# temp.seek(0)
# line = temp.readline()
# print("line:", line)

# tempfile.gettempdir(): C:\Users\guimv\AppData\Local\Temp
# temp.name: C:\Users\guimv\AppData\Local\Temp\tmp_lgv4qam
# temp.mode w+
# line: Ola mundo!

# ---------------------------------------------
# Trabalhando com caminhos
# O módulo pathlib fornece um conjunto de classes representando caminhos
# do sistema de arquivos; isto é, caminhos através da hierarquia de pastas
# e arquivos dentro da estrutura operacional do sistema de arquivos. Foi introduzida
# com Python 3.4. A classe central desse módulo é a classe Path.
# Um objeto Path é útil pois fornece operações que lhe permitem manipular e
# gerenciar o caminho de um arquivo ou pasta. A classe Path também replica
# algumas das operações disponíveis no módulo os(como mkdir, rename e rmdir)
# que significa que não precisamos trabalhar diretamente com o módulo os.
# Um objeto de caminho é criado usando a função construtora Path; esta função
# retorna um tipo específico de Path dependendo do tipo de sistema operacional
# em uso, como WindowsPath ou PosixPath. O construtor Path() pega o caminho
# para criar, por exemplo 'D:/mydir'(em Windows), '/Users/user1/mydir' (em Mac)
# ou 'var/temp' em Linux etc.
# Pode, então, usar vários métodos diferentes no objeto Path para obter informação
# sobre o caminho como:
#   * exists(): retorna True ou False dependendo em se o caminho aponta para
#       uma pasta ou arquivo existentes.
#   * is_dir(): retorna True se o caminho aponta para uma pasta e False se
#       referencia um caminho. Também retorna False se o caminho não existe.
#   * is_file(): retorna True se aponta um arquivo, False se uma pasta ou
#       é um caminho inexistente.
#   * absolute(): Um objeto Path é considerado absoluto se tem tanto uma raiz
#       e(se apropriato) um drive.
#   * is_absolute(): Retorna um Booleano indicando se o Path é absoluto ou não.
# from pathlib import Path

# print("Create Path object for current directory")
# p = Path(".")
# print("p:", p)
# print("p.exists():", p.exists())
# print("p.is_dir():", p.is_dir())
# print("p.is_file():", p.is_file())
# print("p.absolute():", p.absolute())
# Que tem a saída:
# Create Path object for current directory
# p: .
# p.exists(): True
# p.is_dir(): True
# p.is_file(): False
# p.absolute(): D:\programacao\python-intro

# Também tem vários métodos na classe Path que podem ser usados para criar
# e remover pastas e arquivos como:
#   * mkdir()
#   * rmdir(): remove a pasta; a paste deve estar vazia.
#   * rename(alvo): renomeia o arquivo ou pasta com o nome alvo.
#   * unlink(): remove o arquivo referenciado pelo objeto caminho.
#   * joinpath(*other): acrescenta elementos ao objeto path, ex path.joinpath('/temp')
#   * with_name(new_name): retorna um novo objeto caminho com o nome alterado.
#   * O operador '/' também pode ser usado para criar novos objetos caminho
#       a partir de caminhos existentes, por exemplo path/'test'/'output'
#       que iria acrescentar as pastas test e ouput ao objeto caminho.
# Dois métodos da classe Path podem ser usados para obter objetos caminho
# representando pastas chave como a pasta atual e a pasta home do usuário
# executando o programa.
#   * Path.cwd()
#   * Path.home()
# Um exemplo de usar várias das funções acima é dado abaixo. Este exemplo obtém
# um objeto caminho representando a pasta atual e então acrescenta 'text' a ele.
# O caminho resultante é, então, checado para verificar se o caminho existe,
# assumindo que o caminho não exista, ele é criado e o método exists() é reexecutado.
# from pathlib import Path

# p = Path.cwd()
# print("Prepara uma nova pasta")
# newdir = p / "test"
# print("Checa se newdir existe")
# print("newdir.exists():", newdir.exists())
# print("Cria nova pasta")
# newdir.mkdir()
# print("newdir.exists():", newdir.exists())
# newdir.rmdir()

# que tem a saída:
# Prepara uma nova pasta
# Checa se newdir existe
# newdir.exists(): False
# Cria nova pasta
# newdir.exists(): True


# Um método bastante útil no objeto Path é o método glob(pattern). Este método
# retorna todos os elementos dentro do caminho que cumprem o padrão especificado.
# Por exemplo, path.glob('*.py') retornará todos os arquivos terminando em
# .py dentro do caminho atual. Note que '**/*.py' indicaria a pasta atual e
# qualquer subpasta.
# Caminhos que referenciam um arquivo também podem ser usados para ler e escrever
# dados naquele arquivo. Por exemplo, o método open() pode ser usado para
# abrir um arquivo que, por padrão, permite que um arquivo seja lido:
#   * open(mode='r): pode ser usado para abrir o arquivo referenciado pelo objeto caminho.
# Isto é usado abaixo para ler os conteúdos de um arquivo uma linha de cada vez:
# from pathlib import Path

# p = Path("myfile.txt")
# with p.open() as f:
#     for line in f:
#         print(line, end="")
# Entretanto, também existem alguns métodos de alto níveis disponíveis que lhe
# permitem facilmente escrever dados em um arquivos ou ler dados de um arquivo.
# Eles incluem os métodos Path write_text e read_text:
#   * write_text(dado): abre o arquivo apontado no modo texto e escreve dados
#       nele, então fechando-o.
#   * read_text(): abre o arquivo em modo leitura, lê o texto e fecha o arquivo;
#       então retorna os conteúdos do arquivo como uma string.
