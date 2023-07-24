n = int(input("Enter a number: "))

numberlist = []

while n != -1:
    numberlist.append(n)
    
    n = int(input())

    numbersum = sum(numberlist)

print(f"The averge of these numbers are: {numbersum / len(numberlist)}")