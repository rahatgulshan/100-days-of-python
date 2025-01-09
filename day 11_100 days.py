days_this_year=int(input("Days this year? "))
days_in_year=365
days_in_leap_year=366
hours_in_day=24
minutes_in_hour=60
seconds_in_minutes=60
result=days_in_year*hours_in_day*minutes_in_hour*seconds_in_minutes
leap_year_result=days_in_leap_year*hours_in_day*minutes_in_hour*seconds_in_minutes
if days_this_year==366:
   print("Numbers of seconds in a leap year are: ","{:,}".format(leap_year_result),"seconds")
else:
   print("Numbers of seconds in a year are: ","{:,}".format(result), "seconds")
