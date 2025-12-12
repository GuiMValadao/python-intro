# Capítulo 20 - Trabalhando com arquivos CSV
# O formato CSV (Comma Separated Values/Valores Separados por Vírgulas) é o
# formato mais comum de exportação de planilhas e bases de dados. Entretanto,
# CSV não é um padrão preciso, com múltiplas aplicações tendo convenções
# diferentes e padrões específicos. O módulo csv de Python implementa classes
# para ler e escrever dados tabulares no formato CSV. Como parte disso,
# suporta o conceito de um dialeto que é um formato CSV usado por uma
# aplicação ou suíte de programas específico, por exemplo, suporta um dialeto
# Excel. Isto permite que programadores digam 'escreva esses dados no formato
# preferido pelo Excel', ou 'leia dados deste arquivo que foi gerado pelo Excel'
# sem saber os detalhes precisos do formato CSV usado pelo EXcel.
# Programadores também podem descrever os dialetos CSV entendidos por
# outras aplicações ou definier seus próprios dialetos CSV com propósitos-especiais.
# O módulo csv tem diversas funções, entre elas:
#   * csv.reader (csvfile, dialect='excel', **fmtparams): Retorna um objeto
#       leitor que iterará sobre linhas no arquivo csv dado. Um parânetro
#       de dialeto opcional pode ser dado. Ele pode ser uma instância de uma
#       subclasse da classe Dialect ou uma das strings retornadas pela função
#       list_dialects(). Os outros argumentos de palavra-chave opcionais fmtparams
#       podem ser dados para sobrescrever parâmetros de formtação individuais
#       no dialeto atual.
#   * csv.writer(csvfile, dialect='excel', **fmtparams): Retorna um objeto
#       escritor responsável por converter os dados do usuário em strings
#       delimitadas no arquivo csv fornecido. Um parâmetro opcional dialect
#       pode ser dado. fmtparams podem ser dados para sobrescrever parâmetros
#       de formatação individuais no dialeto atual.
#   * csv.list_dialects(): Retorna os nomes de todos os dialetos registrados.
#       Por exemplo, em um MacOS X, a lista padrão de dialetos é ['excel',
#       'excel-tab', 'unix'].
# ---------------------------------------
# A classe CSV Writer
# O escritor CSV é obtido da função csv.writer(). O csvwriter suporta dois
# métodos usados para escrever dados em um arquivo CSV:
#   * csvwriter.writerow(row): escreve o parâmetro 'row' no objeto arquivo
#       do escritor, formatado de acordo com o dialeto atual.
#   * csvwriter.writerows(rows): Escreve todos os elementos em linhas (um iterável
#       de objetos linha como descrito acima) no objeto arquivo do escritor,
#       formatado de acordo com o dialeto atual.
# Objetos escritores também tem o seguinte atributo público:
#   * csvwriter.dialect: uma descrição somente-leitura do dialeto em uso pelo escritor.
# O seguinte programa ilusta um uso simples do módulo csv que cria um arquivo
# chamado sample.csv. Como não especificamos um dialeto, o padrão 'excel' será usado.
# O método writerow() é usado para escrever cada lista separada po vírgulas
# de strings no arquivo CSV:
# import csv

# print("Criando arquivo CSV")
# with open("sample.csv", "w", newline="") as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(["She Loves You", "Sept 1963"])
#     writer.writerow(["I Want to Hold Your Hand", "Dec 1963"])
#     writer.writerow(["Cant Buy Me Love", "Apr 1964"])
#     writer.writerow(["A Hard Days Night", "July 1964"])

# ----------------------------------------
# A classe CSV Reader
# Um objeto CSV Reader é obtido da função csv.reader(). Ele implementa o protocolo
# iteração. Se um objeto csv é usado com um loop for, então cada loop completo
# fornece a próxima linha do arquivo CSV como uma lista, analisada conforme
# o dialeto CSV atual.
# Objetos leitores também tem os seguintes atributos públicos:
#   * csvreader.dialect: Uma descrição somente-leitura do dialeto em uso.
#   * csvreader.line_num: O número de linhas lidas do iterador fonte.
#       Ele não é o mesmo que o número de gravações retornados, pois gravações
#       podem ocupar múltiplas linhas.
# O seguinte código fornece um exemplo muito simples de leitura de um arquivo
# CSV usando um objeto leitor de csv:
# import csv

# print("Iniciando leitura do arquivo csv")
# with open("sample.csv", "r", newline="") as arquivocsv:
#     leitor = csv.reader(arquivocsv)
#     for linha in leitor:
#         print(*linha, sep=", ")
# print("Leitura finalizada")
# ---------------------------------
# A classe CSV DictWriter
# Em muitos casos, a primeira linha de um arquivo CSV contém um grupo de nomes
# (ou chaves) que definem os campos dentro do resto do CSV. Isto é, a primeira
# linha fornece significado às colunas e aos dados armazenados no resto do
# arquivo CSV. Portanto, é bastante útil capturar esta informação e estruturar
# os dados escritos em um arquivo CSV ou carregados de um arquivo CSV baseado
# nas chaves da primeira linha.
# O csv.DictWriter retorna um objeto que pode ser usado para escrever valores
# no arquivo CSV baseado no uso de tais colunas nomeadas. O arquivo a ser usado
# com o DictWriter é fornecido quando a classe é instanciada.
# import csv

# with open("names.csv", "w", newline="") as arquivocsv:
#     nomecolunas = ["primeiro_nome", "ultimo_nome", "resultado"]
#     escritor = csv.DictWriter(arquivocsv, fieldnames=nomecolunas)
#     escritor.writeheader()
#     escritor.writerow(
#         {"primeiro_nome": "John", "ultimo_nome": "Smith", "resultado": 54}
#     )
#     escritor.writerow(
#         {"primeiro_nome": "Jane", "ultimo_nome": "Lewis", "resultado": 63}
#     )
#     escritor.writerow(
#         {"primeiro_nome": "Chris", "ultimo_nome": "Davies", "resultado": 72}
#     )

# Note que quando DictWriter é criado, uma lista de chaves deve ser fornecida
# que será usada para nomear as colunas do arquivo csv. O método writeheader()
# é, então, usado para escrever a linha de cabeçalho no arquivo CSV. O método
# writerow() pega um objeto dicionário que tem chaves baseadas nas definidas
# para o DictWriter. Elas são, então, usadas para escrever dados no CSV.
# ---------------------------------------------------------------------
# A classe CSV DictReader
# O arquivo a ser usado com DictReader é fornecido quando a classe é instanciada.
# Assim como com a DictWriter, DictReader pega uma lista de chaves usadas para
# definir as colunas do arquivo CSV. Os cabeçalhos a serem usados para a
# primeira linha podem ser fornecidos, mas são opcionais (se um conjunto de
# chaves não é fornecido, então os valores na primeira linha do arquivo CSV
# será usado como fieldnames).
# A classe DictReader fornece vários recursos úteis, incluindo a propriedade
# fieldnames que contém uma lista das chaves/cabeçalhos do arquivo CSV
# definidos pela primeira linha do arquivo. A classe DictReader também implementa
# o protocolo iterador e, assim, pode ser usada em um loop for no qual cada
# linha (após a primeira) é retornada em sequência como um dicionário. O objeto
# dicionário representando cada linha pode, então, ser usado para acessar o valor
# de cada coluna baseado nas chaves definidas na primeira linha.
# import csv

# print("Iniciando leitura do dict CSV de exemplo")
# with open("names.csv", newline="") as arquivocsv:
#     leitor = csv.DictReader(arquivocsv)
#     for cabecalho in leitor.fieldnames:
#         print(cabecalho, end=" ")
#     print("\n-----------------------------------")
#     for linha in leitor:
#         print(linha["primeiro_nome"], linha["ultimo_nome"], linha["resultado"])
# print("Pronto")
