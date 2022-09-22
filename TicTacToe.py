# Chapter 5, Program Development Problem 3
# Tic-Tac-Toe Two-Player Program
# Author: Emily Shull

# Develop and test a Python program that lets two players play tic-tac-toe.
# Let player 1 be X and player 2 be O. Devise a method for each player to
# indicate where they wish to plac their symbol. The program should terminate
# if either there is a winner, or if the game results in a tie. The tic-tac-toe
# board should be displayed after every move as shown.

import random


def displayWelcome():
    """Displays messages to welcome the user to Tic-Tac-Toe and explains basic rules. No inputs or returns."""
    print('>>Welcome to Tic-Tac-Totally Fun!')
    print('>>You will be playing Tic-Tac-Toe against the computer.')
    print('>>The goal of Tic-Tac-Toe is to get three of your symbols in a row - ',
          'either horizontally, vertically, or diagonally.')


def displayCurrentBoard(curr_board):
    """
    Prints a picture of the tic-tac-toe board at the current state. No returns.

    Input: curr_board is a list of 9 string values.
    """
    print(curr_board[0], '|', curr_board[1], '|', curr_board[2])
    print('---------')
    print(curr_board[3], '|', curr_board[4], '|', curr_board[5])
    print('---------')
    print(curr_board[6], '|', curr_board[7], '|', curr_board[8])


def initBoard():
    """
    Initializes a list of 9 string values to start the game in a clean board state. Calls displayCurrentBoard,
    populating it with the initialized list.

    Return: starter_board is a list of 9 string literals of the numbers 1 through 9.
    """
    starter_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    print('\n>>Here is the starting board: ')
    displayCurrentBoard(starter_board)
    print('\n>>You will enter the number of the spot that corresponds to the location',
          'you would like to put your symbol.')

    return starter_board


def decidePlayerSymbols():
    """
    Asks user input to decide user symbol selection. Asks for verification of selection.

    Return: user_selection is either the string 'X' or the string 'O'.
    """
    user_selection = input('Enter either X or O to select your symbol: ').upper()
    while user_selection not in ('X', 'O'):
        user_selection = input('Please enter either X or O to select your symbol: ').upper()

    print('\n>>Congratulations! You have selected ', user_selection, ' as your symbol.')
    double_check = input('Is that the correct symbol choice? (y/n): ').upper()

    while double_check not in ('Y', 'N'):
        double_check = input('Is that the correct symbol choice? (y/n): ').upper()

    if double_check == 'N':
        user_selection = decidePlayerSymbols()

    return user_selection


def chooseTurnOrder(initial_board):
    """
    Asks user input for turn order preference (user first or computer first). Calls displayCurrentBoard to
    show the initial board state for the user if they choose to go first.

    Input: initial_board is a list of 9 string literals of the numbers 1 through 9.
    Return: a boolean value for whether the computer will go first (True) or if the user will go first (False).
    """
    go_first = input('\nDo you want to go first? (y/n): ').upper()

    if go_first != 'Y':
        print("\n>>OK! I'll go first, then!")
        return True
    else:
        print("\n>>You first, then!")
        displayCurrentBoard(initial_board)
        return False


def constructTurnOrder(computer_first):
    """
    Begins the gameplay cadence. Calls computerTurn to get a response for the computer turn.
    Calls userTurn to get a response for the turn of the user. Calls determineWinner to check
    the current board state against all possible win and tie conditions.

    Input: computer_first is a boolean value for whether the computer goes first (True) or if the user
    will go first (False).
    Return: has_won is a boolean value for whether a winner has been identified (True) or
    if the game is still ongoing (False).
    """
    has_won = False
    turn_counter = 1
    while turn_counter <= 9 and not has_won:
        if computer_first:
            current_board = computerTurn(board, computer_symbol)
            if turn_counter >= 5:
                has_won = determineWinner(current_board, turn_counter, 'computer')
        else:
            current_board = userTurn(board, user_symbol)
            if turn_counter >= 5:
                has_won = determineWinner(current_board, turn_counter, 'user')

        computer_first = not computer_first
        turn_counter = turn_counter + 1

    return has_won


def computerTurn(curr_board, symbol):
    """
    Computer turn enforces one business rule: on the computer's first turn, if the middle position of
    the board has not been claimed, the computer will claim it. Otherwise, a random number between
    1-9 is generated, with retry logic if the number has already been claimed. Calls displayCurrentBoard
    after turn has been taken to show current board state.

    Input:
        curr_board is a list of 9 string values - a mixture of the numbers 1 through 9 and X's and O's
        depending on the turn.
        symbol is the string 'X' or the string 'O', the inverse of the user selection.
    Return: curr_board is a list of 9 string values - a mixture of the numbers 1 through 9 and X's and O's
    depending on the turn.
    """
    if curr_board[4] not in ('X', 'O'):
        selected_value = 5
    else:
        selected_value = random.randint(1, 9)

    while curr_board[selected_value - 1] in ('X', 'O'):
        selected_value = random.randint(1, 9)

    curr_board[selected_value - 1] = symbol

    print("\n>>I've updated slot ", str(selected_value), ' to "', symbol, '".')
    displayCurrentBoard(curr_board)

    return curr_board


def userTurn(curr_board, symbol):
    """
    Asks for user input to populate a position on the grid with their symbol. Has retry logic for unclean
    user inputs. Calls displayCurrentBoard after turn has been taken to show current board state.

    Input:
        curr_board is a list of 9 string values - a mixture of the numbers 1 through 9 and X's and O's
        depending on the turn.
        symbol is the string 'X' or the string 'O', based off the user's previous selection.
    Return: curr_board is a list of 9 string values - a mixture of the numbers 1 through 9 and X's and O's
    depending on the turn.
    """
    user_location_choice = input('\nChoose a single digit between 1 and 9 to place your symbol: ')

    happy_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    while user_location_choice not in happy_list:
        user_location_choice = input('\nPlease choose a single digit between 1 and 9 to place your symbol: ')

    user_location_choice = int(user_location_choice)
    while curr_board[user_location_choice - 1] in ('X', 'O'):
        print('>>Sorry! That spot is taken. Please try again.')
        displayCurrentBoard(curr_board)
        user_location_choice = int(input('\nChoose a single digit between 1 and 9 to place your symbol: '))

    curr_board[user_location_choice - 1] = symbol

    nice_adjectives = ['Good play!', 'Nice choice!', 'Excellent pick!', "You're a genius!"]
    nice_adjectives_index = random.randint(0, 3)
    print("\n>>I've updated slot ", str(user_location_choice), ' to "', symbol, '". ',
          nice_adjectives[nice_adjectives_index])
    displayCurrentBoard(curr_board)

    return curr_board


def determineWinner(board_to_check, num_turns, current_player):
    """
    Checks the board state to see if any win or tie conditions have been met. Prints unique messaging
    based off if the user wins, if the computer wins, or if there is a tie.

    Input:
        board_to_check is a list of 9 string values - a mixture of the numbers 1 through 9 and X's and O's
        depending on the turn.
        num_turns is an integer 1-9 that describes the number of turns that have been taken in total
        by the user and the computer.
        current_player is the string 'user' or the string 'computer' to detail which player was responsible
        for the last turn action.
    Return: has_winner is a boolean value for if a win or tie condition has been met (True), or if
    no winner has been identified (False) so that play can continue.
    """
    has_winner = False

    if board_to_check[0] == board_to_check[1] == board_to_check[2]:
        has_winner = True
    elif board_to_check[3] == board_to_check[4] == board_to_check[5]:
        has_winner = True
    elif board_to_check[6] == board_to_check[7] == board_to_check[8]:
        has_winner = True
    elif board_to_check[0] == board_to_check[3] == board_to_check[6]:
        has_winner = True
    elif board_to_check[1] == board_to_check[4] == board_to_check[7]:
        has_winner = True
    elif board_to_check[2] == board_to_check[5] == board_to_check[8]:
        has_winner = True
    elif board_to_check[0] == board_to_check[4] == board_to_check[8]:
        has_winner = True
    elif board_to_check[2] == board_to_check[4] == board_to_check[6]:
        has_winner = True

    if has_winner:
        if current_player == 'computer':
            print('>>Looks like I won, better luck next time!')
        else:
            print('>>Congratulations! You are the winner!')
    elif not has_winner and num_turns == 9:
        print(">>Looks like there's a tie!")
        print(">>Does that mean we're both winners, or are we both losers?")
        has_winner = True

    return has_winner


def playAgain():
    """
    Prompts the user after a win or tie has been declared for input on whether they would
    like to play again. If the response is anything but 'Y', the program quits.

    Return: a boolean value for if the user would like to play again (True), or if the game instance
    should be ended (False).
    """
    come_play_with_us = input('\nDo you want to play again? (y/n): ').upper()

    if come_play_with_us != 'Y':
        print('\n>>Okay! Have a nice day! :)')
        return False
    else:
        print("\n>>Let's do it again!")
        print(">>We'll keep our same symbols.")
        return True


# ---- main
displayWelcome()
board = initBoard()

print('\n>>First things first, we need to identify which symbol you want to play.')
user_symbol = decidePlayerSymbols()

# assigns the opposite symbol to the computer based off the user's selected symbol
computer_symbol = ''
if user_symbol == 'X':
    computer_symbol = 'O'
else:
    computer_symbol = 'X'

comp_goes_first = chooseTurnOrder(board)

game_over = constructTurnOrder(comp_goes_first)

# once a winner has been declared, the user is prompted to play again
if game_over:
    lets_play_a_game = playAgain()
    # switches the starting player when game begins again
    # first iteration is the opposite of the original value of comp_goes_first
    reverse_order = not comp_goes_first

    # loops as many times as user consents to playing again
    while lets_play_a_game:
        # restarts game by re-initializing the board
        board = initBoard()

        if reverse_order:
            print("\n>>Since you went first last time, I'll start this game!")
        else:
            print("\n>>I started last time, so you should start this game!")
            displayCurrentBoard(board)

        constructTurnOrder(reverse_order)

        lets_play_a_game = playAgain()
        # switches the starting player when game begins again
        # after the first iteration, order is the opposite of the current value of reverse_order
        reverse_order = not reverse_order
