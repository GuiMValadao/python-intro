# Classes em Python
# Em Python, tudo é um objeto e, portanto, exemplo de um tipo de classe
# de coisas. Por exemplo, inteiros são um exemplo da classe 'int',
# números reais exemplos de 'float' etc. No entanto, não se é 
# restrito apenas a tipos(classes) pré-construídos (build-in types);
# também é possível criar classes definidas pelo usuário. Estas
# podem ser usadas para criar suas próprias estruturas de dados,
# próprios tipos de dados, próprias aplicações etc.
#----------------------------------------------------------------
# Definições de classe
# A definição de uma classe em Python tem o seguinte formato:
#class nameOfClass(SuperClass) :
#    _init_
#    attributes
#    methods

# Mas você deve notar que pode alterar a ordem da definição
# dos atributos e métodos conforme requerido em uma classe.
# O seguinte código é um exemplo da definição de uma classe:
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
# Apesar de não ser uma regra mandatória nem rápida, é comum definir uma
# classe em um arquivo nomeado pela classe. Por exemplo, o código acima
# poderia ser salvo em um arquivo chamado Pessoa.py; isto torna mais fácil
# encontrar o código associado a uma classe.
# A classe 'Pessoa' tem dois atributos (ou variáveis de instância)
# chamados 'nome' e 'idade'. Também há um método especial definido chamado
# __init__. Este é um inicializador(também chamado construtor) para classe.
# Ele indica quais dados devem ser fornecidos quando uma instância 
# da classe Pessoa é criada e como os dados são salvos internamente.
# Neste caso, um 'nome' e uma 'idade' devem ser fornecidos quando uma
# instância da classe Pessoa é criada.
# Os valores fornecidos serão, então, salvos dentro de uma instância
# da classe (representada pela variável especial 'self') em 
# variáveis/atributos de intâncisa self.nome e self.idade. Note que 
# os parâmetros do método __init__ são variáveis locais e desaparecerão
# quando o método finalizar, mas self.nome e self.idade são variáveis
# de instância e existirão enquanto o objeto estiver avaliável.
# Vamos olhar à variável especial self. Este é o primeiro
# parâmetro passao em qualquer método. No entanto, quando um método
# é chamadao, não passamos um valor para este parâmetro; Python o faz.
# Ele é usado para representar o objeto dentro do qual o método está
# executando. Ele fornece o contexto dentro do qual o método executa
# e permite ao método acessar os dados guardados pelo objeto. Portanto,
# self é o objeto em si.
# Um método é o nome dado para o comportamento que está conectado
# diretamente à classe Pessoa; não é uma função livre mas parte da 
# definição da classe Pessoa. Historicamente, esse nome vem da 
# linguagem
#
