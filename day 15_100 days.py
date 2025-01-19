# counter=0
# while counter<10:
#    print(counter)
#    counter+=1
# ______________________________________
# exit=""
# while exit!="yes":
#    print("🥳")
#    exit=input("Exit?: ")
# ______________________________________
exit=""
while exit!="yes":
   animal=input("what animal do you want? ")
   if animal=="cow":
      print("🐮 Moo")
   elif animal=="sheep":
      print("🐑 Baaaa")
   elif animal=="cat":
      print("🐈 Meow")
   elif animal=="duck":
      print("🦆 Quack")
   elif animal=="dog":
      print("🐶 Woof")
   else:
      print("Dont know the animal sound.")
   exit=input("Do you want to exit? ")