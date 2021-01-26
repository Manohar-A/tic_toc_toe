# need a board
#we have to display the board
# play the game   
#handle the inputs 
#handle the turns
#check Win 
#check tie 

#game board to play game
game_board = ['-','-','-',
              '-','-','-',
               '-','-','-']
#displaying the board
def display_game():
  global game_board
  print(game_board[0],game_board[1],game_board[2])
  print(game_board[3],game_board[4],game_board[5])
  print(game_board[6],game_board[7],game_board[8])



#initialising the players
curr_player = 'x'
game_is_running = True

def handle_input():
  global curr_player
  position = int(input("choose an empty position : "))
  position -= 1
  if(game_board[position] != '-'):
    print('invalid input, select a valid position : ')
  else:
    game_board[position] = curr_player
    handle_turn()
def handle_turn():
  global curr_player
  if(curr_player == 'x'):
    curr_player = 'O'
  else:
    curr_player = 'x'


#game ending scenario

#one of them wins
def check_win():
  row_win = row_check()
  column_win = column_check()
  diagonal_win = diagonal_check()
  if(row_win or column_win or diagonal_win):
    return True
  return False

def row_check():
  global game_is_running
  row1 = game_board[0] == game_board[1] == game_board[2] != '-'
  row2 = game_board[3] == game_board[4] == game_board[5] != '-'
  row3 = game_board[6] == game_board[7] == game_board[8] != '-'
  if(row1 or row2 or row3):
    game_is_running = False
    return True
  return False

def column_check():
  global game_is_running
  column1 = game_board[0] == game_board[3] == game_board[6] != '-'
  column2 = game_board[1] == game_board[4] == game_board[7] != '-'
  column3 = game_board[3] == game_board[5] == game_board[8] != '-'
  if(column1 or column2 or column3):
    game_is_running = False
    return True
  return False

def diagonal_check():
  global game_is_running
  diagonal1 = game_board[0] == game_board[4] == game_board[8] != '-'
  diagonal2 = game_board[2] == game_board[4] == game_board[6] != '-'
  if(diagonal1 or diagonal2):
    game_is_running = False
    return True
  return False




def check_tie():
  global game_is_running
  if('-' in game_board):
    return False
  game_is_running = False
  return True

#playing the game
def play_game():
  global curr_player
  global game_is_running
  while(game_is_running):
    display_game()
    handle_input()
    win = check_win()
    tie = check_tie()
  display_game()
  if(win):
    if(curr_player == 'x'):
      print("O's won")
    else:
      print("x's won")
  elif tie:
    print("ah! Its's a tie")

play_game()






