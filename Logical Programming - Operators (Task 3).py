
#This section asks for the user's input
swimming = int(input("What time did you clock in for swimming?"))
cycling = int(input("What time did you clock in for cycling?"))
running = int(input("What time did you clock in for running?"))

#This is the calculaton of the total time of all the user's activities
totaltime = swimming + cycling + running

#This if statement gives a certain award if the totaltime is less than or equal to 100
if totaltime <= 100:
 print("You have achieved Provincial Colours")

#This if statement gives a certain award if the totaltime is less than or equal to 105
elif totaltime <= 105:
 print("You have achieved Provincial Half Colours")

#This if statement gives a certain award if the totaltime is less than or equal to 110
elif totaltime <= 110:
 print("You have achieved Provincial Scroll")

#This if statement gives no award as the totaltime is over 110
else: print("No Award")
