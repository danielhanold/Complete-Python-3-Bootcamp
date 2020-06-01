"""
Create a full card deck that can be retrieved multiple times.
"""
from random import shuffle

class DeckGenerator():
    """
    Class to manage a card deck required for blackjack.
    """

    # Define available suits.
    suits = ('hearts', 'diamonds', 'clover', 'spades')

    # Define cards available for each suit.
    cardlist = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king', 'ace')

    def __init__(self):
        pass

    def get_new_deck(self, shuffle_cards=True):
        """
        Retrieve a new deck of cards.

        Args:
            shuffle_cards: Boolean to indicate if deck should be shuffle_cardsd.

        Returns:
            A list of all available cards as sets of tuples
        """
        deck = self.generate_new_deck()

        # shuffle_cards the deck if necessary.
        if shuffle_cards:
            shuffle(deck)

        return deck


    def generate_new_deck(self):
        """
        Generate a completely new, unshuffle_cardsd deck of cards.
        """
        deck = []

        for suit in DeckGenerator.suits:
            for card in DeckGenerator.cardlist:
                deck.append((suit, card))

        return deck
