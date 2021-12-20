#Import libraries
import random

#Initialize items
board = [[1,2,3],
		[4,5,6],
		[7,8,9]]
remaining_choices = [1,2,3,4,5,6,7,8,9]

#Functions used in game
def one_or_two_player():
    reply = int(input('How many players? one (1) or two (2): '))
    while reply not in [1,2]:
        reply = int(input('How many players? one (1) or two (2): '))
    return reply

def generate_board(board):
	return print(*board,sep='\n')

def player_picks_x_or_o():
	reply = str(input('Choose either X or O: ')).upper().strip()
	while reply not in ['X','O']:
		reply = str(input('Choose either X or O: ')).upper().strip()
	return reply

def who_goes_first(one_or_two):
    if one_or_two == 1:
        reply = str(input('Who goes first, Player (P) or Computer (C): ')).upper().strip()
        while reply not in ['C','P']:
            reply = str(input('Who goes first, Player (P) or Computer (C): ')).upper().strip()
        return reply
    if one_or_two == 2:
        reply = int(input('Who goes first, Player 1 (1) or Player 2 (2): '))
        while reply not in remaining_choices:
            reply = int(input('Who goes first, Player 1 (1) or Player 2 (2): '))
        return reply

def player_picks_spot():
	reply = int(input('Enter an available spot to play: '))
	while reply not in remaining_choices:
		reply = int(input('Enter an available spot to play: '))
	return reply

def horizontal_win(board):
	return any(len(set(i)) == 1 for i in board)

def vertical_win(board):
	first_column = board[0][0] == board[1][0] == board[2][0]
	second_column = board[0][1] == board[1][1] == board[2][1]
	third_column = board[0][2] == board[1][2] == board[2][2]
	return first_column or second_column or third_column

def diagnol_win(board):
	left_to_right = len(set([board[i][i] for i in range(3)])) == 1
	right_to_left = len(set([board[i][2-i] for i in range(3)])) == 1
	return left_to_right or right_to_left

def is_winner(board):
	return horizontal_win(board) or diagnol_win(board) or vertical_win(board)

def cats_game(board):
	if not is_winner(board):
		return remaining_choices == []
	else:
		return False

def computer_picks_spot():
	return random.choice(remaining_choices)

def update_board_players_move(players_spot):
	if players_spot in [1,2,3]:
		board[0][players_spot-1] = player_letter
	elif players_spot in [4,5,6]:
		board[1][players_spot-4] = player_letter
	else:
		board[2][players_spot-7] = player_letter 

def update_board_computer_move(computer_spot):
	if computer_spot in [1,2,3]:
		board[0][computer_spot-1] = computer_letter
	elif computer_spot in [4,5,6]:
		board[1][computer_spot-4] = computer_letter
	else:
		board[2][computer_spot-7] = computer_letter

def update_board_player1_move(player1_spot):
	if player1_spot in [1,2,3]:
		board[0][player1_spot-1] = player1_letter
	elif player1_spot in [4,5,6]:
		board[1][player1_spot-4] = player1_letter
	else:
		board[2][player1_spot-7] = player1_letter 

def update_board_player2_move(player2_spot):
	if player2_spot in [1,2,3]:
		board[0][player2_spot-1] = player2_letter
	elif player2_spot in [4,5,6]:
		board[1][player2_spot-4] = player2_letter
	else:
		board[2][player2_spot-7] = player2_letter

def is_game_over(board):
	return is_winner(board) or cats_game(board)


#Pick one player or two player
one_or_two = one_or_two_player()

#One player game
if one_or_two == 1:
    #Choose who gos first
    first_play = who_goes_first(one_or_two)

    #Pick letters they'll be using
    player_letter = player_picks_x_or_o()
    computer_letter = 'X' if player_letter == 'O' else 'O'

    #Print first board
    generate_board(board)

    #Playing for if player goes first
    if first_play == 'P':
        while not is_game_over(board):
            print('Player\'s turn:')
            players_spot = player_picks_spot()
            update_board_players_move(players_spot)
            remaining_choices.remove(players_spot)
            generate_board(board)
            player_is_winner = True
            if not is_game_over(board):
                print('Computer\'s turn:')
                computer_spot = computer_picks_spot()
                update_board_computer_move(computer_spot)
                remaining_choices.remove(computer_spot)
                generate_board(board)
                player_is_winner = False

    #Playing for if computer goes first
    if first_play == 'C':
        while not is_game_over(board):
            print('Computer\'s turn:')
            computer_spot = computer_picks_spot()
            update_board_computer_move(computer_spot)
            remaining_choices.remove(computer_spot)
            generate_board(board)
            player_is_winner = False
            if not is_game_over(board):
                print('Player\'s turn:')
                players_spot = player_picks_spot()
                update_board_players_move(players_spot)
                remaining_choices.remove(players_spot)
                generate_board(board)
                player_is_winner = True

    #Write who won
    if player_is_winner and not cats_game(board):
        print('Player has beaten the computer!')
    elif not player_is_winner and not cats_game(board):
        print('Computer has beaten the player!')
    else:
        print('Cats game! It\'s a tie!')



#Two player game
if one_or_two == 2:
    #Choose who gos first
    first_play = who_goes_first(one_or_two)

    #Pick letters they'll be using
    player1_letter = player_picks_x_or_o()
    player2_letter = 'X' if player1_letter == 'O' else 'O'

    #Print first board
    generate_board(board)

    #Playing for if player goes first
    if first_play == 1:
        while not is_game_over(board):
            print('Player 1\'s turn:')
            player1_spot = player_picks_spot()
            update_board_player1_move(player1_spot)
            remaining_choices.remove(player1_spot)
            generate_board(board)
            player1_is_winner = True
            if not is_game_over(board):
                print('Player 2\'s turn:')
                player2_spot = player_picks_spot()
                update_board_player2_move(player2_spot)
                remaining_choices.remove(player2_spot)
                generate_board(board)
                player1_is_winner = False

    #Playing for if computer goes first
    if first_play == 2:
        while not is_game_over(board):
            print('Player 2\'s turn:')
            player2_spot = player_picks_spot()
            update_board_player2_move(player2_spot)
            remaining_choices.remove(player2_spot)
            generate_board(board)
            player1_is_winner = False
            if not is_game_over(board):
                print('Player 1\'s turn:')
                player1_spot = player_picks_spot()
                update_board_player1_move(player1_spot)
                remaining_choices.remove(player1_spot)
                generate_board(board)
                player1_is_winner = True

    #Write who won
    if player1_is_winner and not cats_game(board):
        print('Player 1 has beaten Player 2!')
    elif not player1_is_winner and not cats_game(board):
        print('Player 2 has beaten Player 1!')
    else:
        print('Cats game! It\'s a tie!')


