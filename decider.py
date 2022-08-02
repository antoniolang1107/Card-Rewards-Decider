import sys
import json

"""
Author: Antonio Lang
Date: 2 August 2022
Program: Card Rewards Decider
    Tells what the best card to use is based off a given merchant/category.
"""


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Incorrect number of arguments given")
        print(f"Proper format: decider.py <card-data.txt>")
    else:
        card_data = []
        for card in read_list(sys.argv[1]):
            pass
            card_data.append(parse_cards(card))


def get_input() -> str:
    # logic to determine category or merchant?
    pass


def parse_cards(f_name) -> dict:
    """
    reads the data for each card into a dictionary
    """
    with open(f_name) as file:
        card_data = json.load(file)
    return card_data


def read_list(f_name):
    """
    reads the list of cards
    """
    cards = []
    with open(f_name, 'r') as file:
        while (line := file.readline().rstrip()): # reads f_names without \n
            cards.append(line)
    return cards


def select_card(card_list, category) -> str:
    pass


if (__name__ == '__main__'):
    main()