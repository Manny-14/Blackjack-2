import random

#This contains the deck of cards for the players
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

def valid_num(str):
    for char in str:
        if char not in '0123456789':
            return False
    return True

class Player:

    # player can put in custom name
    def __init__(self, name):
        self.name = name
        self.chips = 100
        self.bet = None
        self.hand = []

    def first_turn(self):
        store = draw_card()
        self.current_hand += store[0]
        self.hand.append(store[1])
        store = draw_card()
        self.current_hand += store[0]
        self.hand.append(store[1])
        if self.hand == [1, 1]:
            self.current_hand = 12

    def draw_hand(self):
        store = draw_card()
        if store[0] == 1 and self.current_hand + store[0] > 21:
            self.current_hand += 1
        elif 1 in self.hand and self.current_hand + store[0] > 21:
            store -= 10
            self.current_hand += store[0]
        else:
            self.current_hand += store[0]
        self.hand.append(store[1])

class Bot(Player):

    def __init__(self):
        self.name = random.choice(list(player_name_pool))
        self.chips = 100
        self.hand = []


