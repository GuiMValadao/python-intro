# Exercício 5
def dsa_calcula_imc(peso, altura):
    """ Calcula o imc (peso/(altura^2)), fornecidos peso e altura.
    Exige que a unidade de ambas as grandezas sejam fornecidas,
    gerantindo que sejam kg e m, respectivamente """
    peso_separado = peso.split()        # Usado .split() para separar o valor numérico da unidade
    altura_separada = altura.split()
    while not peso_separado[1] == 'kg':         # Garante que o peso esteja em kg
        peso = input('Peso deve ser em kg! Digite o valor correto com unidade:')
        peso_separado = peso.split()
    while not altura_separada[1] == 'm':        # Garante que a altura esteja em m
        altura = input('Altura deve ser em m! Digite o valor correto com unidade:')
        altura_separada = altura.split()
    return float(peso_separado[0])/(float(altura_separada[0])**2)   # retorna o imc

dsa_calcula_imc('72 kg', '1.74 m')
#---------------------------------------------------
#Exercício 6
lista_dict = [{'nome':'João', 'idade': 23},
              {'nome':'Carlo', 'idade': 32},
              {'nome':'Jonas', 'idade': 43},
              {'nome':'Silvia', 'idade': 22}]
lista_ordenada = sorted(lista_dict, key = lambda x: x['idade']) # Note que na função lambda não especifica-se lista_dict

print(lista_ordenada)

#--------------------------------------------------
# Exercício 8
def funcao_strings(msg, dominio_desejado = 'gmail.com'):
    """ Recebe uma lista 'msg' contendo listas do tipo [e-mail, mensagem]
    e retorna todas as mensagens de emails contendo a string fornecida
    ou a string padrão 'gmail.com'. """
    msg_selec = [msg[email][1] for email in range(len(msg)) if dominio_desejado in msg[email][0]]
    return msg_selec        # Retorna a lista msg_selec com os emails filtrados
msg = [['e-mail@..1', 'string1'],
        ['e-mail@..2', 'string2'],
        ['e-mail@..3', 'string3'],
      ['e-mail@..1', 'string4']]
funcao_strings(msg, '@..1')

#-----------------------------------------------
# Exercício 9
lista_frases = ['string1','string2','string3','string4', 'STring5']
generator = (lambda x: (x.upper() + str('PYTHON')))     # notar, novamente, que na função lambda não especifica-se a lista, pois estamos fazendo isso com a função map
lista_mudada = list(map(generator, lista_frases))
print(lista_mudada)