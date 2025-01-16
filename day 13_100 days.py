print("Exam Grade Calculator")
exam=input("Name of Exam: ")
TotalScore=int(input("Max. Possible Score: "))
yourScore=int(input("Your Score: "))
result=(yourScore*100)/TotalScore
result=round(result,2)
if (yourScore>=90):
   print("You got", result, " which is a A+")
elif (yourScore>=80 and yourScore<90):
   print("You got", result, "which is a A-")
elif (yourScore>=70 and yourScore<80):
   print("You got", result, "which is a B")
elif (yourScore>=60 and yourScore<70):
   print("You got", result, "which is a C")
elif (yourScore>=50 and yourScore<60):
   print("You got", result, "which is a D")
elif (yourScore>=40 and yourScore<50):
   print("You got", result, "which is a U")
else:
   print("You got", yourScore, "which is very low")
