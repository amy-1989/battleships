# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
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
        return welcome_screen()

def how_to_play():
    """
    Displays instructions on how to play battleships
    """
    print('Battleships is a game where the player tries to sink the computers ships before the computer sinks theirs.')
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
        return how_to_play()


welcome_screen()