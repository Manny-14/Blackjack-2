from blackjack_helper import *
import random


def run_game():
    # User turn
    print("Welcome to the Blackjack Casino!")
    user_name = input("What will you like to be called? ")
    user = Player(user_name)
    print("Hello {}! Nice to meet you!".format(user_name))
    player1 = Bot(random.choice(list(player_name_pool)))
    player2 = Bot(random.choice(list(player_name_pool)))
    player3 = Bot(random.choice(list(player_name_pool)))
    player_list = [player1, player2, player3]
    print("Today you will be playing with {}, {} and {}!".format(player1.name, player2.name, player3.name))
    user_bet = input("You have {} chips left! Please place a bet ".format(user.chips))

    # This while loop is to ensure a valid bet is placed
    while not valid_num(user_bet):
        print("Invalid number! Make sure to input an integer within the range of 20 to 100")
        user_bet = input("You have {} chips left! Place a bet ".format(user.chips))
        if valid_num(user_bet):
            while int(user_bet) < 20 or int(user_bet) > user.chips:
                if int(user_bet) < 20:
                    print("A minimum of 20 chips is allowed for entry!")
                    user_bet = input("You have {} chips left! Place a bet ".format(user.chips))
                elif int(user_bet) > user.chips:
                    user_bet = input("You have only {} chips left! Place a bet ".format(user.chips))
                if not valid_num(user_bet):
                    break
    user_bet = int(user_bet)
    print("You have decided to bet {} chips!".format(user_bet))
    # If the bet is valid, the bet is stored somewhere and the user chips get subtracted from
    user.bet = user_bet
    user.chips -= user_bet

    for player in player_list:
        possible_bets = [20, 20, 20, 20, 30, 30, 30, 30, 40, 40, 40, 40, 50, 50, 50, 60, 60, 70, 80, 90, 100]
        player_bet = random.choice(possible_bets)
        while player_bet > player.chips:
            player_bet = random.choice(possible_bets)
        print(f"{player.name} is betting {player_bet} chips!")
        player.chips -= player_bet
        player.bet = player_bet

    print("Let the games begin")
    print_header(f"{user.name}'s Turn!")

    # Player's turn to play
    user.first_turn()
    user.print_status()
    if user.current_hand < 21:
        user_turn = input(' Hit (y/n)? ')
        while user_turn != 'n' and user.current_hand < 21:
            while user_turn != 'y' and user_turn != 'n':
                user_turn = input("Sorry, that's not a valid response. Hit (y/n)? ").lower()
            user.draw_hand()
            if user.current_hand < 21:
                user.print_status()
                user_turn = input(' Hit (y/n)? ').lower()

    user.end_turn()

    # Other Player's turn
    for player in player_list:
        print_header(f'{player.name}\'s Turn!' )
        player.first_turn()
        if player.current_hand >= 21:
            player.end_turn()
            continue
        response = randint(0, 1)
        if response == 0:
            print(f'{player.name} has decided to stay!')
            player.print_status()
            continue
        while response == 1 and player.current_hand < 21:
            print(f"{player.name} has decided to hit!")
            player.draw_hand()
            player.print_status()
            response = randint(0, 1)
        player.end_turn()


run_game()
