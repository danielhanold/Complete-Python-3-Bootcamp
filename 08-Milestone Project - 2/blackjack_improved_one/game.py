"""
Blackjack Game
"""
from deck import Deck
from hand import Hand
from wallet import Wallet
from random import randint
from time import sleep

class Blackjack():
    def __init__(self):
        # Set up the player's wallet.
        self.wallet = Wallet()

        # Reset the game.
        self.reset_game()

    def reset_game(self):
        """
        Reset all game variables for a new round.
        """

        # Set the current cards to an empty array.
        self.hands = {
            'dealer': Hand(),
            'player': Hand()
        }

        # Create a new new deck of cards.
        self.deck = Deck(shuffle_deck=True)


    def ask_bet(self):
        """
        Ask a player for the current round's bet.
        """

        balance=self.wallet.get_balance()
        message = '\nYou have {balance} remaining. Enter your bet: '.format(balance=balance)
        while True:
            try:
                self.bet = int(input(message))
            except:
                print('Please enter a number. Try again.')
                continue
            else:
                if self.bet > balance:
                    print('You cannot bet more than you have. Please enter a smaller number.')
                    continue
                else:
                    print('You bet {} for this round.'.format(self.bet))
                    break

    def draw_initial_cards(self):
        """
        Draw initial cards for player and dealer.
        """

        # Draw cards for player and dealer.
        for current in ('dealer', 'player'):
            for i in range(0, 2):
                card = self.deck.draw_card()
                self.hands[current].add(card)

    @staticmethod
    def format_card(card):
        """ Displays a single card tuple """

        card_value = str(card[1]).capitalize()
        card_suit = card[0].capitalize()
        return "{} of {}".format(card_value, card_suit)

    def display_cards(self, show_all=False):
        """
        Display all cards for the player and dealer.
        """
        message = "{}'s cards: {}"

        for player in ['dealer', 'player']:
            # Format the cards correctly.
            cards = [self.format_card(card) for card in self.hands[player].cards]

            # If it's the player's turn, do not display the second card of the dealer.
            if not show_all and player in 'dealer':
                cards[1] = '--hidden--'

            # Print the message.
            print(message.format(player.capitalize(), ' | '.join(cards)))

        # Empty line.
        print()

    def player_input(self):
        """
        Ask player for input.
        """
        while True:
            action = input("Do you want to Hit or Stay? Enter 'h' for hit, and 's' for stay: ")
            if action not in ['h', 's']:
                print("You can only enter 'h' for hit, and 's' for stay. Please try again.\n")
            else:
                break

        return action

    def display_totals(self):
        """
        Display the totals for this round.
        """
        print()
        print("---- Results for this round ----")
        self.display_cards(show_all=True)
        print("Dealer total is: {}".format(self.hands['dealer'].total))
        print("Player total is: {}".format(self.hands['player'].total))

    def player_result(self, outcome):
        """
        Player has either won or lost this round.
        """
        self.display_totals()
        if outcome == 'win':
            self.wallet.add_money(self.bet * 2)
            message = 'You won this round and doubled your bet of {}.'
        elif outcome == 'lose':
            self.wallet.subtract_amount(self.bet)
            message = 'You lost this round and your bet of {}.'

        print(message.format(self.bet))
        print('Coins in your wallet are now: {}'.format(self.wallet.get_balance()))

    def check_blackjack(self, person):
        """
        Check if a person has blackjack.
        """
        if self.hands[person].total == 21:
            # If the player has more 21, he instantly won.
            print("{} has BLACKJACK!!!!".format(person.capitalize()))

    def play_game(self):
        # Play until game is not continued.
        continue_game = True

        while continue_game:
            # Play another round.
            self.play_round()

            # Once complete, ask if the player wants to play again.
            while True:
                # If user is out of money, he cannot play again.
                if self.wallet.balance == 0:
                    print('You are broke and cannot play any more.')
                    continue_game = False
                    break

                # If user has money left, ask if he wants to play
                play_again = input('Do you want to play anther round (y/n): ')
                if play_again.lower() not in ['y', 'n']:
                    print('Invalid choice. Please enter y or n only.')
                elif play_again == 'y':
                    print('Alright. Let\'s play again.')
                    break
                else:
                    print('Thank you for playing.')
                    if self.wallet.balance > self.wallet.initial_balance:
                        print('You made some coins. Congrats.')
                    else:
                        print('You lost money, but at least you are not broke.')
                    continue_game = False
                    break

    def play_round(self):
        """
        Play another round.
        """
        # Reset everything.
        self.reset_game()

        # Ask player for their bet.
        self.ask_bet()

        # Draw initial set of cards.
        self.draw_initial_cards()

        # Print out first cards that were dealt.
        self.display_cards()

        # Indicate if round is complete.
        round_complete = False

        # Indicate if player already won this turn.
        player_won = False

        # Edge case: Player starts with a blackjack.
        if self.check_blackjack('player'):
            player_won = True
            self.player_result('win')
            return True

        # Ask player for actions.
        while True:
            player_action = self.player_input()
            if player_action == 'h':
                # Draw a new card.
                card = self.deck.draw_card()
                self.hands['player'].add(card)
                self.display_cards()

                if self.check_blackjack('player'):
                    player_won= True
                    self.player_result('win')
                    break
                elif self.hands['player'].total > 21:
                    # If the player has more than 21, he instantly lost.
                    self.player_result('lose')
                    round_complete = True
                    break
            else:
                print('You finished your turn. Now let the dealer play.')
                break

        # Dealer gets to play if player did not win already.
        if not player_won and not round_complete:
            self.display_cards(show_all=True)
            while True:
                # If the dealer has more than the player and less than 21, dealer wins.
                if self.hands['dealer'].total < 21 and self.hands['dealer'].total > self.hands['player'].total:
                    self.player_result('lose')
                    break
                elif self.check_blackjack('dealer'):
                    self.player_result('lose')
                    break
                elif self.hands['dealer'].total > 21:
                    self.player_result('win')
                    break
                else:
                    print('Dealer will hit again')

                # Wait for effect.
                sleep(3)

                # Let the dealer pick a card.
                card = self.deck.draw_card()
                self.hands['dealer'].add(card)
                self.display_cards(show_all=True)

# Play the game.
if __name__ == '__main__':
    game = Blackjack()
    game.play_game()
