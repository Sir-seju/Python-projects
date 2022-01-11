from __future__ import print_function
import os
import time

def board_display(board):
    #a function that displays a 3x3 board with an index 1-9
    os.system('cls')
    print ('\t\t\t'  'TIC\tTAC\tTOE')
    print ('\n')
    print ('\t\t\t',  board[1], ' | ', board[2] ,' | ', board[3], '')  
    print ('\t\t      ------------------')
    print ('\t\t\t',  board[4], ' | ', board[5] ,' | ', board[6], '')
    print ('\t\t      -------------------')
    print ('\t\t\t',  board[7], ' | ', board[8] ,' | ', board[9], '')


def player_input():
    #This function takes in two player names and assigns markers to both.
    marker = ""
    global p1name
    global p2name
    p1name = input('Enter name for player 1: ')
    p2name = input('Enter name for player 2: ')
    while marker != 'X' or marker != 'O':
        marker = input('%s choose a marker "X" / "O" : ' %(p1name)).upper()
        if marker == 'X':
            print(' %s is assigned the "O" marker ' %(p2name))
            return ('X','O')
        elif marker == 'O':
            print(' %s is assigned the "X" marker ' %(p2name))
            return ('O','X')
        else:
            print('%s provided wrong input! choose between "X" / "O" : ' %(p1name))
            continue

def place_marker(board, marker, position):
    #This assigns positions on the board with a marker and checks winning patterns of the tic-tac-toe game.
    if board[position] == ' ':
        board[position] = marker
    else:
        print('that position is taken! choose again: ')

def win_check(board,marker):
    return ((board[1] == board[2] == board[3] == marker) or
            (board[4] == board[5] == board[6] == marker) or
            (board[7] == board[8] == board[9] == marker) or
            (board[1] == board[4] == board[7] == marker) or
            (board[2] == board[5] == board[8] == marker) or
            (board[3] == board[6] == board[9] == marker) or
            (board[1] == board[5] == board[9] == marker) or
            (board[7] == board[5] == board[3] == marker)) 

#Step 5: Write a function that uses the random module to randomly decide which player goes first.
#Return a string of which player went first.
import random
def go_first():
    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

 #Step6: Write a function that returns a boolean indicating whether a space on the board is freely available.
 
def board_space_check(board,position):
    return board[position] == " "
    
#Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.

def board_full_check(board):
    for i in range(1,10):
        if board_space_check(board,i):
            return False
    return True

#Step 8: Write a function that asks for a player's next position (as a number 1-9)
# and then uses the function from step 6 to check if its a free position. 
# If it is, then return the position for later use.
    
def player_position(board):
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not board_space_check(board, int(position)):
        position = input('Choose your next position: (1-9) ')
    return int(position)
# Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again

def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


print ('Welcome to Uwasans\'s Tik-tok game')
while True:
    board = [" "]*10
    player1_marker, player2_marker = player_input()
    time.sleep(.5)
    turn = go_first()

    game_on = True

    while game_on:
        #player 1 turn
        if turn == 'Player 1':
            board_display(board)
            print('your turn', p1name)
            position = player_position(board)
            place_marker(board, player1_marker, position)
            if win_check(board, player1_marker):
                board_display(board)
                print('Congratulations', p1name, '! You have won the game')
                game_on = False
            else:
                if board_full_check(board):
                    board_display(board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'
    
        else:
            board_display(board)
            print('your turn', p2name)
            position = player_position(board)
            place_marker(board, player2_marker, position)
            if win_check(board, player2_marker):
                board_display(board)
                print('Congratulations', p2name,'! You have won the game!')
                game_on = False
            else:
                if board_full_check(board):
                    board_display(board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break




