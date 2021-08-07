
import random

def reset_board():
  global board
  board = [['1','2','3'],
            ['4','5','6'],
            ['7','8','9']]
  return

def draw_board():
  for row in board:
      for value in row:
        print(value, end = "  ")
      print()    
      
column1_val = []
column2_val = []
column3_val = []
columns = [column1_val, column2_val, column3_val]

diagonal1_val = []
diagonal2_val = []
diagonals = [diagonal1_val, diagonal2_val]


def check_for_winner():

  for row in board:
    if row[0] == row[1] == row[2]:
      print(row[0] + ' is the winner')
      return 'DONE'
  
  for column in columns:
    column.clear()
  
  for row in board:
    column1_val.append(row[0])
    column2_val.append(row[1])
    column3_val.append(row[2])

  for column in columns:
      if column[0] == column[1] == column[2]:
        print(column[0] + ' is the winner')
        return 'DONE'

  for diagonal in diagonals:
    diagonal.clear()
  
  diagonal1_val.append(board[0][0])
  diagonal2_val.append(board[0][2])
  diagonal1_val.append(board[1][1])
  diagonal2_val.append(board[1][1])
  diagonal1_val.append(board[2][2])
  diagonal2_val.append(board[2][0])
  
  for diagonal in diagonals:
    if diagonal[0] == diagonal[1] == diagonal[2]:
      print(diagonal[0] + ' is the winner')
      return 'DONE'

def almost_winner():
  global go_to_row
  go_to_row = ''
  global go_to_value
  go_to_value = ''
  for row in board:
    if row.count(player) == 2:
      for value in row:
        if value != player:
          x = value
          if x != computer:
            go_to_row = board.index(row)
            go_to_value = row.index(x)
  for column in columns:
    if column.count(player) == 2:
        for value in column:
          if value != player:
            x = value
            if x != computer:
              for row in board:
                if x in row:
                  go_to_row = board.index(row)
                  go_to_value = row.index(x)
  for diagonal in diagonals:
    if diagonal.count(player) == 2:
        for value in diagonal:
          if value != player:
            x = value
            if x != computer:
              for row in board:
                if x in row:
                  go_to_row = board.index(row)
                  go_to_value = row.index(x)

def two_players():
  
  reset_board()
  draw_board()

  while check_for_winner() != 'DONE':
    
    p1_input = input('Enter where you want to place X: ')
    if p1_input.isdigit() and int(p1_input) < 10:
      for row in board:
        for value in row:
          if p1_input == value:
            row[row.index(value)] = 'X'
    else:
      print('Please enter one of the numbers shown on the tic tac toe board.')
      p1_input = input('Enter where you want to place your symbol: ') 

    for row in board:
      for value in row:
        if p1_input == value:
          row[row.index(value)] = 'X'
    draw_board()
   
    if check_for_winner() == 'DONE':
      display_menu()
    else:
      num_int = 0
      for row in board:
        for value in row:
          if value.isdigit():
            num_int += 1
      if num_int == 0: 
        print('There is no winner.')
        display_menu()
      else:
        p2_input = input('Enter where you want to place O: ')
        if p1_input.isdigit() and int(p2_input) < 10:
          for row in board:
            for value in row:
              if p1_input == value:
                row[row.index(value)] = 'X'
        else:
          print('Please enter one of the numbers shown on the tic tac toe board.')
          p1_input = input('Enter where you want to place your symbol: ')  

        for row in board:
          for value in row:
            if p2_input == value:
              row[row.index(value)] = 'O'

        draw_board()
        if check_for_winner() == 'DONE':
          display_menu()
          
def play_with_comp():
  p2_inputs = []
  p1_inputs = []
  reset_board()
  draw_board()

  global player
  global computer
  player = input('Do you want to be X or O: ')
  while player != 'O' and player != 'X':
    print('Please enter either X or O.')
    player = input('Do you want to be X or O: ')
  
  while check_for_winner() != 'DONE':
    
    p1_input = input('Enter where you want to place your symbol: ')
    if p1_input.isdigit() and int(p1_input) < 10:
      for row in board:
        for value in row:
          if p1_input == value:
            row[row.index(value)] = player
            p1_inputs.append(p1_input)
    else:
      print('Please enter one of the numbers shown on the tic tac toe board.')
      p1_input = input('Enter where you want to place your symbol: ') 
    
    if check_for_winner() == 'DONE':
      display_menu()
    else:
      num_int = 0
      for row in board:
        for value in row:
          if value.isdigit():
            num_int += 1
      if num_int == 0: 
        print('There is no winner.')
        display_menu()
      else:
        if player == 'O':
          computer = 'X'
        elif player == 'X':
          computer = 'O'
        almost_winner()
        if go_to_row == '':
          p2_input = str(random.randint(1,9))
          
          while p2_input in p1_inputs or p2_input in p2_inputs:
            p2_input = str(random.randint(1,9))
           
        else:
          p2_input = board[go_to_row][go_to_value]

        p2_inputs.append(p2_input)
        
        for row in board:
          for value in row:
            if p2_input == value:
              row[row.index(value)] = computer
        draw_board()
        if check_for_winner() == 'DONE':
          display_menu()

def exit():
  print('Thanks for playing!')
  user_exit = input('Enter 1 to reenter the game: ')
  if user_exit == '1':
    display_menu()
  return

def display_menu():
  print("""
    1- Display menu
    2- 2 player game
    3- Play with computer
    4- Exit""")
  user_input = input('Enter the appropriate number: ')
  if user_input == '1':
    reset_board()
    for row in board:
      for value in row:
        print(value, end = "  ")
      print()
    display_menu()
  elif user_input == '2':
    two_players()
  elif user_input == '3':
    play_with_comp()
  elif user_input == '4':
    exit()
  else:
    print('Enter 1, 2, 3, or 4 in order to proceed. Check the menu for help.')
    display_menu()
display_menu()
    
