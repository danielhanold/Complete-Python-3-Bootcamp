"""
Blackjack Game
"""
from deck import DeckGenerator
from wallet import Wallet
from random import randint
from time import sleep

class Blackjack():
    def __init__(self):
        # Set up the player's wallet.
        self.wallet = Wallet()

        # Create a way to generate new cards.
        self.deck_generator = DeckGenerator()

        # Reset the game.
        self.reset_game()

    def reset_game(self):
        """
        Reset all game variables for a new round.
        """
        # The player always goes first.
        self.current_turn = 'player'

        # Set the current cards to an empty array.
        self.cards = {
            'dealer': [],
            'player': []
        }

        # Set the totals for each player.
        self.totals = {
            'dealer': 0,
            'player': 0
        }

        # Create a new new deck of cards.
        self.deck = self.deck_generator.get_new_deck()


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

    def draw_card(self):
        """
        Draw a single card and return it.
        """
        index_options = len(self.deck) - 1
        random_index = randint(0, index_options)
        return self.deck.pop(random_index)

    def draw_initial_cards(self):
        """
        Draw initial cards for player and dealer.
        """

        # Draw cards for player and dealer.
        for current in ('dealer', 'player'):
            for i in range(0, 2):
                card = self.draw_card()
                self.cards[current].append(card)

    @staticmethod
    def format_card(card):
        """ Displays a single card tuple """

        card_value = str(card[1]).capitalize()
        card_suit = card[0].capitalize()
        return "{} of {}".format(card_value, card_suit)

    def display_cards(self):
        """
        Display all cards for the player and dealer.
        """
        message = "{}'s cards: {}"

        for player in ['dealer', 'player']:
            # Format the cards correctly.
            cards = [self.format_card(card) for card in self.cards[player]]

            # If it's the player's turn, do not display the second card of the dealer.
            if self.current_turn == 'player' and player == 'dealer':
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

    def tally_up_cards(self):
        """
        Tally up all the cards for each player.
        """
        for player in ['dealer', 'player']:
            self.totals[player] = self.check_cards(player)


    def check_cards(self, player):
        """
        Check the cards for the specified player.
        """
        total = 0
        for card in self.cards[player]:
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
        aces = list(filter(lambda card: card[1] == 'ace', self.cards['player']))
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

        return total

    def display_totals(self):
        """
        Display the totals for this round.
        """
        print()
        print("---- Results for this round ----")
        self.display_cards()
        print("Dealer total is: {}".format(self.totals['dealer']))
        print("Player total is: {}".format(self.totals['player']))

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
            message = 'You lost this round your bet of {}.'

        print(message.format(self.bet))
        print('Coins in your wallet are now: {}'.format(self.wallet.get_balance()))

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
                        print('You made some money. Congrats')
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

        # Tall up initial cards.
        self.tally_up_cards()

        # Indicate if round is complete.
        round_complete = False

        # Indicate if player already won this turn.
        player_won = False

        # Edge case: Player starts with a blackjack.
        if self.totals['player'] == 21:
            # If the player has more 21, he instantly won.
            print("BLACKJACK!!!!")
            player_won = True
            self.player_result('win')
            return True

        # Ask player for actions.
        while True:
            player_action = self.player_input()
            if player_action == 'h':
                # Draw a new card.
                card = self.draw_card()
                self.cards[self.current_turn].append(card)
                self.display_cards()
                self.tally_up_cards()

                if self.totals['player'] == 21:
                    # If the player has more 21, he instantly won.
                    print("BLACKJACK!!!!")
                    player_won= True
                    self.player_result('win')
                    break
                elif self.totals['player'] > 21:
                    # If the player has more than 21, he instantly lost.
                    self.player_result('lose')
                    round_complete = True
                    break
            else:
                print('You finished your turn. Now let the dealer play.')
                break

        # Dealer gets to play if player did not win already.
        if not player_won and not round_complete:
            self.current_turn = 'dealer'
            self.display_cards()
            while True:
                # If the dealer has more than the player and less than 21, dealer wins.
                if self.totals['dealer'] < 21 and self.totals['dealer'] > self.totals['player']:
                    self.player_result('lose')
                    break
                elif self.totals['dealer'] == 21:
                    print('Dealer has Blackjack')
                    self.player_result('lose')
                    break;
                elif self.totals['dealer'] > 21:
                    self.player_result('win')
                    break
                else:
                    print('Dealer will hit again')

                # Wait for effect.
                sleep(3)

                # Let the dealer pick a card.
                card = self.draw_card()
                self.cards[self.current_turn].append(card)
                self.display_cards()
                self.tally_up_cards()

# Play the game.
if __name__ == '__main__':
    game = Blackjack()
    game.play_game()
