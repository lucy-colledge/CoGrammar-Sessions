print ("")
print ("This application will work out the price of a holiday based on the nights you wish to stay for.")
print ("")
num_nights = input ("Please let us know how many nights you will need to stay in a hotel for: ")
print ("")
rental_days = input("And how many days will you need to rent a vehicle for: ")

hotel_formula = (float(num_nights) * float(164.95))
hotel_cost = round(hotel_formula,2)
car_formula = (float(rental_days) * float(48.51))
car_rental = round(car_formula,2)

def flight():
    print("Options:")
    print("p = Paris") # 186 total 6day = 1473.06
    print("b = Berlin") #40 total 6day = 1327.06
    print("r = Rome") #99 total 6day = 1386.06
    print("c = Cancel")

def layout():
    print("")
    print(f"Your holiday to Paris for {num_nights} nights, including Hotel and Hire car costs will be £ {holiday_cost}")
    print(f"Flights = £ {plane_cost}")
    print(f"Hotel = £ {hotel_cost}")
    print(f"Hire Car = £ {car_rental}")
    print("")

print("")
choice = ""
flight()
while choice != "c":
    choice = input("Please choose a destination city or enter c to cancel:")
    if choice == "p":
        plane_cost = 186.28
        holiday_cost = float(hotel_cost)+ float(car_rental)+ float(plane_cost)
        layout()

    elif choice == "b":
        plane_cost = 39.99
        holiday_cost = float(hotel_cost)+ float(car_rental)+ float(plane_cost)
        layout()

    elif choice == "r":
        plane_cost = 98.98
        holiday_cost = float(hotel_cost)+ float(car_rental)+ float(plane_cost)
        layout()

    elif choice == "c":
        print("")
        print("Thank you, Goodbye.")
        print("")
    else:
        print("")
        print("Unrecognised option.")
        print("")
        flight()
