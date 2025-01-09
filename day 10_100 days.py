# adding = 4 + 3
# print(adding)

# subtraction = 8 - 9
# print(subtraction)

# multiplication = 4 * 32
# print(multiplication)

# division = 50 / 5
# print(division)

# # a number raised to the power of some number
# # in this example we raise 5 to the power of 2
# squared = 5**2
# print(squared)

# # remainder of a division
# modulo = 15 % 4
# print(modulo)

# # whole number division
# divisor = 15 // 2
# print(divisor)
# _________________________________
# myBill = float(input("What was the bill?: "))
# numberOfPeople = int(input("How many people?: "))
# answer = myBill / numberOfPeople
# answer = round(answer, 2)
# print("You all owe", answer)
# ______________________________________
print("Tip Calculator")
print(" ")
myBill=float(input("How much did you spend? "))
myTip=float(input("What percentage you want to tip? "))
numberOfPeople=int(input("How many people in your group? "))
billWithTip=myTip/100*myBill+myBill
# print("Total Bill With Tip",billWithTip)
answer=billWithTip/numberOfPeople
answer=round(answer,2)
print("You each owe", answer)

