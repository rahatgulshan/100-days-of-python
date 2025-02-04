print()
print("=============Guess the Number 🔢================")
print()
print(" Rules 📜: Choose your number betwween 1 to 100,000 I will tell you based on your answer if its too low,too high or get it correct.")
print()
correct_Num=5500
attempt=1
while True:
   user_Num=int(input("Choose your number betwween 1 to 100,000 >: "))
   print()
   if user_Num < 0:
      print("-ve Value not allowed 💀.")
      exit()
   if user_Num > correct_Num:
      print("Its too high 😁")
      attempt += 1
   elif user_Num < correct_Num:
      print("Its too low 🤣")
      attempt += 1
      continue
   elif user_Num == correct_Num:
      print("Its Correct! You are the winner 🥳")
      break
   else:
      print("invalid input detected ❌")
print("It took you", attempt,"attempt(s) to get the correct answer.")
   