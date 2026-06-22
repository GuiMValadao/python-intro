## Conceito inicial de um jogo focado em música

Este projeto é construído usando a biblioteca pygame, em Python.
O jogo possui mecânicas similares a jogos de ritmo, como Guitar Gero, mas prioriza as notas tocadas em vez do ritmo.
Alguns dos recursos presentes neste protótipo são:
* um NPC que fornece um tutorial completo das mecânicas do jogo
* As teclas do jogo mapeiam as 7 notas naturais, e permite os acidentes sustenido e bemol. As teclas padrão são 'A, S, D, H, J, K e L', e os modificadores são SHIFT para os sustenidos e CTRL para os bemois.
* Salva a maior pontuação obtida em cada música.
* Remapeamento das teclas dentro do menu 'Options' no menu principal
* Possui três dificuldades; 'Hard' é o padrão e a forma planejada das músicas, 'Medium' e 'Easy' diminuem a velocidade de movimento dos blocos e diminui sua quantidade.
* Menu de seleção de música. Para jogar com uma música escolhida, deve-se retornar para o mapa do jogo e clicar 'B'. Clicar 'B' de dentro da tela de jogo retorna ao mundo do jogo.

* A forma sugerida para executar o jogo, pode-se lançar o executável 'MusicGame.exe', que foi criado usando pyinstall. Alternativamente, pode-se executar main.py usando Python3. No entanto, devido a incompatibilidade de PyGame com a versão 3.14 de Python, pode-se haver dificuldades de baixar pygame para essa versão do Python (a versão do Python desse projeto é 3.13.12, e a versão do Pygame é 2.6.1).
