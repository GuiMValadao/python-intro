## Initial concept of a music focused game

This project is built using pygame. 
This games has similar mechanics to rhythm games like Guitar Hero, but instead of focusing on rhythm it focuses on the notes played. 
Some of the features of the prototype are:
* an NPC who'll give a comprehensive tutorial of the game workings.
* The playing keys maps the 7 natural notes, and allows sharps and flats accidentals. The default keyboard keys are 'A, S, D, H, J, K and L', and the modifiers are SHIFT for the sharps and CTRL for the flats.
* High score recording for each song
* Key remaping inside the 'Options' menu from the main menu
* Difficulty settings; 'Hard' is the default and intended way, 'Medium' and 'Easy' slows the movement of the blocks and decreases their amount
* Song selection screen. To play a selected song, it's necessary to be in the game map and click 'B'. Clicking 'B' from inside the song play screen returns to the game world.


* A forma sugerida para executar o jogo, pode-se lançar o executável 'MusicGame.exe', que foi criado usando pyinstall. Alternativamente, pode-se executar main.py usando Python3. No entanto, devido a incompatibilidade de PyGame com a versão 3.14 de Python, pode-se haver dificuldades de baixar pygame para essa versão do Python (a versão do Python desse projeto é 3.13.12, e a versão do Pygame é 2.6.1).
