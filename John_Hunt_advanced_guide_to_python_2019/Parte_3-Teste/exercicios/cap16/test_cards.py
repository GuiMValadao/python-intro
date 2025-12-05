import cards
from unittest.mock import *
from unittest import TestCase
from unittest import main


import random
from unittest.mock import *


def create_suite(suite):
    return [(i, suite) for i in range(1, 14)]


def pick_a_card(deck):
    print("You picked")
    position = random.randint(0, 52)
    print(deck[position][0], "of", deck[position][1])
    return deck[position]


class test_Cards(TestCase):

    @patch("random.randint")
    def test_pick_a_card(self, mock_random):
        mock_random.return_value = (
            51  # Escolhe valor que será retornado pela função(random.randint) simulada
        )
        result = pick_a_card(deck)  # Chama a função a ser simulada
        # Verifica se o valor especificado condiz com o comportamento da função
        self.assertEqual((13, "clubs"), result, "resultado incorreto")


# Set up the data
hearts = create_suite("hearts")
spades = create_suite("spades")
diamonds = create_suite("diamonds")
clubs = create_suite("clubs")
# Make the deck of cards
deck = hearts + spades + diamonds + clubs
# Randomly pick from the deck of cards
card = pick_a_card(deck)
# print(deck)
