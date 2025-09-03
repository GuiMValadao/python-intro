#Cada linha de print, com cada exemplo, esta colocada como comentario. Para rever a linha basta remover #.
frase = '''
Qualquer coisa
        so chamar
'''
#print(frase)            # Usar aspas triplas permite gravar strings em linhas diferentes.

#print(type(frase))      #type retorna o tipo da variavel

parte1 = 'Um di'
parte2 = 'a chuvoso'
#print(parte1 + parte2)  #pode-se fazer combinaçoes de strings:

#print(len(parte1))      #a funçao length retorna o numero de caracteres na string:

#print(parte2[3])        #pode-se acessar caracteres especificos de uma string usando [], note que a contagem começa no zero

#print(parte1[2:5])      #pode-se acessar um conjunto especifico de caracteres de uma string atraves de [:]
#print(parte2[:5])       #omitir o primeiro ou ultimo numero implica em iniciar ou terminar nos extremos da string

#print('?'*3)            #Usar o operador * em uma string a fara ser repetida um determinado numero de vezes

titulo = 'O bom, o mau, e o feio'
#print('string inicial:', titulo)    #Pode-se separar strings com a funçao split(' '):
#print('Separar usando um espaço:')
#print(titulo.split(' '))            #Se o argumento do split e vazio, separa nos espaços
#print('Separar usando uma virgula:')
#print(titulo.split(','))            #Se o argumento do split e uma virgula, separa nas virgulas
#print('Separar usando "o":')        #O argumento de split pode ser uma letra
#print(titulo.split('o'))            #a funçao split e um metodo.

string1 = 'Contar o numero de     espaços:'
#print("string1.count(''):", string1.count(' ')) #count permite contar o numero do caracteres ou sequencias de caracteres de interesse
#print("string1.count(''):", string1.count('o'))
#print("string1.count(''):", string1.count('ar'))

boas_vindas = "Ola, mundo!"
#print(boas_vindas.replace('Ola','Tchau'))   #pode-se substituir uma sequencia de caracteres de uma string para outra usando .replace()

#print(frase.find('coisa'))      #Pode-se verificar se uma string e substring de outra com o metodo find(). Se sim, ele retorna a posiçao  inicial da substring na string principal
#print(frase.find('espaços'))    #Se a string nao aparece na principal, retorna -1.

#msg = 'Ola Joao, voce tem' + 23    #(Esta linha causara erro na proxima)
#print(msg)                      #Usar operaçoes em tipos de dados diferentes resulta em erro. Deve-se tornar os dados no mesmo tipo
msg = 'Ola Joao, voce tem ' + str(23)
#print(msg)

#print('Jonas' == 'Jonas')       #pode-se comparar duas strings usando == (retorna verdade se sao iguais) ou != (retorna verdade se sao diferentes)
#print('Carla' == 'Jonas')
#print('Marcio' != 'Jonas')

#Outras possiveis operaçoes usando strings:
some_string = 'Hello World'
#print('Testing a String')
#print('-' * 20)
#print('some_string', some_string)
#print("some_string.startswith('H')",
#some_string.startswith('H'))
#print("some_string.startswith('h')",
#some_string.startswith('h'))
#print("some_string.endswith('d')", some_string.endswith('d'))
#print('some_string.istitle()', some_string.istitle())
#print('some_string.isupper()', some_string.isupper())
#print('some_string.islower()', some_string.islower())
#print('some_string.isalpha()', some_string.isalpha())
#print('String conversions')
#print('-' * 20)
#print('some_string.upper()', some_string.upper())
#print('some_string.lower()', some_string.lower())
#print('some_string.title()', some_string.title())
#print('some_string.swapcase()', some_string.swapcase())
#print('String leading, trailing spaces', "    xyz      ".strip())

#Formataçao de strings
#format_string = 'Salve {}!'
#print(format_string.format('rapaziada'))

#nome = 'Bruno'
#idade = 34
#3print("{} tem {} anos de idade".format(nome, idade)) #Se os espaços reservados nao tem indices, sao preenchidos na ordem que aparecem no argumento
#format_string = "Ola {1} {0}, voce conseguiu {2}%"
#print(format_string.format('Silva', 'Carol', 75))   #Se os espaços reservados tem indices, eles serao preenchidos de acordo.

#format_string = "{artista} lançou {musica} em {ano}"
#print(format_string.format(artista='Judas Priest', musica='Invincible shield', ano='2024')) # Os indices podem ser nomes para diminuir a chance de confundir as posiçoes
/
#print('|{:35}|'.format('largura de 35 caracteres'))     #Pode-se usar o metodo format() para definir largura e alinhamento da string.
#print('|{:<35}|'.format('alinhado a esquerda'))         #Por padrao, se nao explicito, a string e alinhada a esquerda
#print('|{:>35}|'.format('alinhado a direita'))
#print('|{:^35}|'.format('centralizado'))
#print('{:,}'.format(1234567890))                         #Pode-se tambem utilizar formato para separa numeros por virgulas a cada milhares,milhoes,etc
#print('{:,}'.format(1234567890.0))

import string       #esse comando permite usar a funçao template, que permite usar $variaveis em uma string que serao substituidas por valores reais.
template = string.Template('$artista lançou a musica $musica em $ano')
#print(template.substitute(artista = 'Van der Graaf Generator',
#                          musica = 'A Plague of Lighthouse Keepers',
#                          ano = 1971))
#d = dict(artista  = 'Iron Maiden', musica = 'Powerslave', ano = 1985)   #Pode-se tambem criar um dicionario que grava os valores das variaveis, em vez de se substitui-las diretamente no argumento.
#print(template.substitute(d))
#temp = string.Template('R$$ $valor')        #Para usar o simbolo $ como caractere, basta utilizar $$ (escaping a control character)
#print(temp.substitute(valor = 500))        #${template_var} = $template_var
#print(template.safe_substitute(artista = 'Iron Maiden', musica = 'Powerslave'))  #Usar safe_substitute remove a necessidade de preencher todas as variaveis, exibindo o nome da variavel faltando em vez de um valor.

