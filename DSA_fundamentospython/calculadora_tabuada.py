def tabuada(x):
    """ Calcula a tabuada de x do 1 ao 10 """
    print('-'*20)
    print(f'Tabuada do {x}')
    print('-'*20)
    for i in range(1,11):
        print(f' {x} * {i} = {x*i}')

def tabuada2(x):
    """ Calcula a taboada de x do 1 ao 10, usando comprehension """
    return {f'{x} x {i}': x*i for i in range(1,11)}
    
tabuada(int(input('insira um número inteiro: ' )))
print('-'*20)
#print(tabuada2(21))