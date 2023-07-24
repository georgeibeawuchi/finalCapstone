import math

# The main menu
def menu():
    print("[investment] option - to calculate the amont of interest you'll earn on your investment")
    print("[bond] option - to calculate the amount you'll have to pay on a home loan")

# The main option
menu()
option = str(input("Enter either 'investment' or 'bond' from the menu above to proceed \n")).lower()

# Option if user selects an option
if option == "investment":
    p = int(input("How much money will you be depositing? \n"))
    r = int(input("What is the interest rate? \n"))
    r = (r/100)
    t = int(input("What are the number of years that you plan to invest the money? \n"))

    # Two options within first option with calculations and an output
    interesttype = str(input("simple or compound interest? \n")).lower()
    if interesttype == "simple":
      
      simple = p*(1 + r*t)
      
      print(simple)

    elif interesttype == "compound":
      a = p * math.pow((1+r),t)

      print(a)

# Option if user selects another option (includes inputs, a calculation and an output)
elif option == "bond":
   p = int(input("What is the present value of the house? \n"))
   i = int(input("What is the interest rate? \n"))
   i = ((i/100)/12)
   n = int(input("What is the number of months you plan to repay the bond? \n"))
   
   
   repayment = (i * p)/(1 -(1 + i)**(-n))

   print(repayment)
   
# This is a statement if the user enters an invalid input
else:
   print("Please try again with a valid input.")
   menu()
option = str(input("Enter either 'investment' or 'bond' from the menu above to proceed \n")).lower()

# Option if user selects an option
if option == "investment":
    p = int(input("How much money will you be depositing? \n"))
    r = int(input("What is the interest rate? \n"))
    r = (r/100) / 12
    t = int(input("What are the number of years that you plan to invest the money? \n"))

    # Two options within first option with calculations and an output
    interesttype = str(input("simple or compound interest? \n")).lower()
    if interesttype == "simple":
      
      simple = p*(1 + r*t)
      
      print(simple)

    elif interesttype == "compound":
      a = p * math.pow((1+r),t)

      print(a)

# Option if user selects another option (includes inputs, a calculation and an output)
elif option == "bond":
   p = int(input("What is the present value of the house? \n"))
   i = int(input("What is the interest rate? \n"))
   i = ((i/100)/12) / 12
   n = int(input("What is the number of months you plan to repay the bond? \n"))
   
   
   repayment = (i * p)/(1 -(1 + i)**(-n))

   print(repayment)
   
