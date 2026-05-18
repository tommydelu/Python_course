# This code implements the classic Tic Tac Toe game.

"""
To choose a position to insert your sign take this layout as reference, each number represent the index

0   |   1   |   2   |
3   |   4   |   5   |
6   |   7   |   8   |
"""

def displayBoard(board):

    # This function displays the board

    string_board = f"""
    {board[0]} | {board[1]} | {board[2]} |
    -------------
    {board[3]} | {board[4]} | {board[5]} |
    -------------
    {board[6]} | {board[7]} | {board[8]} |
    
"""
    print(string_board)

def chooseSign():

    # This function assigns a symbol to each player
    choice = ''
    while choice != 'X' and choice !='O':

        choice = input('Player 1, choose your marker: ')

        if choice =='X':
            return 'X','O'

        elif choice =='O':
            return 'O','X'
        else:
            print('Incorrect input, try again')

def who_starts():

    # Function that decides who starts first
    import random
    a = random.randint(0,1)
    if a == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def choose_position():
    # The player choose a position to insert it's sign
    res = int(input('Choose a position: '))
    return res

def make_move(board,position,sign):
    # Update the board with the player's choice
    board[position]=sign

def check_win(board,sign):
    # This function checks if a player won the game or not
    if  (board[0]==sign and board[1]==sign and board[2]==sign) or \
        (board[3]==sign and board[4]==sign and board[5]==sign) or \
        (board[6]==sign and board[7]==sign and board[8]==sign) or \
        (board[0]==sign and board[3]==sign and board[6]==sign) or \
        (board[1]==sign and board[4]==sign and board[7]==sign) or \
        (board[2]==sign and board[5]==sign and board[8]==sign) or \
        (board[0]==sign and board[4]==sign and board[8]==sign) or \
        (board[2]==sign and board[4]==sign and board[6]== sign):

        return True
    else:
        return False

def continue_play():
    # Function to continue playing after winning/draw
    a = input('Do you want to play again? (y,n) ')
    if a == 'n':
        return False
    else:
        return True

def board_full(board):
    # check whether the board is full or not
    if ' ' not in board:
        return True
    else:
        return False


# ---------------------------------------------- #


print(' #-------- WELCOME TO TIC TAC TOE! --------#')

while True:
    board = [' '] * 9
    print(' This is the board you are going to play with')
    displayBoard(board)
    player1Marker, player2Marker = chooseSign()
    print(f'Player 1: {player1Marker}')
    print(f'Player 2: {player2Marker}\n')

    turn = who_starts()
    game_on = True

    while game_on:

        if turn == 'Player 1':
            print("Player 1's turn")
            pos = choose_position()
            make_move(board,pos,player1Marker)
            displayBoard(board)
            if check_win(board,player1Marker):
                print('Player 1 wins!')
                game_on = False
            else:
                if board_full(board):
                    print("It's a draw!")
                    game_on = False
                else:
                    turn = 'Player 2'

        if turn == 'Player 2':
            print("Player 2's turn")
            pos = choose_position()
            make_move(board,pos,player2Marker)
            displayBoard(board)
            if check_win(board,player2Marker):
                print('Player 2 wins!')
                game_on = False
            else:
                if board_full(board):
                    print("It's a draw!")
                    game_on = False
                else:
                    turn = 'Player 1'

    if not continue_play():
        break