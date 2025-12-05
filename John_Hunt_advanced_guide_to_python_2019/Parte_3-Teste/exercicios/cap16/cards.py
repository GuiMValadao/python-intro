import random
from unittest.mock import *


def create_suite(suite):
    return [(i, suite) for i in range(1, 14)]


def pick_a_card(deck):
    print("You picked")
    position = random.randint(0, 52)
    print(deck[position][0], "of", deck[position][1])
    return deck[position]


@patch("random.randint")
def test_pick_a_card(mock_card):
    print("You picked")
    mock_card.return_value = 5
    #    position = random.randint(0, 52)
    print(deck[mock_card][0], "of", deck[mock_card][1])
    return deck[mock_card]


# Set up the data
hearts = create_suite("hearts")
spades = create_suite("spades")
diamonds = create_suite("diamonds")
clubs = create_suite("clubs")
# Make the deck of cards
deck = hearts + spades + diamonds + clubs
# Randomly pick from the deck of cards
card = pick_a_card(deck)
print(deck)
