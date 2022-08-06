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
    card_data = read_card_list(card_file_name="card-file.txt")
    merchants, categories = parse_dict(card_data)
    location, spend_type = get_input(merchants, categories)
    if location != "exit":
        if spend_type == "merchant":
            best_card = select_card(merchants, location)
            pass
        elif spend_type == "category":
            best_card = select_card(categories, location)
        print(f"The best card for the transaction is: {best_card}")

def get_input(merchant_data, category_data) -> str:
    """
    displays information and gets input from user
    """
    while True:
        option = ""
        option = input ("--------------------------\n"
                      + "1. Display Merchants\n"
                      + "2. Display Categories\n"
                      + "3. Enter Merchant\n"
                      + "4. Enter Category\n"
                      + "5. Exit\n"
                      + "Option: ")
        print("--------------------------")
        if option == "1":
            for merchant in merchant_data:
                print(merchant.location)
        elif option == "2":
            for category in category_data:
                print(category.location)
        elif option == "3": # add option to select by number/index?
            return input("Enter the merchant: "), 'merchant'
        elif option == "4":
            return input("Enter the category: "), 'category'
        elif option == "5":
            break
        else:
            print("Invalid input")
    return "exit", "exit"


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


def select_card(selection_list, location) -> str:
    best_card = ""
    for reward in reversed(selection_list):
        if reward.location.lower() == location.lower() or reward.location == "base":
            best_card = reward.card_name
    return best_card

def parse_dict(given_dict) -> list:
    """
    create each into tuples and removes duplicate merchant/categories
    """
    merchants, categories = create_tuples(given_dict)
    merchants = remove_duplicate_rewards(merchants)
    categories = remove_duplicate_rewards(categories)
    return merchants, categories


def create_tuples(card_dict) -> list:
    """
    separates the card dictionary into separate lists
    """
    merchant_tuples = []
    category_tuples = []
    # iterates over the merchants and categories sections of the dict
    # separates the two into separate Reward lists
    for card in card_dict:
        card_name = card['card']
        for merchants in card['merchants']:
            for percent, merchant in merchants.items():
                for specific in merchant:
                    merchant_tuples.append(Reward(specific, percent, card_name))
        for categories in card['categories']:
            for percent, category in categories.items():
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
            # following if removes from the pruned list if the new one is same or better
            if loc_seen.location == value.location and value >= loc_seen:
                pruned_list.remove(loc_seen)
        seen.append(value)
        pruned_list.append(value)
    return pruned_list


def read_card_list(card_file_name) -> dict:
    card_data = []
    for card in read_list(card_file_name):
        card_data.append(parse_cards(card))
    return card_data


if (__name__ == '__main__'):
    main()