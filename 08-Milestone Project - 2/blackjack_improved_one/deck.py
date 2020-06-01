"""
Create a full card deck that can be retrieved multiple times.
"""
from random import shuffle

class Deck():
    """
    Class to manage a card deck required for blackjack.
    """

    # Define available suits.
    suits = ('hearts', 'diamonds', 'clover', 'spades')

    # Define cards available for each suit.
    cardlist = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king', 'ace')

    def __init__(self, shuffle_deck=True):
        # Generate deck.
        self.deck = []
        self.generate_new_deck()

        # Shuffle the deck.
        if shuffle_deck:
            shuffle(self.deck)


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

    def draw_card(self):
        """
        Draw a single card and return it.
        """
        return self.deck.pop()

    def generate_new_deck(self):
        """
        Generate a completely new, unshuffle_cardsd deck of cards.
        """
        for suit in Deck.suits:
            for card in Deck.cardlist:
                self.deck.append((suit, card))
