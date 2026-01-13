from json import JSONEncoder


class Livro:
    """Representa um livro na livraria"""

    def __init__(self, isbn, titulo, autor, preco):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.preco = preco

    def __str__(self):
        return (
            self.titulo
            + " por "
            + self.autor
            + " (ISBN: "
            + self.isbn
            + ", Preço: R$"
            + str(self.preco)
            + ")"
        )


class Livraria:
    def __init__(self, livros):
        self.livros = livros

    def add_livro(self, livro):
        self.livros.append(livro)


class LivroJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Livro):
            return {
                "isbn": obj.isbn,
                "titulo": obj.titulo,
                "autor": obj.autor,
                "preco": obj.preco,
            }
        return super(LivroJSONEncoder, self).default(obj)


livraria = Livraria(
    [
        Livro("1", "Effective Java", "Joshua Bloch", 45.0),
        Livro("2", "Design Patterns", "Gang of Four", 50.0),
        Livro("3", "Effective C++", "Scott Meyers", 42.0),
    ]
)

livro = LivroJSONEncoder().encode(livraria.livros[0])
print(type(livro))
