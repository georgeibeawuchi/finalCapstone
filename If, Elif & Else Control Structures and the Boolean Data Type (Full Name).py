fullname = input("Enter your full name: /n").strip()

#If statement on if user has entered nothing
if len(fullname) == 0:
    print("You haven't entered anything. Please enter your full name")

#If statemrnt on if user has entered less than 4 characters
elif len(fullname) < 4:
     print("'You have entered less than 4 characters. Please make sure that you have entered your name and surname.")

#If statemrnt on if user has entered more than 25 characters
elif len(fullname) > 25:
     print("'You have entered more than 25 characters. Please make sure that you have only entered your name and surname.")
else: print("Thank you for entering your name")
