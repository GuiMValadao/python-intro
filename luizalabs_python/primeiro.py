# Para executar um programa no modo interativo basta
# digitar 'python -i nome_programa.py' no terminal
print("Testando com o modo interativo")

# Método dir() sem argumentos retorna a lista de nomes no
# escopo local atual. Com argumento, retorna a lista
# de atributos válidos para o objeto: dir(), dir(100)

# Método help() invoca o sistema de ajuda integrado.

nome = 'Guilherme'
sobrenome = 'Valadão'

print(nome, sobrenome)
print(nome, sobrenome, end='...\n')   # end='' pemite escrever o novo print na mesma linha ou mudar o final da linha; \n faz o print exibir o restante em nova linha
print(nome, sobrenome, sep='$')     # sep='' muda o separador entre as variáveis em print.
