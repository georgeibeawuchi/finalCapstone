import math

# these are the main equations in the code
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


# this is the layout of the menu options
print("Please select")
print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")

# this is the menu (may or may not be seen)
def menu():
  option = ''

  while option != 'equation' and option != 'open a file':

# this option is the functions of choices between equations

   option = str(input("Would you like to enter an equation or open a file? \n").lower())
 
   if option == 'equation':

   
       choice = input("Enter choice 1, 2, 3 or 4 \n")
  

       if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Please enter a number \n"))
            num2 = float(input("Please enter another number \n"))
        except ValueError:
            print("Invalid number. Please enter anew.")

  
        
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
            answer = (num1, "+", num2, "=", add(num1, num2))
            
            
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
            answer = (num1, "-", num2, "=", subtract(num1, num2))
            

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
            answer = (num1, "*", num2, "=", multiply(num1, num2))
            

        elif choice == '4':
            try:
                print(num1, "/", num2, "=", divide(num1, num2))
                answer = (num1, "/", num2, "=", divide(num1, num2))
            except ZeroDivisionError as e:
                print("Error: Cannot divide by zero")
                

        print(answer)
        
        # this part writes the content to the file

        with open("taskfile.txt", 'w') as filename:
         test_tup1 = (int(num1), int(num2))
         test_tup2 = (tuple(answer))

         
        
         string1 = "".join(str(test_tup1))
         ans_str = "".join(str(answer))
         #string2 = "".join(str(ans_str))

         test_tup = string1 + ans_str

         filename.write(str(test_tup))
         
 
        try:    
          user = input("Please enter 'taskfile' for the title of the filename. \n").lower()
        except FileNotFoundError:
          print("File {} not found")
          user = input("Please enter the correct file name. \n").lower()
        
        filename = user + ".txt"
        with open ("taskfile.txt", 'r') as filename:
                #print(f.readline())
         print(filename.read())
         filename.close()

  # this part opens the answers in a text file
   elif option == 'open':
     try:    
          user = input("Please enter 'taskfile' for the title of the filename. \n").lower()
     except FileNotFoundError:
          print("File {} not found")
          user = input("Please enter the correct file name. \n").lower()
        
     filename = user + ".txt"
        
     with open ("taskfile.txt", 'r') as filename:
                #print(f.readline())
         print(filename.read())
         filename.close()
menu()   
    
#option = str(input("Would you like to enter an equation or open a file? \n").lower())


        #except FileNotFoundError:
          #print("File {} not found".format(user))
          #user = input("Please enter the correct file name. \n").lower()
        
        
        
    # this function is the menu from whence the user can choose between 2 options
    # option = str(input("Would you like to enter another equation or see your answers? \n").lower())
    
    # this option is the functions of choices between equations
   # if option == "equation":
        

    #menu()
    
            
        
    
    # this if statement is the option of seeing all the answers in a text file

    
    #menu()    