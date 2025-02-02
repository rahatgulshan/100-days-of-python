# while True:
#   print("You are in a corridor, do you go left or right?")
#   direction = input("> ")
#   if direction == "left":
#     print("You have fallen to your death")
#     break
#   elif direction == "right":
#     continue
#   else:
#     print("Ahh! You're a genius, you've won")
#     exit()
# print("The game is over, you've failed!")
# ________________________________________________
from getpass import getpass as input
print("E P I C 🥌 📜 ✂ BATTLE")
print()
# Varables for score records
player1_score = 0
player2_score = 0
while True:
   print("Select your move (R, P or S)")
   print()
   player1=input("Player 1 >").upper() 
   player2=input("Player 2 >").upper() 
   if player1=="R":
      if player2=="R":
         print("Its a tie 😛")
      elif player2=="P":
         print("Player 1 wins 🥳")
         player1_score += 1
      elif player2=="S":
         print("Player 1 wins 🥳")
         player1_score += 1
      else:
         print("invalid input detected Player2 ❌")
         exit()
   elif player1=="P":
      if player2=="P":
         print("Its a tie 😛")
      elif player2=="R":
         print("Player 1 wins 🥳")
         player1_score += 1
      elif player2=="S":
         print("Player 2 wins 🥳")
         player2_score += 1
      else:
         print("invalid input detected Player2 ❌")
   elif player1=="S":
      if player2=="S":
         print("Its a tie 😛")
      elif player2=="R":
         print("Player 2 wins 🥳")
         player2_score += 1
      elif player2=="P":
         print("Player 1 wins 🥳")
         player1_score += 1
      else:
         print("invalid input detected Player2 ❌")
   else:
      print("invalid input detected player1 ❌")
   print("Player 1 has", player1_score, "wins.")
   print("Player 2 has", player2_score, "wins.")
   if player1_score==3 or player2_score==3:
      print("Thanks for playing!")
      exit()
      