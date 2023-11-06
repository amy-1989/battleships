from random import randint
import sys
from random_username.generate import generate_username
import gspread
from google.oauth2.service_account import Credentials
from time import sleep
from colorama import Fore

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('battleships_save_data')


def welcome_screen():
    """
    Displays welcome message to the player and
    home screen
    """
    print(Fore.BLUE + 'Welcome to BattleShips')
    print(Fore.YELLOW + 'First time player [F]')
    print(Fore.YELLOW + 'How to Play [H]')
    print(Fore.RED + 'To exit, enter [Q]')
    player_start_screen_choice = input(Fore.GREEN + 'Please input a letter: \n').upper()
    if player_start_screen_choice == 'F':
        print(Fore.GREEN + 'You have chosen First time player')
        return first_time_player()
    elif player_start_screen_choice == 'H':
        return how_to_play()
    elif player_start_screen_choice == 'Q':
        sys.exit()
    else:
        print(Fore.RED +'Player input is invalid. Please try again')
        player_start_screen_choice = input('Please input a letter: ').upper()


def how_to_play():
    """
    Displays instructions on how to play battleships
    """
    print('The player tries to sink the computers ships.')
    print('You will have 10 tries to find and sink the ships.')
    print('There are 5 levels, each one harder than the one before.')
    print('Sink all the computers ships to move on to the next level.')
    print('At the end you may save your username and score.')
    print('How many tries will it take you to beat the game?')
    print('To begin, enter [Y], to exit, enter [N]')
    print('To quit at anytime during the game, input Q \n')

    player_choice = input(Fore.GREEN + 'Enter your choice here: ').upper()
    if player_choice == 'Y':
        return welcome_screen()
    elif player_choice == 'N':
        sys.exit()
    elif player_choice == 'Q':
        sys.exit()
    else:
        print(Fore.RED + 'Player input is invalid. Please try again \n')
        player_choice = input(Fore.GREEN + 'Enter your choice here: ').upper()


def first_time_player():
    player_username = generate_username(1)
    print(player_username)
    print(Fore.RED + 'Please remember the above username for replays \n')
    levels_worksheet = SHEET.worksheet('usernames')
    levels_worksheet.append_row(player_username)
    sleep(2)
    main()


computer_board = [[' ']*5 for x in range(5)]
player_board = [[' ']*5 for x in range(5)]

letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, }


def count_sunk_ships(board):
    """
    counts the ships that have been sunk
    """
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count


def create_game_board(board):
    """
    Creates the gameboard for playing the battleships game
    """
    print(Fore.YELLOW + '  A B C D E')
    print(' -----------')
    row_num = 1
    for row in board:
        print(Fore.YELLOW + '%d|%s|' % (row_num, '|'.join(row)))
        row_num += 1


def find_ship_location():
    """
    to allow the player to input their guess as to 
    where the ships location is and try to sink it
    """
    row = input('Please enter a ship row between 1 & 5: ').upper()
    if row == 'Q':
        sys.exit()
    elif row == "":
        print('Please enter a valid row')
        row = input('Please enter a ship row between 1 & 5: ')
    else:
        while row not in '12345':
            print('Please enter a valid row')
            row = input('Please enter a ship row between 1 & 5: ')
        
    column = input('Please enter a ship column between A & E: ').upper()
    if column == 'Q':
        sys.exit()
    elif column == "":
        print('Please enter a valid column')
        column = input('Please enter a letter between A & E: ').upper()
    else:
        while column not in 'ABCDE':
            print('Please enter a valid column')
            column = input('Please enter a letter between A & E: ').upper()
        
    return int(row)-1, letters_to_numbers[column]


def create_battleships(board):
    """
    randomly generates positions for the 3 ships on the board
    """
    for ship in range(3):
        ship_r, ship_cl = randint(0, 4), randint(0, 4)
        while computer_board[ship_r][ship_cl] == 'X':
            ship_r, ship_cl = randint(0, 4), randint(0, 4)
        computer_board[ship_r][ship_cl] = 'X'


def main():
    """
    Runs the battleship game
    """
    create_battleships(computer_board)
    turns = 30

    while turns > 0:
        print(Fore.BLUE + 'Welcome to Battleships \n')
        create_game_board(player_board)
        row, column = find_ship_location()
        if player_board[row][column] == '-':
            print(Fore.YELLOW + 'You already guessed that!')
            sleep(1)
        elif computer_board[row][column] == 'X':
            print(Fore.GREEN + 'Congratulations! You have sunk a battleship')
            sleep(1)
            player_board[row][column] = 'X'
            turns -= 1
        else:
            print(Fore.RED + 'Sorry! You missed!')
            sleep(1)
            player_board[row][column] = '-'
            turns -= 1
        if count_sunk_ships(player_board) == 3:
            print(Fore.GREEN + 'You have sunk all the battleships! You have won!')
            sleep(2)
            sys.exit()
        if turns == 0:
            print(Fore.RED + 'Game Over! You have ran out of turns!')
            sleep(2)
            sys.exit()


welcome_screen()
