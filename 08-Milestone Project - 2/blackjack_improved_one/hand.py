class Hand():
    """
    Class to hold a Blackjack player's hand.
    """

    def __init__(self):
        # Cards for this hand are kept in a list.
        self.cards = []

        # Total value of player's hand.
        self.total = 0


    def add(self, card):
        """
        Add a new card to this hand.

        Whenever a new card gets added, the total value of this
        hand gets updated.
        """

        # Add card.
        self.cards.append(card)

        # Recalculate totals for this hand.
        self.calculate_total()


    def get_total(self):
        """
        Get the total value of this hand.
        """
        return self.total


    def calculate_total(self):
        """
        Check the cards for the specified player.
        """
        total = 0
        for card in self.cards:
            # Number cards can simply be added.
            if isinstance(card[1], int):
                total = total + card[1]

            # People cards have a value of 10.
            if card[1] in ['jack', 'queen', 'king']:
                total = total + 10

        # Handle aces separately.
        # Find the best combination for aces.
        # 1 ace:  1 or 11
        # 2 aces: 1,1, or 11,1 (all other combos go over)
        # 3 aces: 1,1,1 or 11,1,1 (all other combos go over)
        # 4 aces: 1,1,1,1 or 11,1,1,1 (all other combos go over)
        aces = list(
            filter(lambda card: card[1] == 'ace', self.cards))
        if len(aces) == 1:
            if (total + 11) > 21:
                total = total + 1
            else:
                total = total + 11
        elif len(aces) == 2:
            if (total + 12) > 21:
                total = total + 2
            else:
                total = total + 12
        elif len(aces) == 3:
            if (total + 13) > 21:
                total = total + 3
            else:
                total = total + 13
        elif len(aces) == 4:
            if (total + 14) > 21:
                total = total + 4
            else:
                total = total + 14

        # Set the total as an instance variable.
        self.total = total
