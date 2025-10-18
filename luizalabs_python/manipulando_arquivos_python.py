
#Exemplo

#file = open("example.txt", "r")
# ... fazemos algo com o arquivo
#file.close()

# Existem diferentes modos de abrir um arquivo: r(leitura), w(gravação/escrita) 
# ou a(anexar)
######LEITURA-DE-ARQUIVOS##########
# Para ler um arquivo pode-se usar read(), readline() ou readlines().
#file = open('D:/programacao/python-intro/luizalabs_python/algum_arquivo.txt', 'r')      # cuidado com a barra(\), tem que usar /; 
#print(arquivo.read())
#print(arquivo.readline())
#print(arquivo.readlines())
#while len(linha := file.readline()):    # := atribuição, atribui cada linha a uma variável linha e a exibe; len vai contar as linhas, se for 0 torna o argumento de while false, encerrando o loop.
#    print(linha)
#file.close()
# readline() lê uma linha por vez e readlines() retorna uma lista onde
# cada linha é um elemento da lista.

######ESCRITA-DE-ARQUIVOS##########
# Pode-se usar write() ou writelines() para escrever em um arquivo.
#file = open('D:/programacao/python-intro/luizalabs_python/teste_escrita.txt', 'w')
#file.write('Olá, mundo!')
#file.writelines(['\n', 'Python','\n' 'escrevendo','\n', 'em ', 'um ', 'texto'])
#file.close()

#file = open('D:/programacao/python-intro/luizalabs_python/teste_escrita.txt', 'r') 
#while len(linha := file.readline()):    # := atribuição, atribui cada linha a uma variável linha e a exibe; len vai contar as linhas, se for 0 torna o argumento de while false, encerrando o loop.
#    print(linha)
#file.close()

######GERENCIAR-ARQUIVOS-E-DIRETÓRIOS##########
# Pode-se criar, renomear e excluir arquivos e diretórios com os módulos
# 'os' e 'shutil'.
#import os
#import shutil
#from pathlib import Path    # Para definir o caminho
# Criar um diretório


#ROOT_PATH = Path(__file__).parent
# __file__ retorna o caminho do arquivo no qual o código se encontra,
#print(ROOT_PATH.parent)
# ROOT_PATH.parent remove o arquivo do caminho, retornando a pasta em que o arquivo se encontra.

#os.mkdir(ROOT_PATH /'nova-pasta')

#arquivo = open(ROOT_PATH / 'novo.txt', 'w')
#arquivo.close()

# Renomear um arquivo
#os.rename(ROOT_PATH / 'novo.txt', ROOT_PATH /'trocado.txt')
#arquivo.close()

# Remover um arquivo
#os.remove(ROOT_PATH /'nova-pasta/novo.txt')

# Mover um arquivo
#shutil.move(ROOT_PATH/'novo.txt', ROOT_PATH/'nova-pasta'/'novo.txt')

######BOAS-PRÁTICAS-NA-MANIPULACÃO DE ARQUIVOS##########

#from pathlib import Path

#ROOT_PATH = Path(__file__).parent

# Automatizar o fechamento do arquivo:
#with open(ROOT_PATH / 'teste_escrita.txt', 'r') as arquivo:
#    print(arquivo.readline())
#print(arquivo.readline())


# Verificar se o arquivo foi aberto com sucesso:
#try:
#    with open(ROOT_PATH / 'teste_escrit.txt', 'r') as arquivo:
#        print(arquivo.readline())
# except IOError as exc:
#    print(f'Erro ao abrir o arquivo: {exc}')

# Usar a codificação correta. O argumento 'encoding' de open() permite especificá-la
# try:
#     with open(ROOT_PATH / 'teste_utf-8.txt', 'w', encoding='utf-8') as arquivo:
#         arquivo.write('Aprendendo a manipülar arquivos em Python')
# except IOError as exc:
#     print(f'Erro ao abrir o arquivo: {exc}')
# try:
#     with open(ROOT_PATH / 'teste_utf-8.txt', 'r', encoding='utf-8') as arquivo:
#         print(arquivo.read())
# except IOError as exc:
#     print(f'Erro ao abrir o arquivo: {exc}')
# except UnicodeDecodeError as exc:
#     print(f'Caractere indevido encontrado: {exc}')
#
#
######TRABALHANDO-COM-ARQUIVOS-CSV##########
import csv
from pathlib import Path
ROOT_PATH = Path(__file__).parent

# Criação e escrita de arquivo .csv
# try:
    # with open(ROOT_PATH/'usuarios.csv', 'w', encoding='utf-8', newline='') as arquivo:
        # escritor = csv.writer(arquivo)
        # escritor.writerow(['id', 'Nome'])
        # escritor.writerow(['1', 'João'])
        # escritor.writerow(['2', 'Gui'])
# except IOError as exc:
    # print(f'Erro ao criar o arquivo: {exc}')
# 
# Leitura de arquivo .csv
# try:
    # with open(ROOT_PATH/'usuarios.csv', 'r', encoding='utf-8') as arquivo:
        # leitor = csv.reader(arquivo)
        # for row in leitor:
            # print(row)
# except IOError as exc:
    # print(f'Erro ao criar o arquivo: {exc}')

# Práticas recomendadas:
#   - Usar csv.reader e csv.writer para modificar arquivos .csv
#   - Fazer tratamento correto das exceções
#   - Ao gravar arquivos csv definir o argumento newline ='' no método open
