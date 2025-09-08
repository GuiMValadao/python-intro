#-----------------------------------
# Idade de cachorros
#-----------------------------------

def obter_idade():
    """ Verifica que o input e numero real."""
    idade = input('Digite a idade do cachorro em anos: ')
    def try_float():
        try:
            float(idade)
            return True
        except:
            return False
    while not try_float() or float(idade) < 0:
        if not idade.isnumeric():
            print('O valor deve ser numero real')
            idade = input('Digite a idade do cachorro em anos: ')
        elif float(idade) < 0:
            print('A idade nao pode ser negativa. Digite novamente')
            idade = input('Digite a idade do cachorro em anos: ')
    return idade

idade_cachorro = obter_idade()
if float(idade_cachorro) <= 2:
    print('A idade equivalente do cachorro a idade humana '
          'e', float(idade_cachorro)*10.5)
else:
    print('A idade equivalente do cachorro a idade humana '
          'e', 21 + float(idade_cachorro) * 4)

