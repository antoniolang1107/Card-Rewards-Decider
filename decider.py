import sys
import json

"""
Author: Antonio Lang
Date: 1 July 2022
Program: Card Rewards Decider
    Tells what the best card to use is based off a given merchant/category.
"""


def main() -> None:
    if len(sys.argv) == 2 is True:
        card_data = parse_file(sys.argv[1])
        pass
    else:
        print(f"Incorrect number of arguments given")
        print(f"Proper format: decider.py <cardData.json>")


def get_input() -> str:
    # logic to determine category or merchant?
    pass


def parse_file(f_name) -> dict:
    with open(f_name) as f:
        data = json.load(f)
    return data


def select_card(card_list, category) -> str:
    pass


if (__name__ == '__main__'):
    main()