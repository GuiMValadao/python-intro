import numpy as np

import math
import time

#precos_np = np.random.rand(10_000_000)

#print(type(precos_np))

#precos_list = list(precos_np)
#print(type(precos_list))

#t0 = time.time()
#desc = precos_np * 0.90
#final = desc + 5
#raiz = np.sqrt(precos_np)
#print("NumPy:", time.time() - t0, "segundos")

#t0 = time.time()
#desc = [p * 0.90 for p in precos_list]
#final = [p + 5 for p in desc]
#raiz = [math.sqrt(p) for p in precos_list]
#print("Python puro:", time.time() - t0, "segundos")

#vetor = np.array([17, 21, 100, 34])
#print("\nVetor(Array 1D):\n")
#print(vetor)
#print('='*30)
#--Output--
#Vetor(Array 1D):
#
#[ 17  21 100  34]
#================================================
#print("Formato do vetor:", vetor.shape)
#print("Número de dimentsões do vetor:", vetor.ndim)
#print("Número total de elementos do vetor:", vetor.size)
#print('='*30)
#--Output--
#Formato do vetor: (4,) -: (valor 1 dim, valor 2 dim ), se tem 1 dim, valor 2 dim é vazio.
#Número de dimentsões do vetor: 1
#Número total de elementos do vetor: 4
#================================================
#matriz = np.array([[1, 2, 3], [4, 5, 6]])
#print("\nMatriz(Array 2D):\n")
#print(matriz)
#print("Formato da matriz:", matriz.shape)
#print("Número de dimentsões do matriz:", matriz.ndim)
#print("Número total de elementos do matriz:", matriz.size)
#print('='*30)
#--Output--
#Matriz(Array 2D):
#
#[[1 2 3]
# [4 5 6]]
#Formato da matriz: (2, 3) -> (linhas, colunas)
#Número de dimentsões do matriz: 2
#Número total de elementos do matriz: 6
#================================================
#tensor = np.arange(24).reshape(4, 3, 2)
#print("\nTensor(Array 3D):\n")
#print(tensor)
#print("Formato do tensor:", tensor.shape)
#print("Número de dimentsões do tensor:", tensor.ndim)
#print("Número total de elementos do tensor:", tensor.size)
#print('='*30)
#--Output--
# Tensor(Array 3D):
#
#[[[ 0  1]
#  [ 2  3]
#  [ 4  5]]
#
# [[ 6  7]
#  [ 8  9]
#  [10 11]]
#
# [[12 13]
#  [14 15]
#  [16 17]]
#
# [[18 19]
#  [20 21]
#  [22 23]]]
#Formato do tensor: (4, 3, 2)  - > (profundidade, linhas, colunas)
#Número de dimentsões do tensor: 3
#Número total de elementos do tensor: 24
#================================================
#tensor_4d = np.arange(120).reshape(2, 3, 4, 5)
#print("\nTensor 4D(Array 4D):\n")
#print(tensor_4d)  
#print("Formato (shape) do array:", tensor_4d.shape) 
#print("Número de dimensões (ndim) do array:", tensor_4d.ndim)
#print("Número total de elementos (size) do array:", tensor_4d.size)
#--Output--

#Tensor 4D(Array 4D):

#[[[[  0   1   2   3   4]
#   [  5   6   7   8   9]
#   [ 10  11  12  13  14]
#   [ 15  16  17  18  19]]
#
#  [[ 20  21  22  23  24]
#   [ 25  26  27  28  29]
#   [ 30  31  32  33  34]
#   [ 35  36  37  38  39]]
#
#  [[ 40  41  42  43  44]
#   [ 45  46  47  48  49]
#   [ 50  51  52  53  54]
#   [ 55  56  57  58  59]]]
#
#
# [[[ 60  61  62  63  64]
#   [ 65  66  67  68  69]
#   [ 70  71  72  73  74]
#   [ 75  76  77  78  79]]
#
#  [[ 80  81  82  83  84]
#   [ 85  86  87  88  89]
#   [ 90  91  92  93  94]
#   [ 95  96  97  98  99]]
#
#  [[100 101 102 103 104]
#   [105 106 107 108 109]
#   [110 111 112 113 114]
#   [115 116 117 118 119]]]]
#Formato (shape) do array: (2, 3, 4, 5)
#Número de dimensões (ndim) do array: 4
#Número total de elementos (size) do array: 120

#================================================

# TIPOS DE DADOS DO NUMPY
# NumPy infere o tipo de dado automaticamente
#arr_inteiros = np.array([1, 2, 3])
#print("Tipo de dado (inteiros):", arr_inteiros.dtype)
# NumPy infere o tipo de dado automaticamente
#arr_float = np.array([1.4, 2.1, 3.5])
#print("Tipo de dado (inteiros):", arr_float.dtype)
# Mas podemos especificar o tipo de dado durante a criação
#arr_float2 = np.array([1, 2, 3], dtype = np.float64)
#print("Tipo de dado (float64):", arr_float2.dtype)
#print("Array float2:", arr_float2)
# Conversão para int64
#arr_int = arr_float.astype(np.int64)    # Se tiver decimais,
#print("Tipo convertido:", arr_int.dtype)
#print("Array convertido:", arr_int)
#================================================
#INDEXAÇÃO E FATIAMENTO
# Vamos criar uma matriz 4x4 com números de 0 a 15
#dados = np.arange(16).reshape(4, 4)
#print("\nMatriz Original:\n")
#print(dados)
# Acessando um elemento específico: linha 1, coluna 2 (lembre-se que a indexação em Python começa em 0)
#print("\nMatriz Original:\n")
#print(dados)
#elemento = dados[1, 2]
#print(f"\nElemento na posição [1, 2]: {elemento}\n")
# Fatiando para obter a primeira linha completa (sintaxe pelo índice da linha)
#print("\nMatriz Original:\n")
#print(dados)
#primeira_linha = dados[0] 
#print(f"\nPrimeira linha:\n{primeira_linha}\n")
# Fatiando para obter a primeira linha completa (sintaxe pelo índice da linha e da coluna)
#print("\nMatriz Original:\n")
#print(dados)
#primeira_linha = dados[0, :]
#print(f"\nPrimeira linha:\n{primeira_linha}\n")
# Fatiando para obter a segunda coluna completa
#print("\nMatriz Original:\n")
#print(dados)
#segunda_coluna = dados[:, 1]
#print(f"\nSegunda coluna:\n{segunda_coluna}\n")
# Fatiando um bloco 2x2 do canto superior esquerdo
#print("\nMatriz Original:\n")
#print(dados)
#bloco_superior_esquerdo = dados[:2, :2]
#print(f"\nBloco 2x2 superior esquerdo:\n{bloco_superior_esquerdo}\n")
# Indexação booleana: selecionando apenas os números maiores que 10
#print("\nMatriz Original:\n")
#print(dados)
#maiores_que_10 = dados[dados > 10]
#print(f"\nNúmeros maiores que 10:\n {maiores_que_10}")
# Dada a matriz 5x5 abaixo, vamos criar um novo array que contenha apenas 
# as linhas de índice par e as colunas de índice ímpar.
# Cria a matriz
#matriz = np.arange(25).reshape(5, 5)
# Usamos o passo no slicing (start:stop:step)
# Para as linhas: '::2' significa do início ao fim, pulando de 2 em 2 (0, 2, 4)
# Para as colunas: '1::2' significa do índice 1 ao fim, pulando de 2 em 2 (1, 3)
#resultado = matriz[::2, 1::2]
#print("Matriz Original:")
#print(matriz)
#print("\nLinhas Pares e Colunas Ímpares:")
#print(resultado)

#================================================

#OPERAÇÕES MATEMÁTICAS VETORIZADAS
# Simulando dados de preços de produtos
#precos = np.array([19.99, 25.50, 8.90, 43.00])
#print(f"\nPreços originais: {precos}\n")
# Aplicando um desconto de 10% a todos os preços de uma vez
#precos_com_desconto = precos * 0.90
#print(f"\nPreços com 10% de desconto: {precos_com_desconto}\n")
# Mesmo resultado da célula anterior usando Python puro
# Lista original de preços
#precos_pp = [19.99, 25.50, 8.90, 43.00]
# Aplicando desconto de 10% usando list comprehension
#precos_com_desconto_pp = [preco * 0.90 for preco in precos_pp]
#print(f"\nPreços com 10% de desconto: {precos_com_desconto_pp}\n")
# Adicionando um valor fixo de frete
#precos_finais = precos_com_desconto + 5.00
#print(f"\nPreços finais com frete: {precos_finais}\n")
# Usando funções universais (ufuncs) do NumPy
# Exemplo: calculando a raiz quadrada de cada elemento
#raizes = np.sqrt(precos)
#print(f"\nRaiz quadrada dos preços: {raizes}")

#================================================

#AGREGAÇÕES ESTATÍSTICAS
# Simulando as notas de 3 alunos em 4 provas
#notas = np.array([
#    [8.5, 7.0, 9.2, 6.5],  # Aluno 1
#    [5.5, 6.8, 7.5, 8.0],  # Aluno 2
#    [9.5, 9.0, 8.8, 10.0]  # Aluno 3
#])
#print("\nMatriz de Notas:\n")
#print(notas)
#print(type(notas))
# Agregações na matriz inteira
#print(f"\nMédia geral da turma:    {notas.mean():.2f}")
#print(f"Nota máxima da turma:    {notas.max()}")
#print(f"Nota mínima da turma:    {notas.min()}")
#print(f"Soma de todas as notas:  {notas.sum()}\n")
# Agregações por eixo (axis)
# Média de cada aluno (agregando nas colunas, axis = 1) arredondando para duas casas decimais
#media_por_aluno = notas.mean(axis = 1).round(2)
#print(f"\nMédia de cada aluno: {media_por_aluno}\n")
# Média de cada prova (agregando nas linhas, axis = 0) arredondando para duas casas decimais
#media_por_prova = notas.mean(axis = 0).round(2)
#print(f"\nMédia de cada prova: {media_por_prova}")

#================================================

#BROADCASTING E OPERAÇÕES ENTRE ARRAYS
# No NumPy, broadcasting é o mecanismo que permite realizar 
# operações aritméticas entre arrays de formas (shapes) diferentes, 
# sem precisar copiar ou replicar manualmente os dados.
# Ele funciona expandindo automaticamente as dimensões de arrays 
# menores para que fiquem compatíveis com os maiores, seguindo um 
# conjunto de regras. Isso evita laços (loops) explícitos e melhora 
# muito a eficiência.
# Por exemplo, se você soma uma matriz 3×3 com um vetor de 3 elementos,
# o NumPy “estica” o vetor para que cada linha da matriz receba a soma
# correspondente elemento a elemento, sem criar cópias extras na memória.
# Matriz 3x3
#matriz = np.array([
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9]
#])
#print(type(matriz))
#print(matriz.shape)
# Vetor 1D com 3 elementos
#vetor = np.array([10, 20, 30])
#print(type(vetor))
#print(vetor.shape)
# Broadcasting: o vetor é "expandido" para cada linha da matriz
# (cada dimensão extra de vetor realiza a operação com valores da matriz)
#resultado = matriz + vetor
#print("\nMatriz original:\n", matriz)
#print("\nVetor:\n", vetor)
#print("\nResultado com broadcasting:\n", resultado)
#--OUTPUT--
#Resultado com broadcasting:
# [[11 22 33]
# [14 25 36]
# [17 28 39]]
#-------------
# Matriz com faturamento de 3 produtos em 4 meses
#faturamento = np.array([
#    [100, 110, 120, 130], # Produto A
#    [200, 210, 220, 230], # Produto B
#    [300, 310, 320, 330]  # Produto C
#])
# Vetor com um bônus (incentivo) para cada produto
#bonus_por_produto = np.array([5, 10, 15])
#print("\nFaturamento:\n")
#print(faturamento)
#print("\nBônus por Produto:\n")
#print(bonus_por_produto)
# Poderíamos usar a vetorização e fazer algo assim:
#faturamento_com_bonus = faturamento + bonus_por_produto
# O que retorna um erro
# O NumPy "estica" (broadcast) o vetor bônus para que ele possa ser somado à matriz
# Mas forma de `bonus_por_produto` (3,) é incompatível com (3, 4)
# Para somar, precisamos que tenha a forma (3, 1) para o broadcast funcionar nas colunas
#bonus_formatado = bonus_por_produto.reshape(3, 1)
#print(bonus_formatado.shape)
#print("\nBônus por Produto:\n")
#print(bonus_formatado)
# Agora sim
#faturamento_com_bonus = faturamento + bonus_formatado
#print("\nFaturamento com Bônus (via Broadcasting):\n")
#print(faturamento_com_bonus)

#================================================

#MANIPULAÇÃO DE FORMATO DE ARRAYS

# Criando um array 1D com 12 elementos
#dados_sequenciais = np.arange(12)
#print(f"\nArray original (1D): {dados_sequenciais}\n")
# Remodelando para uma matriz 3x4
#matriz_3x4 = dados_sequenciais.reshape(3, 4)
#print(f"\nMatriz 3x4:\n{matriz_3x4}\n")
# Transpondo a matriz (trocando linhas por colunas)
#matriz_transposta = matriz_3x4.T
#print(f"\nMatriz Transposta (4x3):\n{matriz_transposta}\n")
# Achatando a matriz de volta para um array 1D
#array_achatado = matriz_transposta.flatten()
#print(f"\nArray achatado (1D): {array_achatado}")

#================================================

#OPERAÇÕES MATEMÁTICAS COM MATRIZES
# Criando duas matrizes
#A = np.array([[1, 2], [3, 4]])
#B = np.array([[5, 6], [7, 8]])
#print(f"\nMatriz A:\n{A}\n")
#print(f"Matriz B:\n{B}\n")
# Produto de Matrizes (diferente da multiplicação elemento a elemento)
# Usando o operador @ (permite multiplicar duas matrizes)
#produto_matricial = A @ B
#print(f"\nProduto de A por B:\n\n{produto_matricial}\n")
# Usando np.dot() ao invés de @
#produto_matricial = np.dot(A, B)
#print(f"Produto de A por B:\n{produto_matricial}\n")
# Ambas operações são o produto matricial clássico da Álgebra Linear.
#print(f"\nMatriz A:\n{A}\n")
#print(f"Matriz B:\n{B}\n")
# Element wise
#produto_element_wise = A * B
#print(f"Multiplicação Element-wise de A por B:\n{produto_element_wise}\n")
#O NumPy multiplica cada elemento na mesma posição das duas matrizes. 
# Não há soma de produtos; é apenas posição a posição.
# Criando duas matrizes 2x2

A = np.array([[10, 20],
              [30, 40]])

B = np.array([[7, 14],
              [4, 3]])
# Soma de matrizes
soma = A + B
# Subtração de matrizes
subtracao = A - B
# Divisão elemento a elemento
divisao = A / B
print("Matriz A:\n", A)
print("\nMatriz B:\n", B)
print("\nSoma A + B:\n", soma)
print("\nSubtração A - B:\n", subtracao)
print("\nDivisão A / B:\n", divisao)