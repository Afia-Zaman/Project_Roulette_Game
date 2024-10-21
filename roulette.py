# roulette.py

import random

# Constants for colors
RED = "red"
BLACK = "black"

def spin_wheel():
    """Spins the wheel and returns a random number between 1 and 36."""
    return random.randint(1, 36)

def get_color(number):
    """Determines the color of the number on the roulette wheel."""
    if ((1 <= number <= 10) or (19 <= number <= 28)):
        return RED if number % 2 != 0 else BLACK
    else:
        return BLACK if number % 2 != 0 else RED

def color_bet_won(bet_color, winning_number):
    """Returns True if the color bet won, False otherwise."""
    return bet_color == get_color(winning_number)

def number_bet_won(bet_number, winning_number):
    """Returns True if the number bet won, False otherwise."""
    return bet_number == winning_number
