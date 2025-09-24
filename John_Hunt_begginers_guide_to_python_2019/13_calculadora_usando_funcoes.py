#------------------------------------------------------
# Implementando uma calculadora usando funçoes
# Implementar uma calculadora simples que realiza +, -, * e /
#------------------------------------------------------
print('Aplicativo de calculos simples')

def soma(x, y):
    """ Adiciona dois numeros"""
    return x + y

def subtracao(x, y):
    """ Subtrai dois numeros"""
    return x - y

def multiplicacao(x, y):
    """ Multiplica dois numeros"""
    return x * y

def divisao(x, y):
    """ Divide dois numeros"""
    global operacao
    if operacao[1] == 'a':
        return x / y
    elif operacao[1] == 'b':
        return x // y

def modulo(x, y):
    """ Retorna o resto da divisao
        entre dois numeros"""
    return x % y

def potencia(x, y):
    """ Retorna x na potencia y"""
    return x ** y

def finalizador():
    """
    Checa se o usuario quer terminar
    os calculos ou nao. """
    terminar = True
    aceitar_input = False
    while not aceitar_input:
        terminar = input('Deseja terminar? (s/n) ')
        if terminar == 's':
            aceitar_input = True
        elif terminar == 'n':
            terminar = False
            aceitar_input = True
        else:
            aceitar_input = False
    return terminar

def sel_operacao():
    """
    Seleciona a operaçao a ser realizada."""
    input_ok = False
    while not input_ok:
        print('As opçoes de operaçoes sao:')
        print('\t1 Adicao')
        print('\t2 Subtracao')
        print('\t3 Multiplicacao')
        print('\t4 Divisao')
        print('\t5 Resto')
        print('\t6 Potencia')
        print('----------------------------')
        selecao_usuario = input('Por favor, escolha a operacao: ')
        if selecao_usuario in ('1', '2', '3', '4', '5', '6'):
            input_ok = True
            if selecao_usuario == '4':
                escolha = tipo_divisao()
                return selecao_usuario, escolha
            return selecao_usuario
        else:
            print('Escolha invalida (deve ser 1 a 4)')
        print('----------------------------')

def obter_nums():
    """ Obtem dois numeros reais."""
    num1 = obter_float('Digite o primeiro numero: ')
    num2 = obter_float('Digite o segundo numero: ')
    return num1, num2

def obter_float(message):
    """ Verifica que o input e numero real."""
    valor_string = input(message)
    def try_float():
        try:
            float(valor_string)
            return True
        except:
            return False
    while not try_float():
        print('O valor deve ser numero real')
        valor_string = input(message)
    return float(valor_string)

def tipo_divisao():
    esc_div = False
    while not esc_div:
        print('Pode escolher entre as divisoes:')
        print('\ta Divisao exata')
        print('\tb Divisao inteira')
        escolha = input('Qual divisao quer realizar? ')
        if escolha == 'a':
            esc_div = True
            return escolha
        elif escolha == 'b':
            esc_div = True
            return escolha
        else:
            print('Escolha entre 1 ou 2')
            print('-----------------------')

terminar = False
while not terminar:
    resultado = 0
    operacao = sel_operacao()
    x, y = obter_nums()
    if operacao == '1':
        resultado = soma(x, y)
    elif operacao == '2':
        resultado = subtracao(x, y)
    elif operacao == '3':
        resultado = multiplicacao(x, y)
    elif operacao[0] == '4':
        resultado = divisao(x, y)
    elif operacao == '5':
        resultado = modulo(x, y)
    elif operacao == '6':
        resultado = potencia(x, y)
    print('Resultado:', resultado)
    print('====================')
    terminar = finalizador()
print('Fim de papo')