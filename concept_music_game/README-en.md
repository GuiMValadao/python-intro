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

* The suggested way to launch the game is by executing 'MusicGame.exe', created using pyinstall. Alternatively, the entry point is found in main.py, which can be, then, launched using Python3. However, due Pygame incompatibility with Python 3.14, this way can require some adjustment of the python environment (the Python version for the project is 3.13.12, and Pygame version is 2.6.1).

