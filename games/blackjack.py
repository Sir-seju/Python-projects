"""
This is a blackjack game where you compete with the dealer to see who
can get a closer value to 21 with their cards.
"""

import time
import os
import random

class Card:
    """Create a Card class with a show method"""
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def show(self):
        """ A print method for the cards"""
        print(f'{self.rank} of {self.suit}')


values = {'Ace': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
          '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10}


class Deck:
    def __init__(self, value=0):
        self.cards = []
        self.value = value
        self.autobuild()  # Auto call this method to build a deck of cards
        self.card_value()  # Auto call this to assign values to each card in the deck

    def build(self):
        for suit in ['Spades', 'Hearts', 'Diamonds', 'Clubs']:
            for rank in ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']:
                self.cards.append(Card(rank, suit))

    def autobuild(self):
        """ Build the deck of cards"""
        self.build()
        self.build()

    def card_value(self):
        """Asssign a value to each card"""
        for card in self.cards:
            card.value = values['%s' % (card.rank)]

    def show(self):
        """show method for cards"""
        for card in self.cards:
            card.show()

    def shuffle(self):
        """shuffle method for cards"""
        for i in range(len(self.cards)-1, 0, -1):
            rand = random.randint(0, i)
            self.cards[i], self.cards[rand] = self.cards[rand], self.cards[i]

    def draw_card(self):
        """draw method from deck of cards"""
        return self.cards.pop()


class Player:
    def __init__(self, name, balance=10000.0):
        self.name = name
        self.balance = balance
        self.hand = []
        self.ace = 0
        self.hand_value = 0
        self.blackjack = False

    def bet(self):
        while True:
            try:
                player.show_balance()
                amount = float(input('Place your bets: '))
                while amount > self.balance:
                    amount = float(input(
                        'Your balance cannot fund this amount! choose an amount less '
                        'than or equal to %s: ' % (self.balance)))
            except:
                print('Wrong input! Try again')
                continue
            else:
                self.balance -= amount
                return amount

    def show_balance(self):
        print('%s your balance is %s' % (self.name, self.balance))

    def deposit(self, sum):
        self.balance += sum

    def draw(self, deck):
        a = [deck.draw_card()]
        for card in a:
            self.hand_value += card.value
            self.hand.append(card)
            if card.rank == 'Ace':
                self.ace += 1
        print('%s draws' % (self.name))

    def show_hand(self):
        for card in self.hand:
            card.show()
        self.catch_ace()
        if len(self.hand) == 2 and self.ace == 1 and self.hand_value == 21:
            self.blackjack = True

    def catch_ace(self):
        for x in range(self.ace):
            if self.hand_value > 21:
                self.ace -= 1
                self.hand_value -= 10

    def declare_hand(self):
        print('Value of cards in %s\'s hand is %s' %
              (self.name, self.hand_value))

    def reset_hand(self):
        self.hand = []
        self.hand_value = 0
        self.ace = 0
        return self


class Dealer(Player):
    def __init__(self):
        Player.__init__(self, name='Dealer')


def player_input():
    choice = ''
    while choice != 'H' or choice != 'S':
        choice = input(' do you want to "hit" or "stand" h/s?: ').upper()
        if choice == "H" or choice == 'S':
            return choice
        else:
            print('Wrong input! Choose between "h" / "s"! ')
            continue


def hit():
    print("-----------------")
    player.draw(deck)
    player.show_hand()
    player.declare_hand()
    time.sleep(2)


def stand():
    print("-----------------")
    player.declare_hand()
    time.sleep(1)
    while dealer.hand_value < 17:
        dealer.draw(deck)
        dealer.show_hand()
        time.sleep(1.5)
    dealer.declare_hand()


def ingame_check():
    if player.hand_value > 21:
        print('Bust! You lose!')
        time.sleep(3)
        return True
    return False


def bj_check():
    if player.blackjack == True and dealer.hand_value < 21:
        return True


def win_check():
    if player.hand_value > dealer.hand_value and player.hand_value < 22:
        return True
    elif dealer.hand_value > 21 and player.hand_value < 22:
        return True
    else:
        return False


def draw_check():
    if dealer.blackjack == True and player.blackjack == True:
        return True
    return (dealer.hand_value == player.hand_value and dealer.hand_value < 22)


def game_eval():
    while True:
        if dealer.hand_value > 21:
            print('Bust for dealer!')
            time.sleep(1)
            print('Congratulations %s! you win!' % (player.name))
            player.balance += bet*2
            player.show_balance()
            time.sleep(3)
            break
        if bj_check():
            print('Blackjack!! you win')
            player.balance += bet*3
            player.show_balance()
            time.sleep(3)
            break
        if win_check():
            print('Congratulations %s! you win!' % (player.name))
            time.sleep(1)
            player.balance += bet*2
            player.show_balance()
            time.sleep(3)
            break
        if draw_check():
            print('The game is a draw!')
            time.sleep(1)
            player.balance += bet
            player.show_balance()
            time.sleep(3)
            break
        else:
            print('Sorry! You lose!')
            time.sleep(3)
            break


def play_again():
    global no
    func = input('Play again? "y" / "n": ').upper()
    if func == 'Y':
        return True
    else:
        no = True


print('Welcome to Uwasan\'s BlackJack Game!')
game_on = True
while game_on:
    os.system('clear')
    time.sleep(.5)
    player_name = input('Enter player name: ')
    player = Player('%s' % (player_name))
    time.sleep(2)
    print(f"Hello {player_name}!")
    time.sleep(1)
    print(
        f"The amount of money you have to bet in this game is {player.balance}"
        " \nGoodluck and bet wisely!")
    time.sleep(2)
    dealer = Dealer()
    deck = Deck()
    deck.shuffle()
    start_game = True
    no = False
    while start_game:
        ingame = True
        while ingame:
            os.system('clear')
            player.reset_hand()
            dealer.reset_hand()
            bet = player.bet()
            os.system('clear')
            time.sleep(1)
            print("-----------------")
            dealer.draw(deck)
            time.sleep(1)
            dealer.show_hand()
            time.sleep(1)
            print("-----------------")
            player.draw(deck)
            time.sleep(1)
            player.draw(deck)
            time.sleep(1)
            player.show_hand()
            time.sleep(1)
            print("-----------------")
            player.declare_hand()
            time.sleep(2)
            Choice = player_input()
            if Choice == 'H':
                hit()
                if ingame_check():
                    break
                else:
                    Choice2 = player_input()
                    if Choice2 == 'H':
                        hit()
                        if ingame_check():
                            break
                        else:
                            Choice3 = player_input()
                            if Choice3 == 'H':
                                hit()
                                if ingame_check():
                                    break
                                else:
                                    stand()
                                    game_eval()
                                    break
                            else:
                                stand()
                                game_eval()
                                break
                    else:
                        stand()
                        game_eval()
                        break
            else:
                stand()
                game_eval()
                break

        if player.balance < 100:
            print('Game over!')
            game_on = False
            break
        play_again()
        if no == True:
            game_on = False
            break
        continue

print("Thanks for playing my blackjack game")
print("-----------------")
time.sleep(2)
