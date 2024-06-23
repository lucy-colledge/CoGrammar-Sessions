print ("")
print ("This application will work out the price of a holiday.")
print ("")

#city_flight = city they will fly to 
#create some options
def flight_options():
    print("Options:")
    print("p = Paris") # 186 total 6day = 1473.06
    print("b = Berlin") #40 total 6day = 1327.06
    print("r = Rome") #99 total 6day = 1386.06
    print("c = Cancel")

flight_options()
city_flight = input("Please choose a destination city or enter c to cancel:")
print ("")
#tidy layout newline

#num_nights = nights in hotel
num_nights = input ("Please let us know how many nights you will need to stay in a hotel for: ")
print ("")
#tidy layout newline

#num_nights = nights in hotel
rental_days = input("And how many days will you need to rent a vehicle for: ")

#function hotel_cost() 
# take num_nights as argument
def hotel_cost():
    hotel_formula = (float(num_nights) * float(164.95))
    return float(round(hotel_formula,2))

#function plane_cost() 
# take city_flight as argument
def plane_cost():
    if city_flight == "p":
        return float(186.28)
    elif city_flight == "b":
        return float(39.99)
    elif city_flight == "r":
        return float(98.98)
    elif city_flight == "c":
        print("Thank you, Goodbye.")
    else:
        print("Unrecognised option.")

#function car_rental() 
# take rental_days as argument
def car_rental():
    car_formula = (float(rental_days) * float(48.51))
    return float(round(car_formula,2))

#function holiday_cost() 
# take num_nights, city_flight & rental_days as argument
#  use hotel_cost, plane_cost and car_rental 
#   return total cost

def holiday_cost():
    total = hotel_cost() + plane_cost() + car_rental()
    print(f"Your holiday to {city_flight} for {num_nights} nights, including Hotel and Hire car costs will be £ {total}")
    print(f"Flights = £ {plane_cost()}")
    print(f"Hotel = £ {hotel_cost()}")
    print(f"Hire Car = £ {car_rental()}")

holiday_cost()