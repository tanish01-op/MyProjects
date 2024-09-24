import random

#Display the board
def display_board(board):
    print('\n'*100)  
    print(board[1] + "|" + board[2] + "|" + board[3])
    print('-|-|-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-|-|-')
    print(board[7] + '|' + board[8] + '|' + board[9])
#c
def player_input():
    marker =-1
    while marker!="X" and marker!="O":
        marker = input("Enter X or O: ").upper()
        player1 = marker
        if player1=='X':
            return('X','O')
        else:
            return('O','X')
    
def place_marker(board, marker, position):
    board[position]=marker

#checks if player win or not
def win_check(board, mark):
    return ((board[1] == board[2] == board[3] == mark) or 
            (board[4] == board[5] == board[6] == mark) or 
            (board[7] == board[8] == board[9] == mark) or 
            (board[1] == board[4] == board[7] == mark) or 
            (board[2] == board[5] == board[8] == mark) or 
            (board[3] == board[6] == board[9] == mark) or 
            (board[1] == board[5] == board[9] == mark) or 
            (board[3] == board[5] == board[7] == mark))

#chose who go first
def choose_first():
    flip = random.randint(0,1)
    if flip==0:
        return 'Player 1'
    else:
        return 'Player 2'
 #check if    
def space_check(board, position):
    return board[position] == " "

#checks if board is full or not
def full_board_check(board):
    return all([space != " " for space in board[1:]])

def player_choice(board):
    position = -1
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input("Enter a number between(1-9)"))
    return position
    
def replay():
    k = input("Play again y or n: ").lower()
    if k == 'y':
        return True
    else:
        return False

print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    board = [' ']*10
    player1_marker,player2_marker = player_input()
    turn = choose_first()
    print( turn + " will go first")
    play_game = input("Enter yes or no for game: ")
    game_on = play_game == 'yes'
    #pass

    while game_on:
        #Player 1 Turn
        if turn == 'Player 1':
            display_board(board)
            position = player_choice(board)            
            place_marker(board,player1_marker,position)

            if win_check(board,player1_marker):
                display_board(board)
                print('Player 1 has won!!')
                game_on = False
            else:
                if full_board_check(board):
                    print('The game is tie')
                    game_on = False
                else:
                    turn = 'Player 2'
        
        # Player2's turn.
        else:
            display_board(board)
            position = player_choice(board)            
            place_marker(board,player2_marker,position)
            if win_check(board,player2_marker):
                display_board(board)
                print('Player 2 has won!!')
                game_on = False
            else:
                if full_board_check(board):
                    print('The game is tie')
                    game_on = False
                else:
                    turn = 'Player 1'    
            #pass

    if not replay():
        break                    
    
