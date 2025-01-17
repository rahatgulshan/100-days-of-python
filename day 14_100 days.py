from getpass import getpass as input
print("E P I C 🥌 📜 ✂ BATTLE")
print()
print("Select your move (R, P or S)")
print()
player1=input("Player 1 >").upper() 
player2=input("Player 2 >").upper() 
if player1=="R":
   if player2=="R":
      print("Its a tie 😛")
   elif player2=="P":
      print("Player 1 wins 🥳")
   elif player2=="S":
      print("Player 1 wins 🥳")
   else:
      print("invalid input detected Player2 ❌")
elif player1=="P":
   if player2=="P":
      print("Its a tie 😛")
   elif player2=="R":
      print("Player 1 wins 🥳")
   elif player2=="S":
      print("Player 2 wins 🥳")
   else:
      print("invalid input detected Player2 ❌")
elif player1=="S":
   if player2=="S":
      print("Its a tie 😛")
   elif player2=="R":
      print("Player 2 wins 🥳")
   elif player2=="P":
      print("Player 1 wins 🥳")
   else:
      print("invalid input detected Player2 ❌")
else:
   print("invalid input detected player1 ❌")