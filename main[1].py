#U3L3 Tic-Tac-Toe
# Hiba Altaf

#displays a menu that allows the user to choose whether they want a 2 player game or a game with the computer. 
#draw the board if the user chooses to play.
#take in user inputs and place them on the board
#after each turn have function that checks whether there is a winner by looking at the rows, columns, and diagonals.
#once all the slots are filled or if there is a winner, the game displays who won. Otherwise, the game tells the user that there is a tie. 


import random

#this function resets the 3 by 3 matrix such that each index is a number from 1-9 ordered from top left to bottom right. 
def reset_board():
  global board
  board = [['1','2','3'],
            ['4','5','6'],
            ['7','8','9']]
  return

#this function draws the board with the changes caused by the users' inputs. 
#the board is displayed as an aligned 3 by 3 matrix.
def draw_board():
  for row in board:
      for value in row:
        print(value, end = "  ")
      print()    

#these lists store the values of each column and diagonal in a seperate list. 
#the columns list stores all 3 columns and the diagonals list stores all 3 diagonals. 
column1_val = []
column2_val = []
column3_val = []
columns = [column1_val, column2_val, column3_val]

diagonal1_val = []
diagonal2_val = []
diagonals = [diagonal1_val, diagonal2_val]

#this function checks who won the game. It is run when it is called in two_players() or play_with_comp. 
#it checks each row to see if the values in the rows are identical. It then checks the columns in the grid and see if the values are identical. Finally, it checks the values of the diagonals to see if they are identical.
# If any of these conditions are true, then it prints a statement, declaring the winner and returns 'DONE'.

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

#this function is run when it is called in the play_with_comp() function.
#it checks if the human player is about to win. It does this by checking each row, column, and diagonal and seeing if it can find 2 of the player's symbols. If it can, then it finds the unfilled space in that segment that it needs to fill in order to prevent the player from winning. It then records what row that space is in using a global variable go_to_row. It also records which index the space is in the row and stores that value in global variable go_to_value.
#it stores these values so the computer can access and use them to plot its symbol on that space.

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

#this function is run when the user enters 2.
#at the start of each game, the board resets to its inital state(with numbered spaces).  
#the function asks each player to enter the space on which they will plot their X or O, and after the user enters a value, it then reprints the board with the symbol plotted on the corresponding space. If the user does not enter an integer less than 10 for their input, they get an error message and asked to enter another value. 
#each time a player enters a value, this function uses the check_for_winner() function to check if there is a winner before the next player can plot a value. If check_for_winner() shows that one of the players have won then the function displays the menu. 
#if the board is filled up and there is no winner then the function prints a statement informing the reader of this.

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

# this function is run with the user enters 3
#at the start of each game, the board resets to its inital state(with numbered spaces). 
# this allows the user to play with the computer. The player first chooses if they want to be X or O. The function then asks the player to enter the space on which they will plot their X or O, and plots the player's symbol in that space on the board. If the user does not enter an integer less than 10 then they get an error message and are asked for another input. 
#if the player did not win then the function checks if the player is about to win by running the about_winner() function. If that function does return values for go_to_row and go_to_value, then the computer plots its symbol on the space that leads to board[go_to_row][go_to_value]
#if the player has not won and is not about to win, then the function picks a random number from 1 to 9 and plots its symbol on the corresponding space.
#the function runs the checks_for_winner() function to see if someone has won each time the player and computer play their turns. If they have, then the menu is displayed.
#if the board is filled up and there is no winner then the function prints a statement informing the reader of this.

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

#this function is run when the user enters 3.
#it allows the user to exit the game. However, the user can reenter the game by entering 1. 
def exit():
  print('Thanks for playing!')
  user_exit = input('Enter 1 to reenter the game: ')
  if user_exit == '1':
    display_menu()
  return

#this function displays the menu to the user.
#it runs different functions based on the user's input. If the user enters 1, then reset_board() is run which sets the board into the format with numbered spaces. This board is then printed to the user.  If the user enters 2, two_players() is run which allows 2 human players to play the game. If the user enters 3, play_with_comp() is run which allows 1 player to play the game with the computer. If the user enters 4, exit() is run which allows them to exit the game.
#if the user does not enter one of the listed numbers then they get an error message and are asked to try again. 
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
    