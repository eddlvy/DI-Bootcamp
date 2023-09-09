

board = [
  [" "," "," "],
  [" "," "," "],
  [" "," "," "]
]








# BOARD FUNCTION


def print_board():

  print("")
  print("Welcome to TIC TAC TOE")
  print("")




  print()
  
  
  print("           TIC TAC TOE")
  print(" ******************************")
  print(f"       {board[0][0]}    |    {board[0][1]}   |    {board[0][2]}   ")
  print(" ------------------------------")
  print(f"       {board[1][0]}    |    {board[1][1]}   |    {board[1][2]}   ")
  print(" ------------------------------")
  print(f"       {board[2][0]}    |    {board[2][1]}   |    {board[2][2]}   ")
  print(" ******************************")

# print_board()

# number = 1



# PLAYER 1 INPUT

def player_1_input():
 
    player_input_row = int(input(f"Player number 1 \nEnter the row number from 1 to 3 \n"))
    player_input_column = int(input(f"Player number 1 \nEnter the column number from 1 to 3 \n"))
    for row in range(len(board)):
      if row == player_input_row -1:
       for item in range(len(board[row])):
         item = player_input_column -1
         if board[row][item] == " ":
             board[row][item] = "X"
             return board[row][item]
         else:
           print("That space is taken, try again :)")
       break
           
              
   
             

# PLAYER 2 INPUT

def player_2_input():         
  
    player_input_row = int(input(f"Player number 2 \nEnter the row number from 1 to 3 \n"))
    player_input_column = int(input(f"Player number 2 \nEnter the column number from 1 to 3 \n"))
    for row in range(len(board)):
      if row == player_input_row -1:
       for item in range(len(board[row])):
         item = player_input_column -1
         if board[row][item] == " ":
             board[row][item] = "O"
             return board[row][item]
         else:
           print("That space is taken, try again :)")
       break
           
    
             
             
           
         
# def draw_conditions():
#   for i in range(len(board)):
#     for j in range(len(board[i])):
#       if " " not in board[i][j]:
#         print("It's a draw :)")
#         break
        
# def winning_conditions():
  # if board[0][0] == board[0][1] ==board[0][2]=="X" or \
  #    board[1][0] == board[1][1] ==board[1][2]=="X" or \
  #    board[2][0] == board[2][1] ==board[2][2]=="X" or \
  #    board[0][0] == board[1][1] ==board[2][2]=="X" or \
  #    board[2][0] == board[1][1] ==board[0][2]=="X" or \
  #    board[0][0] == board[1][0] ==board[2][0]=="X" or \
  #    board[0][2] == board[1][2] ==board[2][2]=="X":
  #   print("Player 1 Wins ;)*************************")
  # elif board[0][0] == board[0][1] ==board[0][2]=="O" or \
  #    board[1][0] == board[1][1] ==board[1][2]=="O" or \
  #    board[2][0] == board[2][1] ==board[2][2]=="O" or \
  #    board[0][0] == board[1][1] ==board[2][2]=="O" or \
  #    board[2][0] == board[1][1] ==board[0][2]=="O" or \
  #    board[0][0] == board[1][0] ==board[2][0]=="O" or \
  #    board[0][2] == board[1][2] ==board[2][2]=="O":
  #   print("Player 2 Wins ;)********************")
  # elif " " not in board:
  #   print("It's a draw :)")

# player_1 = player_1_input()
# player_2 = player_2_input()
# number = 1
# number = 0

while True:
  print_board()
  player_1_input()
  # draw_conditions()
  # number +=1
  print_board()
  player_2_input()
  # draw_conditions()
  
  # winning_conditions()
  # number +=1

  
 



  


  
 


   





          

 

         




       


  
  
         


         
         


       
         


        


           

           
         

 
        






 
 
     
     
     
  


  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  # player_input = int(input(f"Player number {number} \nEnter a grid number from 1 to 9 to place the mark "))
  # print(player_input)
  # if 1 <= player_input <= 9:
  #  for x in range(len(board)):
  #    for j in range(len(board[x])):
  #        if board[x][j] == " ":
  #           board[x][j] = "X" 
  #           number += 1


          
        
     
         
          
          
           
             
       
       
       
        #   for j in range(len(board[x])):
        #  if board[x][j] == " ":
        #   board[x][j] = "X" 
        #   number += 1 :
        #   print("Grid Occupied, Try another number")
        #   continue
          
  
  
# PLAYER 2 INPUT 
         

# def player_input_o():
#   player_input_2 = int(input("Player number 2 \nEnter a grid number from 1 to 9 to place the mark "))
  
#   for k in range(len(board)):
#      print(player_input_2)
#      if 1 <= player_input_2 <= 9:
#         for j in range(len(board[k])):
#          if board[k][j] == "":
#           board[k][j] = "O" 
#           return (board[k][j])
#          else:
#           print("Grid Occupied, Try another number")
#           continue
          
         

# def check_winning_conditions():
#   if board[0][0] == board[0][1] ==board[0][2]=="X" or \
#      board[1][0] == board[1][1] ==board[1][2]=="X" or \
#      board[2][0] == board[2][1] ==board[2][2]=="X" or \
#      board[0][0] == board[1][1] ==board[2][2]=="X" or \
#      board[0][2] == board[1][1] ==board[2][0]=="X" or \
#      board[0][0] == board[1][0] ==board[2][0]=="X" or \
#      board[0][2] == board[1][2] ==board[2][2]=="X":
#     print("Player 1 Wins") 
#   else:
#     print("Player 2")

# # to evaluate draw check  with a function if check_winnin_conditions == True

# def is_draw():
#   if check_winning_conditions == False:
#     print("Is a draw")

# # GAMEPLAY 

# def play_game():
#   print_board()
#   player_input()
#   print_board()
  
  


# play_game()



  


    
     
   

                 


  


  
  
         
          
        






         
       

       






