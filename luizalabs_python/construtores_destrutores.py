class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instância")

    def latir(self):
        if self.acordado:
            print("auau")
        else:
            print("zzzz")


def criar_cachorro():
    c = Cachorro("Boris", "preto")
    c.latir()
    print(c.nome)


criar_cachorro()

# c1 = Cachorro("Medroso", "caramelo")
# c1.latir()
# del c1
# print(c1)
