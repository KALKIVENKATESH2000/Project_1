cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers # subtraction
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car # Mutlipication
average_passangers_per_car = passengers / cars_driven # division

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available." )
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passangers_per_car, "in each car.")
