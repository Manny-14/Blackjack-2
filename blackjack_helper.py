import random
from random import randint

# This contains the deck of cards for the players
deck = {
    1: 4, 2: 4, 3: 4, 4: 4, 5: 4, 6: 4, 7: 4, 8: 4, 9: 4, 10: 4, 11: 4, 12: 4, 13: 4
}

player_name_pool = {
    'Lily', 'Hannah', 'Caroline', 'Samuel', 'Caleb', 'Stella', 'Ava', 'Maya', 'Eleanor', 'Ivy', 'Zoey',
    'Mason', 'Lucas', 'Levi', 'Abigail', 'Adam', 'Chloe', 'Grayson', 'Henry', 'Xavier', 'Lucy', 'Eli',
    'Aiden', 'Leo', 'Mia', 'Owen', 'Hazel', 'Olivia', 'Amelia', 'Aria', 'Charlotte', 'Lila', 'Penelope',
    'Wyatt', 'Noah', 'Scarlett', 'Daniel', 'Aurora', 'Dylan', 'Oliver', 'Sebastian', 'Rose', 'Emma', 'Chase',
    'Harper', 'Audrey', 'Piper', 'Isabella', 'Logan', 'Zoe', 'Ella', 'Bella', 'Elijah', 'Grace', 'Layla',
    'Hunter', 'Ethan', 'Isaac', 'Nathan', 'Julian', 'Max', 'Sophia', 'Savannah', 'Emily', 'Jackson',
    'Isaiah', 'Ruby', 'Jack', 'Benjamin', 'Riley', 'Claire', 'Cooper', 'Addison', 'Liam'
}


def draw_card():
    hand = randint(1, 13)
    while deck[hand] == 0:
        hand = randint(1, 13)
    deck[hand] -= 1
    if hand == 1:
        value = 11
        print('Drew an Ace.')
    elif hand == 11:
        print('Drew a Jack.')
        value = 10
    elif hand == 12:
        print('Drew a Queen.')
        value = 10
    elif hand == 13:
        print('Drew a King.')
        value = 10
    elif hand == 8:
        print('Drew an', str(hand) + '.')
        value = 8
    else:
        print('Drew a', str(hand) + '.')
        value = hand
    return [value, hand]


def valid_num(strs):
    for char in strs:
        if char not in '0123456789':
            return False
    return True


def print_header(message):
    print('---------------')
    print(message)
    print('---------------')


# 0 means dealer won
# 1 means player won
# 2 means push
def determine_winner(score, dealer):
    if score == 21 and dealer != 21:
        return 1
    elif 21 > score > dealer or dealer > 21 > score:
        return 1
    elif 21 >= score == dealer:
        return 2
    else:
        return 0


class Player:

    # player can put in custom name
    def __init__(self):
        self.name = None
        self.previous = 100
        self.chips = 100
        self.bet = None
        self.fate = False
        self.hand = []
        self.current_hand = None
        self.earned = None
        self.times_played = 0

    def first_turn(self):
        store = draw_card()
        self.current_hand = store[0]
        self.hand.append(store[1])
        store = draw_card()
        self.current_hand += store[0]
        self.hand.append(store[1])
        # In the case of two Aces
        if self.hand == [1, 1]:
            self.current_hand = 12
            self.hand.remove(1)
        elif self.current_hand == 21:
            self.fate = True

    def draw_hand(self):
        store = draw_card()
        if store[0] == 1 and self.current_hand + store[0] > 21:
            self.current_hand += 1
        elif 1 in self.hand and self.current_hand + store[0] > 21:
            self.current_hand -= 10
            self.current_hand += store[0]
            self.hand.remove(1)
        else:
            self.current_hand += store[0]
        self.hand.append(store[1])

    def print_status(self):
        print(f"You have {self.current_hand}.", end='')

    def end_turn(self):
        # print('{} has {}.'.format(self.name, self.current_hand))
        if self.current_hand == 21:
            print('Blackjack!')
        elif self.current_hand > 21:
            print('Bust.')

    def result(self, dealer, result):
        if dealer.fate and not self.fate:
            print("You lose your bet to the dealer by not getting a Natural")
            self.chips -= self.bet
            self.bet = 0
        elif self.fate and not dealer.fate and dealer.current_hand != 21:
            print(f"Congratulations! You got a Natural and win 3 times your bet")
            self.earned = self.bet * 3
            self.chips += self.earned
            print(f"You win {self.earned} chips!")
        elif self.fate and not dealer.fate:
            print(f"You and the dealer got a Blackjack but you walk away with 1.5 times your bet "
                  f"due to getting a Natural!")
            self.earned = self.bet * 1.5
            self.chips += self.earned
            print(f"You win {self.earned} chips!")
        elif result == 2:
            print("You don't win or lose due to a push.")
        elif result == 0:
            print(f"You lost to the dealer and therefore lose your bet.")
        elif result == 1 and self.current_hand == 21:
            print("You win twice your bet by getting a Blackjack!")
            self.earned = self.bet * 2
            self.chips += self.earned
            print(f"You win {self.earned} chips!")
        elif result == 1:
            print(f"You win twice your bet by beating the dealer")
            self.earned = self.bet * 2
            self.chips += self.earned
            print(f"You win {self.earned} chips!")


class Bot(Player):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.chips = 100

    def print_status(self):
        print(f"{self.name} has {self.current_hand}.")

    # This function takes a dealer object and a result calculated from the determine winner function
    def result(self, dealer, result):
        if dealer.fate and not self.fate:
            print(f"{self.name} loses bet to the dealer by not getting a Natural")
            self.chips -= self.bet
            self.bet = 0
        elif self.fate and not dealer.fate and dealer.current_hand != 21:
            print(f"Congratulations! {self.name} gets a Natural and wins 3 times his bet")
            self.earned = self.bet * 3
            print(f"{self.name} wins {self.earned} chips today!")
        elif self.fate and not dealer.fate:
            print(f"Both {self.name} and the dealer got a Blackjack but {self.name} walks away with 1.5 times his bet "
                  f"due to getting a Natural!")
            self.earned = self.bet * 1.5
            print(f"{self.name} wins {self.earned} chips today")
        elif result == 2:
            print(f"{self.name} does not win or lose due to a push.")
        elif result == 0:
            print(f"{self.name} lost to the dealer and therefore loses his bet.")
        elif result == 1 and self.current_hand == 21:
            print(f"{self.name} wins twice their bet by getting a Blackjack!")
            self.earned = self.bet * 2
            print(f"{self.name} wins {self.earned} chips today")
        elif result == 1:
            print(f"{self.name} wins twice their bet by beating the dealer")
            self.earned = self.bet * 2
            print(f"{self.name} wins {self.earned} chips today")


class Dealer:

    def __init__(self):
        self.name = 'Dealer'
        self.hand = []
        self.current_hand = None
        self.fate = False

    def first_turn(self):
        store = draw_card()
        self.current_hand = store[0]
        self.hand.append(store[1])
        store = draw_card()
        self.current_hand += store[0]
        self.hand.append(store[1])
        if self.hand == [1, 1]:
            self.current_hand = 12
            self.hand.remove(1)
        elif self.current_hand == 21:
            self.fate = True

    def draw_hand(self):
        store = draw_card()
        if store[0] == 1 and self.current_hand + store[0] > 21:
            self.current_hand += 1
        elif 1 in self.hand and self.current_hand + store[0] > 21:
            self.current_hand -= 10
            self.current_hand += store[0]
            self.hand.remove(1)
        else:
            self.current_hand += store[0]
        self.hand.append(store[1])

    def end_turn(self):
        print('{} has {}.'.format(self.name, self.current_hand))
        if self.current_hand == 21:
            print('Blackjack!')
        elif self.current_hand > 21:
            print('Bust.')
