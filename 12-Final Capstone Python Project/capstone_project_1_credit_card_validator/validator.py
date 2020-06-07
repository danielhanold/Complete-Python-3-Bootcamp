"""
Credit card validator.
"""
from credit_card_tools import card_types
from credit_card_tools.luhn_algorithm import LuhnAlgorithm

# Define a class called CCValidator.
#
# Ask the user for a card number input
#
# Input validation:
# * Remove any spaces
# * Confirm correct length of number
# * Confirm number contains no invalid characters
#
# Card Number validation using custom package CreditCardTools
# * Use custom class LuhnAlgorithm to confirm is card is valid.
# * Use custom class CardType to determine which card type is used
#
# Output:
# * Show if card is valid
# * If card is valid, show type of credit card.

class CCValidator():
    """
    Asks user for a credit card number and validates it.
    """

    def __init__(self):
        print('Welcome to the credit card validation service.\n')
        self.number = self.get_card_number()

        # Validate the number.
        self.validate_card_number()

    def get_card_number(self):
        while True:
            # Retrieve input.
            num = input('Please enter a credit card number for validation: ')

            # Remove all whitespace from input.
            num = num.replace(' ', '')

            # Convert input to int.
            try:
                num = int(num)
            except:
                print('Your number contains invalid characters. Please remove and try again.\n')
                continue
            else:
                if card_types.max_number > len(str(num)) < card_types.min_number:
                    # Confirm that number is correct length.
                    print('The number of digits in your credit card number is incorrect. Please fix.')
                    continue
                else:
                    return num

    def validate_card_number(self):
        luhn_tester = LuhnAlgorithm(self.number)
        if luhn_tester.is_valid:
            print('Your card number is valid.')
        else:
            print('This is an invalid credit card number.')


# Require this script to be executed as the main script.
if __name__ == '__main__':
    val = CCValidator()
else:
    print('This script needs to be executed by itself from a shell.')
