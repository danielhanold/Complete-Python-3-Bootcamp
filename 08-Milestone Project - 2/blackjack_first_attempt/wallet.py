"""
Class to manage the player's wallet.
"""

class Wallet:
    """
    Creates a new wallet with a predefined amount of cash.
    """

    def __init__(self, start_amount=1000):
        """
        Args:
            start_amount: Amount of money player starts out with.
        """
        self.initial_balance = start_amount
        self.balance = start_amount

    def get_balance(self):
        """
        Returns the current balance.
        """
        return self.balance

    def add_money(self, amount):
        """
        Add a certain amount to the player's balance.
        """
        self.balance += amount

    def subtract_amount(self, amount):
        """
        Removes money from the player's balance.
        """
        if amount <= self.balance:
            self.balance -= amount
        else:
            message = 'Player cannot bet this amount. '
            message += 'He only has a remaining balance of {}.'
            print(message.format(self.balance))
