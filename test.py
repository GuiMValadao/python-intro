class PessoaFisica:

    contagem_usuarios = 0

    def __init__(self, nome="", cpf="", data_nascimento=""):
        self._cpf = cpf
        self.lista_cpfs = {}
        if cpf != "":
            PessoaFisica.contar_pessoas()
            self.lista_cpfs[PessoaFisica.contagem_usuarios] = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento
        self.__contador = 0
        self.valor_maximo = PessoaFisica.contagem_usuarios

    def __iter__(self):
        return self

    def __next__(self):
        print(self.lista_cpfs)
        if self.__contador == self.valor_maximo:
            raise StopIteration
        else:
            self.__contador += 1
            retornar = self.lista_cpfs[self.__contador]
            return retornar

    # método __str__?

    @classmethod
    def contar_pessoas(cls):
        cls.contagem_usuarios += 1


j1 = PessoaFisica(nome="Joao", cpf="1")
print(j1._cpf)
j2 = PessoaFisica(nome="Maria", cpf="2")
j3 = PessoaFisica(nome="Gui", cpf="3")
j4 = PessoaFisica(nome="Adriano", cpf="4")
j5 = PessoaFisica(nome="Silvana", cpf="5")


for num in PessoaFisica:
    print(num)
