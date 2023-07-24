
# n is declared as 0 firstly
n = 0

# user is asked politely to enter a number
n = int(input("Please enter a number \n"))

# total number a sum of mathematics is declared.
totalnum = n
sum = 0

# while loop with -1 as a stoppage to its function
while n != -1:
 
      n = int(input("Please enter a number \n"))
      sum += n
      #n -= 1

      print(sum)

# average equation
average = sum / totalnum

# this prints the average.
print(average)