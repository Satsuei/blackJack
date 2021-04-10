# Time for gambling!
import os
import random
import time


class Card:
    def __init__(self, suit, value, card_value):
        # Suit of the Card like Spades and Clubs
        self.suit = suit

        # Representing Value of the Card like A for Ace, K for King
        self.value = value

        # Score Value for the Card like 10 for King
        self.card_value = card_value
def clear():
    os.system("clear")

# Function to print the cards
def print_cards(cards, hidden):
    x = ""
    for card in cards:
        if card.value == '10':
            x = x + "".format(card.value)
        else:
            x = x + "".format(card.value)
    if hidden:
        x += "?"
    print(x)

    x = ""
    for card in cards:
        x = x + "".format(card.suit)
    if hidden:
        x += ""
    print(x)


# Function for a single game of blackjack
def blackjack_game(deck):
    global cards_values

    # Cards for both dealer and player
    player_cards = []
    dealer_cards = []

    # Scores for both dealer and player
    player_score = 0
    dealer_score = 0

    while len(player_cards) < 2:

        # Randomly deal a card
        player_card = random.choice(deck)
        player_cards.append(player_card)
        deck.remove(player_card)

        # Updating score
        player_score += player_card.card_value

    clear()









if __name__ == '__main__':

    # The type of suit
    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]

    # The suit value
    suits_values = {"Spades": "\u2664", "Hearts": "\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}

    # The type of card
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    # The card value
    cards_values = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10,
                    "K": 10}

    # The deck of cards
    deck = []

    # Loop for every type of suit
    for suit in suits:

        # Loop for every type of card in a suit
        for card in cards:
            # Adding card to the deck
            deck.append(Card(suits_values[suit], card, cards_values[card]))