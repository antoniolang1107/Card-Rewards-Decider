import json

"""
Author: Antonio Lang
Date: 6 August 2022
Program: Card Rewards Decider
    Tells what the best card to use is based off a given merchant/category.
"""

class Reward:
    def __init__(self, location, percent, card_name) -> None:
        self.location = location
        self.percent = float(percent)
        self.card_name = card_name
    def __ge__(self, __o : object):
        return self.percent >= __o.percent
    def __str__(self):
        return str(f"{self.percent}% at {self.location} on {self.card_name}")


def main():
    card_file = "card-file.txt"
    card_data = []
    for card in read_list(card_file):
        card_data.append(parse_cards(card))
    merchants, categories = parse_dict(card_data)
    # get_input(card_data)


def get_input(display_data) -> str:
    """
    displays information and gets input from user
    """
    while True:
        option = ""
        option = input ("1. Display Merchants\n"
                      + "2. Display Categories\n"
                      + "3. Enter Merchant\n"
                      + "4. Enter Category\n"
                      + "Option: ")
        if option == "1":
            pass
            # print(display_data[0]['merchants']) # works to display, but should be cleaned first
        elif option == "2":
            pass
            # print(display_data[0]['categories'])
        elif option == "3" or option == "4":
            return input("Merchant/Category: ") # maybe separate merchant or category
        else:
            print("Invalid input")


def parse_cards(f_name) -> dict:
    """
    reads the data for each card into a dictionary
    """
    with open(f_name) as file:
        card_data = json.load(file)
    return card_data


def read_list(f_name) -> list:
    """
    reads the list of cards
    """
    cards = []
    with open(f_name, 'r') as file:
        while (line := file.readline().rstrip()): # reads f_names without \n
            cards.append(line)
    return cards


def select_card(selection_list, spend_type) -> str:
    pass


def parse_dict(given_dict) -> list:
    """
    create each into tuples and removes duplicate merchant/categories
    """
    merchants, categories = create_tuples(given_dict)
    merchants = remove_duplicate_rewards(merchants)
    categories = remove_duplicate_rewards(categories)

    # tuple: place, %, card
    return merchants, categories


def create_tuples(card_dict) -> list:
    """
    separates the card dictionary into separate lists
    """
    merchant_tuples = []
    category_tuples = []
    for card in card_dict:
        card_name = card['card']
        for merchants in card['merchants']:
            # print(f"Merchants: {merchants}")
            for percent, merchant in merchants.items():
                # print(f"Percent {percent}, Merchant: {merchant}")
                for specific in merchant:
                    merchant_tuples.append((specific, percent, card_name))
        for categories in card['categories']:
            # print(f"Categories: {categories}")
            for percent, category in categories.items():
                # print(f"Percent {percent}, Category: {category}")
                for specific in category:
                    category_tuples.append(Reward(specific, percent, card_name))
    return merchant_tuples, category_tuples


def remove_duplicate_rewards(given_list) -> list:
    """
    remove duplicate (by merchant/category) tuples in a given list
    """
    seen = []
    pruned_list = []
    for value in given_list: # iterates over merchants/categories list
        for loc_seen in seen:
            if loc_seen.location == value.location and value >= loc_seen:
                pruned_list.remove(loc_seen)
        seen.append(value)
        pruned_list.append(value)
    return pruned_list


if (__name__ == '__main__'):
    main()