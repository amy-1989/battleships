from random import randint

def welcome_screen():
    """
    Displays welcome message to the player and
    home screen
    """

    print('Welcome to BattleShips')
    print('First time player [F]')
    print('Returning player [R]')
    print('How to Play [H]')
    player_start_screen_choice = input('Please input one of the above letters to continue: ').upper()
    if player_start_screen_choice == 'F':
        print('You have chosen First time player')
        return start_game()
    elif player_start_screen_choice == 'R':
        print('You have chosen Returning player')
    elif player_start_screen_choice == 'H':
        return how_to_play()
    else:
        print('Player input is invalid. Please try again')
        player_start_screen_choice = input('Please input one of the above letters to continue: ').upper()

def how_to_play():
    """
    Displays instructions on how to play battleships
    """
    print('Battleships is a game where the player tries to sink the computers ships.')
    print('You will have 10 tries to find and sink the ships.')
    print('There are 5 levels, each one progressively harder than the one before.')
    print('You must win the previous level by sinking the computers ships to move on to the next level.')
    print('At the end of your first playthrough you will be given the option to save your username and score.')
    print('How many tries will it take you to get through all 5 levels and beat the game?')
    print('To begin, enter [Y], to exit, enter [N]')

    player_how_to_play_choice = input('Enter your choice here: ').upper()
    if player_how_to_play_choice == 'Y':
        return start_game()
    elif player_how_to_play_choice == 'N':
        return welcome_screen()
    else:
        print('Player input is invalid. Please try again')
        player_how_to_play_choice = input('Enter your choice here: ').upper()
        

computer_board = [[' ']*5 for x in range(5)]
player_board = [[' ']*5 for x in range(5)]

letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4,}

def create_game_board(board):
    """
    Creates the gameboard for playing the battleships game
    """
    print('  A B C D E')
    print(' -----------')
    row_num = 1
    for row in board:
        print('%d|%s|' % (row_num, '|'.join(row)))
        row_num += 1

def find_ship_location():
    """
    to allow the player to input their guess as to 
    where the ships location is and try to sink it
    """    
    row = input('Please enter a ship row between 1 & 5: ')
    while row not in '12345':
        print('Please enter a valid row')
        row = input('Please enter a ship row between 1 & 5: ')
    
    column = input('Please enter a ship column between A & E: ').upper()
    while column not in 'ABCDE':
        print('Please enter a valid column')
        column = input('Please enter a ship column between A & E: ').upper()
    return int(row)-1, letters_to_numbers[column]
        
def create_battleships(board):
    """
    randomly generates positions for the 3 ships on the board
    """
    for ship in range(3):
        ship_r, ship_cl = randint(0, 4), randint(0, 4)
        while board[ship_r][ship_cl] == 'X':
            ship_r, ship_cl = randint(0, 4), randint(0, 4)
        board[ship_r][ship_cl] = 'X'

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

def start_game():
    """
    Runs the battleship game
    """
    create_battleships(computer_board)
    turns = 10
    while turns > 0:
        print('Welcome to Battleships')
        create_game_board(player_board)
        row, column = find_ship_location()
        if player_board[row][column] == '-':
            print('You already guessed that!')
        elif computer_board[row][column] == 'X':
            print('Congratulations! You have sunk a battleship')
            player_board[row][column] = 'X'
            turns -= 1
        else:
            print('Sorry! You missed!')
            player_board[row][column] = '-'
            turns -= 1
        if count_sunk_ships(player_board) == 3:
            print('Congratulations! You have sunk all the battleships! You have won!')
            break
        if turns == 0:
            print('Game Over! You have ran out of turns!')
            break


welcome_screen()


