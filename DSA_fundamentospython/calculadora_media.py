def media_turma(alunos):
    """ Calcula a média de notas a partir de um 
    dicionário contendo 'nome' como chave e 'nota' como valor
    e retorna a lista com os nomes dos alunos com notas acima
    da média """
    media, i = 0, 0
    aprovados = []
    for nome, nota in alunos.items():       # Calcula a média da turma
        media += nota
        i += 1
    media = media/i
    print(f'Média da turma = {media:.2f}')
    for nome, nota in alunos.items():       # Salva o nome dos alunos com nota acima da média
        if nota > media:
            aprovados.append(nome)
        else:
            continue
    return aprovados



alunos = {'Ana': 6.5,                   #Dicionário de exemplo
         'Carlos': 8.0,
         'João': 7.3,
         'José': 5.6,
         'Mário': 7.8,
         'Santana': 7,
         'Maria': 6.5,
         'Tadeu': 5.2}
print(media_turma(alunos))