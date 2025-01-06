# myScore = int(input("Your score: "))
# if myScore > 100000:
#   print("Winner!")
# else:
#   print("Try again 😭")
# __________________________________________
# myPi = float(input("What is Pi to 3dp? "))
# if myPi == 3.142 :
#   print("Exactly!")
# else:
#   print("Try again 😭")
# ________________________________________
print("Generation Identifier")
print(" ")
intYear=int(input("Which Year were you born? "))
if intYear>=1883  and intYear<=1900:
   print("Lost Generation")
elif intYear>=1901  and intYear<=1927:
   print("Greatest Generation 🥳")
elif intYear>=1928  and intYear<=1945:
   print("Silent Generation 🤐")
elif intYear>=1946  and intYear<=1964:
   print("Baby Boomers 😘")
elif intYear>=1965  and intYear<=1980:
   print("Generation X 😎")
elif intYear>=1981  and intYear<=1996:
   print("Millennials 🤩")
elif intYear>=1997  and intYear<=2012:
   print("Generation Z 😄")
elif intYear>=2012:
   print("Generation Alpha 🥰")

else:
   print("You born out of range 😂")