#this is the function for the hotel cost
def hotel_cost(nights):
    return nights * 875



#this is the function for the plane cost
def plane_cost(city):
    #city = range(4)
    
    if city == 1:
        city = 750
        
            
    elif city == 2:
        city = 850
            

    elif city == 3:
        city = 600
            

    else:
        print("You have selected an invalid option")
    
    return city



#this is the function for the car rental cost
def car_rental(days):
    return days * 275



#this is the function for the holiday cost
def holiday_cost(nights, city, days):
    nights = hotel_cost(nights)
    ticket = plane_cost(city)
    days = car_rental(days)
    return nights + city + days



#these inputs define the city of flight, number of nights stayed and the car rentalm duration
nights = int(input("How many nights will you be staying? "))
city = int(input("\n1. London\n2. Rome\n3. Paris\nWhere you flying to? "))
days = int(input("How many days will you need a car for?: "))
total = holiday_cost(nights, city, days)

if days > nights:
    print("Please make sure that the days you need to hire a car does not exceed the amount of nights that you need to stay.")

#this prints the hotel cost, the plane cost, the car rental cost and the total cost
print("This is the hotel cost ")
print(hotel_cost(nights))

print("This is the plane cost " )
print(plane_cost(city))

print("This is the car rental cost ")
print(car_rental(days))

print("This is the total cost " )
print(total)