# counter = 0
# while True:
#   answer = int(input("Enter a number: "))
#   print("Adding it up!")
#   counter += answer
#   print("Current total is", counter)
#   addAnother = input("Add another? ")
#   if addAnother == "no":
#     break
# print("Bye!")

# __________________________

# counter = 0
# while True:
#   answer = int(input("Enter a number: "))
#   print("Adding it up!")
#   counter += answer
#   print("Current total is", counter)
#   addAnother = input("Add another? ")
#   if addAnother == "no":
#    break
# print("Bye!")
# ___________________________________

# while True:
#   color = input("Enter a color: ")
#   if color == "red":
#    break
#   else:
#     print("Cool color!")
# print("I don't like red")

# ___________________________________

counter=0
print("Fill in the blank lyrics!")
print()
print("\(Type in the blank lyrics and see! if you are as cool as me.)")
print()
while True:
   word=input("Never going to ______ you up.\n")
   counter += 1
   if word=="give" or word=="Give":
      print("Well done! It only took you",counter,"attempts.")
      break
   else:
      print("Nope, try again.")
