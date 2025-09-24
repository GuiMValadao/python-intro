# Capítulo 21 - Porque se inportar com Orientação a objetos?
# Este capítulo trata sobre como orientação a objetos
# lida com alguns dos problemas que surgem com linguagens processuais.
# Para fazer isso vamos olhar em como uma porção pequena de um programa
# poderia ser escrito em uma linguagem como C, considerar os problemas
# enfrentados pelo desenvolvedor de C e então olhar como a mesma
# funcionalidade poderia ser obtida em uma linguagem orientada a
# objetos como Python.
#------------------------------------
# Abordagem processual
# Considere o seguinte exemplo:
#record Date {
#   int day
#   int month
#   int year
#}
# Ele define uma estrutura de dados para guardar datas. Há estruturas
# similares em muitas linguagens processuais como C, Ada e Pascal. O que
# há de errado com uma estrutura como essa? Nada, além do problema
# de visibilidade? Isto é, o que pode ver esta estrutura e o que 
# pode atualizar os conteúdos da estrutura? Qualquer código pode
# acessar e modificar seus conteúdos. Poderia ocorrer, por exemplo, 
# algum código poderia definir dia como -1, mês como 13 e ano 9999.
# Esta estrutura apenas espera receber inteiros, e essas opções todas
# respeitam essa limitação.
# Procedimento para estruturas de dados
# Este dado é associado com procedimentos que realizam operações nele.
# Estas operações poderiam ser:
#   * testar se a data representa uma data em um fim de semana ou parte
#     da semana útil.
#   * mudar a data (neste caso o processo também poderia checar se a 
#     data é válida)
# Por exemplo:
#is_day_of_week(date)
#in_month(date,2)
#next_day(date)
#set_day(date, 9, 3, 1946)
# Como sabemos se estes procedimentos são relacionados à estrutura de datas 
# que acabamos de ver? Pelas convenções de nomeação dos processos e pelo
# fato que um dos parâmetros é um dado (record).
# O problema é que estes procedimentos não são limitados no que
# eles podem fazer aos dados (por exemplo, o processo SetDay poderia
# ter sido implementado por um britanico que assume que a ordem da
# data é dia, mês e ano. Entretanto, poderia ser usado por um americano
# que acha que a ordem é mês, dia, ano). Assim, o significado de
# set_day(date, 9, 3, 1946) será interpretado diferentemente.
# O problema é que o dado não tem defesa contra o que os procedimentos
# poderiam fazer com  ele.
# Pacotes
# Uma possibilidade, é claro, é usar um construto pacote. Em línguas como 
# Ada, pacotes são comuns e usados de maneira a organizar o código
# e restringir visibilidade. Por exemplo:
#package Dates ir
#   type Date is....
#   function is_day_of_week(d: Date) return Boolean;
#   function in_month(d: Date, m: Integer) return Boolean;
#...
# O construto pacote fornece alguma proteção à estrutura de dados 
# e um agrupamento da estrutura de dados com procedimentos associados.
# Para poder usar este pacote, um desenvolvedor primeiro deve importar
# o pacote. Então pode acessar os procedimentos e trabalhar
# com dados do tipo especificado (neste caso, Data).
# Pode até existir dados escondidos do usuário dentro de uma parte secreta.
# Portanto, isto aumenta a habilidade de enncapsular dos dados (esconder
# os dados) de atenção indesejada.
#-------------------------------------
# A orientação a objetos consegue fafazer melhor?
# Pacotes x Classes
# Pacotes tendem a ser maiores (pelo menos conceitualmente) que classes.
# Por exemplo, o pacote TextIO em Ada é, essencialmente, uma biblioteca de 
# instalações de IO textuais, em vez de um único conceito como a classe 
# string em Python. Assim, pacotes não são usados para encapsular um 
# único conceito pequeno como string ou Date, mas um conjunto inteiro de 
# conceitos relacionados. Assim, uma classe é um nível menor de granularidade
# que um pacote.
# Em segundo lugar, pacotes ainda fornecem uma associação relativamente
# frouxa entre os dados e procedimentos. Um pacote Ada pode, na verdade,
# lidar com muitas estruturas de dados com um alcance grande de métodos.
# Os dados e métodos são relacionados primariamente pelos conjuntos 
# relacionados de conceitos representados pelo pacote. Em contraste, 
# uma classe tende a relacionar dados e métodos proximamente em um único
# conceito. De fato, uma das guias relacionadas ao bom desenho de classes
# é que se uma classe representa mais de um conceito, você deveria 
# dividí-la em duas classes.
# Assim, esta associação próxima entre dados e código significa
# que o conceito resultante é mais que apenas uma estrutura de dados
# (é mais próximo de uma realização concreta do conceito). Por exemplo:
class Data:

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    def e_dia_util(self):
        """ Checa se a data é dia útil """
        #... A ser definido
    
    def no_mes(self, indice_mes):
        """ Checa se o mês está no indice_mes """
        return self.mes == indice_mes

# Qualquer um usando uma instância de Data agora obtém um objeto
# que pode dizer-lhe se é um dia útil ou não e pode guardar o
# dado apropriado. No que o método e_dia_util() não pega nenhum
# parâmetro além de self, pois ele não precisa, porque ele e a informação
# da data são parte da mesma coisa. Isto quer dizer que um usuário de
# um objeto Data nunca precisará obter o dado de fato que armazena a data
# (isto é, os inteiro dia, mes, ano). Em vez disso, eles deveriam usar
# os métodos. Nada fora do objeto deveria precisar acessar o dado de dentro
# dele. Em contraste, a estrutura de dados da versão processual, não apenas
# é armazenada separadamente aos procedimentos, mas os valores de dia,
# mes e ano também devem ser modificados diretamente.
# Por exemplo, compare a diferença entre uma seção de um programa que 
# manipula datas (usando linguagem processual):
#d: Data;
#definirDia(d, 28);
#definirMes(d, 2);
#definirAno(d, 1998);
#eDiaDaSemana(d);
#noMes(d, 2);

# Note que foi necessário, primeiro, criar os dados e então definir
# os campos na estrutura de dados. Aqui fomos bonzinhos e usamos a
# interface dos procedimentos para fazer isso. Uma vez que temos os
# dados prontos, poderíamos então chamar métodos como eDiaDaSemana e noMes
# naqueles dados.
# Em contraste, o código Python usa um construtor para passar a informação
# de inicialização apropriada. Como isto é inicializado internamente é
# escondido do usuário da classe Data. Podemos, então, chamar métodos
# como e_dia_util() e e_mes(12) diretamente na data objeto.
#data = Data(12, 2, 1998)
#data.e_dia_util()
#data.e_mes
#------------------------------------------------
# Herança
# Herança é um elemento chave em linguagens orientadas a objetos
# permitindo uma classe herdar dados e métodos de outras.
# Um dos recursos mais importantes da herança é que permite o 
# desenvolverdor entrar na bolha de encapsulação de forma limitada
# e controlada.
# Isto permite à subclasse tirar vantagem de estruturas de dados
# internas e métodos, sem comprometer a encapsulação conseguida a objetos.
# Por exemplo, vamos definir uma subclasse da classe Data:
#class aniversario(Data):
#   nome = ''
#   idade = 0
#   def e_aniversario():
#       #... Checar se é seu aniversário
# O método e_aniversario() poderia checar para ver a data atual,
# combinar o aniversário representado pela instância de aniversario
# e retornar True se são iguais e False se não.
# Note, no entanto, que o interessante aqui não é apenas que não
# tivemos que definir inteiros para representar a data, nem tivemos
# que definir métodos para acessar estas datas. Ambos foram herdados
# da classe Data.
# Além disso, podemos agora tratar uma instância de Aniversario como
# tanto uma data quanto um aniversario dependendo do que queremos fazer.
# Em linguagens como C, Pascal ou Ada você teria de definir um pacote 
# Aniversário que precisaria importar de Data, mas não extenderia Data.
# E certamente não poderia tratar Aniversário como Data.
# Em linguagens como Python, por causa do polimorfismo, você pode
# fazer exatamento isto. Você opde reutilizar código já existente 
# que apenas sabia sobre Data, por exemplo:
#aniversario = Aniversario(12, 3, 1974)
#def test(date):
#   # Fazer algo que funciona com uma data
#t.test(aniversario)
# Isto ocorre pois aniversário é, de fato, um tipo de Data, assim
# como é um tipo de Aniversário. Você pode, também, usar todas os
# recursos definidos para Data em Aniversario
#aniversario.e_dia_util()
# De fato, você não saberia de fato onde o método é definido.
# Este método poderia ser definido na classe Aniversario(onde 
# sobrescreveria o definido na classe Data), mas poderia também
# ser definido na classe Data (se não estivesse presente em Aniversario);
# sem olhar o código não há como saber.
